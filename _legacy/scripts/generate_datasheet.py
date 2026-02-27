#!/usr/bin/env python3
"""
Generates or updates a detailed markdown datasheet for a Mozilla Common Voice
dataset using the Google Gemini Pro API.

This script performs the following steps:
1.  Calculates detailed statistics from a Common Voice dataset directory,
    including clip and sentence counts, recording hours, demographic data,
    contributor statistics, and text corpus analysis.
2.  Optionally reads an existing markdown datasheet for the same language.
3.  Constructs a highly specific, detailed prompt for the Gemini Pro model,
    bundling the new statistics and, if applicable, the existing markdown.
4.  Instructs the AI to either generate a new datasheet from scratch or
    intelligently update the existing one by replacing only the auto-generated
    statistical sections while preserving manual, human-written content.
5.  The prompt includes modern calls to action reflecting the current Common
    Voice contribution workflow (Speak, Listen, Write, Review) and adds
    other engaging content like a "Fun Fact" about the language.
6.  Outputs both the raw JSON data sent to the API and the final,
    AI-generated markdown to standard output.
"""
import argparse
import csv
import json
import logging
import os
import random
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from google import genai
except ImportError:
    print("Error: The new Google GenAI SDK ('google-genai') is not installed.")
    print("Please install it using: pip install google-genai")
    sys.exit(1)

# --- SCRIPT CONSTANTS ---
SENTENCE_THRESHOLD = 1000
AVG_CLIPS_THRESHOLD = 5
CSV_FIELD_SIZE_LIMIT = 10000000

# --- Configure Logging ---
logger = logging.getLogger(__name__)


# --- DATA LOADING ---


def read_tsv(file_path: Path) -> List[Dict[str, str]]:
    """
    Opens and reads a tab-separated values (TSV) file from the given path.
    """
    logger.info(f"Reading data from {file_path.name}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f, delimiter="\t"))
    except FileNotFoundError:
        logger.warning(
            f"Optional file not found: {file_path}. Proceeding without it."
        )
        return []
    except Exception as e:
        logger.error(
            f"Fatal: An error occurred while reading {file_path}: {e}"
        )
        sys.exit(1)


# --- STATS CALCULATION ---


def get_hours(data: List[Dict[str, str]], durations: Dict[str, int]) -> float:
    """
    Calculates the total duration in hours for a specific subset of audio clips.
    """
    logger.info("Calculating clip hours for a subset of data...")
    total_ms = sum(durations.get(row["path"], 0) for row in data)
    return total_ms / (1000 * 60 * 60)


def get_demographics(data: List[Dict[str, str]]) -> Dict[str, Counter]:
    """
    Analyzes clip metadata to extract and count demographic information.
    """
    logger.info("Calculating demographic statistics (gender, age, accent)...")
    accents = [s for row in data if (s := row.get("accents", ""))]
    return {
        "gender": Counter(
            row.get("gender") for row in data if row.get("gender")
        ),
        "age": Counter(row.get("age") for row in data if row.get("age")),
        "accent": Counter(accents),
    }


def get_contributor_stats(data: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Calculates the distribution of contributions per user.
    """
    logger.info("Calculating contributor statistics...")
    clips_per_contributor = Counter(row["client_id"] for row in data)
    bins = {"1-10": 0, "11-50": 0, "51-100": 0, "101-500": 0, ">500": 0}
    for count in clips_per_contributor.values():
        if 1 <= count <= 10:
            bins["1-10"] += 1
        elif 11 <= count <= 50:
            bins["11-50"] += 1
        elif 51 <= count <= 100:
            bins["51-100"] += 1
        elif 101 <= count <= 500:
            bins["101-500"] += 1
        else:
            bins[">500"] += 1
    return bins


def get_text_corpus_stats(
    validated_sentences: List[Dict[str, str]],
    validated_clips: List[Dict[str, str]],
) -> Dict[str, Any]:
    """
    Performs a deep analysis of the dataset's text sentences.
    """
    logger.info("Analyzing text corpus statistics...")
    used_sentences = [
        row for row in validated_sentences if row.get("is_used") == "1"
    ]
    clips_counts = [int(row.get("clips_count", 0)) for row in used_sentences]
    all_text = [
        row["sentence"] for row in validated_clips if "sentence" in row
    ]
    total_tokens = sum(len(s.split()) for s in all_text)
    total_chars = sum(len(s) for s in all_text)

    return {
        "unique_sources": sorted(
            list(
                set(
                    row["source"]
                    for row in used_sentences
                    if row.get("source")
                )
            )
        ),
        "sentences_without_recording": sum(1 for c in clips_counts if c == 0),
        "average_clips_per_sentence": (
            round(sum(clips_counts) / len(clips_counts), 2)
            if clips_counts
            else 0
        ),
        "alphabet": sorted(list(set("".join(all_text)))),
        "sample_sentences": random.sample(all_text, k=min(5, len(all_text))),
        "average_sentence_length_tokens": (
            round(total_tokens / len(all_text), 1) if all_text else 0
        ),
        "average_sentence_length_chars": (
            round(total_chars / len(all_text), 1) if all_text else 0
        ),
    }


# --- PROMPT AND API CALL ---


def generate_prompt_for_llm(
    stats: Dict[str, Any],
    sentence_threshold: int,
    avg_clips_threshold: float,
    existing_markdown: Optional[str] = None,
) -> str:
    """
    Constructs a highly specific prompt to guide the Gemini LLM for datasheet
    creation or update.
    """
    logger.info("Generating detailed prompt for the language model...")
    prompt_stats = json.loads(json.dumps(stats, default=lambda o: dict(o)))
    lang_name = stats["language"]["name"]

    if existing_markdown:
        update_instructions = f"""
You are an expert AI assistant that updates datasheets for Mozilla Common Voice.
Your task is to **UPDATE** the provided markdown file with new statistics. You must intelligently merge the new data while preserving manually-written sections.

**Core Task:**
Replace the old, auto-generated statistical sections in the "EXISTING MARKDOWN" with fresh data from the "NEW STATISTICAL DATA" section.
- **Preserve Manual Content:** Sections like 'History', 'Acknowledgements', or detailed, human-written introductions should be kept exactly as they are.
- **Replace Statistical Content:** Sections that are clearly generated from data (like 'Clip & Sentence Statistics', 'Demographic Information', 'Text Corpus', 'Contributor Statistics', etc.) must be completely replaced with newly generated content based on the new data.
- **Follow all formatting and content instructions below** when generating the new sections.

**EXISTING MARKDOWN:**
---
{existing_markdown}
---
"""
    else:
        update_instructions = """
You are an expert AI assistant that creates datasheets for Mozilla Common Voice datasets.
Your task is to generate a comprehensive and accurate markdown file from scratch based on the statistical data provided below. Follow all instructions with extreme precision.
"""

    return f"""
{update_instructions}

**NEW STATISTICAL DATA:**
{json.dumps(prompt_stats, indent=2, ensure_ascii=False)}

**DETAILED INSTRUCTIONS (Apply to new and updated sections):**

**1. Main Title:**
Ensure the title is: `# Mozilla Common Voice: {lang_name} ({stats['language']['code']})`

**2. Language Section:**
If updating, preserve any existing detailed introduction. If creating from scratch, write a brief, encyclopedic introduction for the `{lang_name}` language, including its language family, regions, and speaker count.

**3. Clip & Sentence Statistics Section:**
Generate a section titled `## Clip & Sentence Statistics`. State that the dataset contains **{stats['clip_stats']['validated_hours']} validated hours** of speech from **{sum(stats['contributor_stats'].values())}** unique contributors. Then, create two markdown tables EXACTLY as follows:

First table (Clip Summary):
| Type                | Count | Hours  |
| ------------------- | ----: | -----: |
| Validated Clips     | {stats['clip_stats']['validated_count']:,} |   {stats['clip_stats']['validated_hours']:.2f} |
| Invalidated Clips   | {stats['clip_stats']['invalidated_count']:,} |   {stats['clip_stats']['invalidated_hours']:.2f} |
| **Total Clips**     | {stats['clip_stats']['total_count']:,} |   {stats['clip_stats']['total_hours']:.2f} |

Second table (Sentence Summary):
| Type                  |   Count |
| --------------------- | ------: |
| Validated Sentences   |   {stats['sentence_stats']['validated_count']:,} |
| Invalidated Sentences |     {stats['sentence_stats']['invalidated_count']:,} |
| **Total Sentences**   |     {stats['sentence_stats']['total_count']:,} |

**4. Demographic Information Section:**
Generate a section `## Demographic Information`. Include the sentence: "Demographic information is self-reported by contributors and may not be representative of the entire speaker population."
- Create subsections `### Age` and `### Gender` with tables.
- Create `### Accent` with two tables: the first for raw data, the second titled `#### English Translation of Accents` providing best-effort translations/explanations.

**5. Contributor Statistics Section:**
Generate a section `## Contributor Statistics` with a table showing the distribution of clips per contributor.

**6. Text Corpus Section:**
Generate `## Text Corpus`. Add these bullet points:
- **Total validated sentences:** {stats['sentence_stats']['validated_count']:,}
- **Sentences without a recording yet:** {stats['text_corpus']['sentences_without_recording']:,}
- **Average clips per validated sentence:** {stats['text_corpus']['average_clips_per_sentence']:.2f}
- **Average sentence length (tokens):** {stats['text_corpus']['average_sentence_length_tokens']:.1f}
- **Average sentence length (characters):** {stats['text_corpus']['average_sentence_length_chars']:.1f}
Then create subsections for `### Corpus Sources`, `### Alphabet`, and `### Sample Sentences`.

**7. Community Links Section & Conditional Call to Action:**
Generate `## Community Links`.
- Add a link to the main page: `https://commonvoice.mozilla.org/{stats['language']['code']}`.
- **Conditional Analysis:** If `sentences_without_recording` is less than {sentence_threshold} OR `average_clips_per_sentence` is greater than {avg_clips_threshold}, add a prominent note stating this language is in **dire need of new sentences** to provide variety for voice contributors.

**8. Fun Fact Section:**
Generate `## Fun Fact`. Provide one interesting, non-offensive fun fact about the `{lang_name}` language, and cite the source.

**9. Final Sections:**
- Generate `## Datasheet Authors` credited to 'This datasheet was generated automatically...'. Preserve any existing human authors if updating.
- **Modern Call to Action:** After everything else, add a final, encouraging call to action. Invite readers to help grow the dataset for `{lang_name}` by contributing in four key ways: **Speaking** new clips, **Listening** to and verifying others' recordings, **Writing** new public domain sentences, and **Reviewing** sentences submitted by the community, all on the main Common Voice website.

**10. Formatting Rules (Strictly follow):**
- Maximum line width is 79 characters. Wrap paragraphs.
- Use '$$$' for code blocks, NOT '```'.
- Right-align numbers in tables where appropriate.
"""


def call_gemini_api(prompt: str) -> str:
    """
    Initializes the Gemini client and sends a request to the API.
    """
    if not os.getenv("GEMINI_API_KEY"):
        logger.error("Fatal: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    logger.info("Instantiating the GenAI Client...")
    try:
        client = genai.Client()
        logger.info(
            "Sending request to the Gemini API. This may take a moment..."
        )
        response = client.models.generate_content(
            model="models/gemini-2.5-pro", contents=prompt
        )
        logger.info("Successfully received response from the API.")
        return response.text
    except Exception as e:
        logger.error(
            f"Fatal: An error occurred during the Gemini API call: {e}"
        )
        sys.exit(1)


# --- MAIN EXECUTION ---


def main():
    """
    Main entry point and orchestrator for the datasheet generation script.

    USAGE:
        1. Make sure the 'google-genai' library is installed.
           (pip install -r requirements.txt)
        2. Set your Gemini API key as an environment variable:
           export GEMINI_API_KEY="YOUR_API_KEY_HERE"
        3. Run the script from the command line:
           - To create a new file:
             python generate_datasheet.py --base_path /path/to/language_dir
           - To update an existing file:
             python generate_datasheet.py --base_path /path/to/lang_dir --update_file existing_datasheet.md
    """
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger.info(f"Setting CSV field size limit to {CSV_FIELD_SIZE_LIMIT}")
    csv.field_size_limit(CSV_FIELD_SIZE_LIMIT)

    parser = argparse.ArgumentParser(
        description="Generate or update a datasheet for a Mozilla Common Voice dataset."
    )
    parser.add_argument(
        "--base_path",
        type=Path,
        required=True,
        help="Path to the language directory (e.g., ./cv-corpus-vX/kk)",
    )
    parser.add_argument(
        "--update_file",
        type=Path,
        help="Optional path to an existing markdown datasheet to update.",
    )
    args = parser.parse_args()

    existing_markdown_content = None
    if args.update_file:
        if args.update_file.exists():
            logger.info(
                f"Found existing datasheet to update: {args.update_file}"
            )
            existing_markdown_content = args.update_file.read_text(
                encoding="utf-8"
            )
        else:
            logger.warning(
                f"File to update not found: {args.update_file}. Will create a new file instead."
            )

    base_path = args.base_path
    if not base_path.is_dir():
        logger.error(
            f"Fatal: Provided path '{base_path}' is not a valid directory."
        )
        return

    lang_code = base_path.name
    lang_name_map = {
        "kk": "Kazakh",
        "ky": "Kyrgyz",
        "uz": "Uzbek",
        "az": "Azerbaijani",
        "tg": "Tajik",
        "ru": "Russian",
        "tr": "Turkish",
        "en": "English",
        "nn-NO": "Norwegian Nynorsk",
        "tt": "Tatar",
    }
    lang_name = lang_name_map.get(lang_code, lang_code.upper())
    logger.info(
        f"Starting datasheet generation for language: {lang_name} ({lang_code})"
    )

    validated_clips = read_tsv(base_path / "validated.tsv")
    invalidated_clips = read_tsv(base_path / "invalidated.tsv")
    all_clips_durations = read_tsv(base_path / "clip_durations.tsv")
    validated_sentences = read_tsv(base_path / "validated_sentences.tsv")
    unvalidated_sentences_data = read_tsv(
        base_path / "unvalidated_sentences.tsv"
    )
    durations_map = {
        row["clip"]: int(row["duration[ms]"]) for row in all_clips_durations
    }

    validated_hours = round(get_hours(validated_clips, durations_map), 2)
    invalidated_hours = round(get_hours(invalidated_clips, durations_map), 2)

    stats = {
        "language": {"code": lang_code, "name": lang_name},
        "clip_stats": {
            "total_count": len(all_clips_durations),
            "validated_count": len(validated_clips),
            "invalidated_count": len(invalidated_clips),
            "validated_hours": validated_hours,
            "invalidated_hours": invalidated_hours,
            "total_hours": validated_hours + invalidated_hours,
        },
        "sentence_stats": {
            "validated_count": len(validated_sentences),
            "invalidated_count": len(unvalidated_sentences_data),
            "total_count": len(validated_sentences)
            + len(unvalidated_sentences_data),
        },
        "demographics": get_demographics(validated_clips),
        "contributor_stats": get_contributor_stats(validated_clips),
        "text_corpus": get_text_corpus_stats(
            validated_sentences, validated_clips
        ),
    }

    prompt = generate_prompt_for_llm(
        stats,
        SENTENCE_THRESHOLD,
        AVG_CLIPS_THRESHOLD,
        existing_markdown_content,
    )
    final_markdown = call_gemini_api(prompt)

    print("\n\n" + "=" * 30 + " RESULTS " + "=" * 30)
    print("\n--- PART 1: GATHERED STATISTICS (Data sent to LLM) ---\n")
    stats_for_printing = json.loads(
        json.dumps(stats, default=lambda o: dict(o))
    )
    print(json.dumps(stats_for_printing, indent=2, ensure_ascii=False))
    print("\n\n--- PART 2: FINAL MARKDOWN (Generated by Gemini API) ---\n")
    print(final_markdown)
    print("\n" + "=" * 28 + " END OF SCRIPT " + "=" * 28)


if __name__ == "__main__":
    main()
