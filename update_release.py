import os
import sys
from http.client import responses

import requests as r

from scripts.datasheet import CVDatasheet, DatasheetSection

# 24.0-2025-12-05
RELEASE_VERSION = sys.argv[1]
CV_LANG_API = "https://commonvoice.mozilla.org/api/v1/languagedata/{lang}"
METADATA = "https://raw.githubusercontent.com/common-voice/cv-dataset/refs/heads/main/datasets/cv-corpus-{release}.json"

OUTPUT_PATH_BASE = "cv-corpus"
PREV_FINAL_RELEASE_PATH = os.path.join(OUTPUT_PATH_BASE, "scs","23.0-2025-09-05", "final")
TEMPLATE_PATH = "templates/scs/{lang}.md"

AUTOMATIC_MSG = "> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!\n\n"
MISS_ENGLISH_NAMES = {
    "fmp": "Feʼefeʼe",
    "esu": "Central Alaskan Yupʼik"
}

def download_release_metadata() -> dict:
    response = r.get(METADATA.format(release=RELEASE_VERSION))
    response.raise_for_status()
    return response.json()

def read_datasheet(path: str) -> CVDatasheet:
    with open(path, "r") as f:
        template = f.read()
    return CVDatasheet(template)

def get_language_metadata(lang: str) -> dict:
    response = r.get(CV_LANG_API.format(lang=lang))
    response.raise_for_status()
    return response.json()

def make_table(data: dict, header: str) -> str:
    # TODO: localize fields
    table = f"{header}\n"
    for field, freq in data.items():
        if freq != 0:
            # Convert to percent format
            clean_freq = f"{freq * 100:.1f}%" if freq <= 1 else freq
            clean_field = field.title().replace("_", " ") if field else "Undefined"
            table += f"| {clean_field} | {clean_freq} |\n"
    return table

def fill_paragraph(lang: str, ds: CVDatasheet, metadata: dict, template_paragraph: str):
    lang_metadata = get_language_metadata(lang)
    version_readable = RELEASE_VERSION.split("-")[0]
    english_name = lang_metadata.get("english_name", "")
    if not english_name and lang in MISS_ENGLISH_NAMES:
        english_name = MISS_ENGLISH_NAMES.get(lang)

    if not english_name:
        raise Exception("API ERROR")
    template_paragraph = template_paragraph.replace("{{VERSION}}", version_readable)
    template_paragraph = template_paragraph.replace("{{ENGLISH_NAME}}", english_name)
    template_paragraph = template_paragraph.replace("{{LOCALE}}", lang)
    template_paragraph = template_paragraph.replace("{{CLIPS}}", str(metadata.get("clips")))
    template_paragraph = template_paragraph.replace("{{HOURS_RECORDED}}", str(metadata.get("totalHrs")))
    template_paragraph = template_paragraph.replace("{{HOURS_VALIDATED}}", str(metadata.get("validHrs")))
    template_paragraph = template_paragraph.replace("{{SPEAKERS}}", str(metadata.get("users")))
    if "automatically" in ds.header.content:
        # Add automatic generation message
        print(f"\t[INFO] Add automatic generation DS message")
        template_paragraph = AUTOMATIC_MSG + template_paragraph
    ds.header.content = template_paragraph

def fill_demographic_data(
        ds: CVDatasheet,
        template: CVDatasheet,
        scs_demographic_data: dict,
        lang_code: str,
):
    if lang_code == "en":
        demographic_info_title = "Demographic information"
        text_corpus_title = "Text corpus"
        age_section = "Age"
        gender_section = "Gender"
        domains_section = "Text domains"
        age_header = "| Age Band | Percentage |\n|-|-|"
        gender_header = "| Gender | Pertentage |\n|-|-|"
        domain_header = "| Domain | Count |\n|-|-|"
        language_title = "Language"
        data_splits_title = "Data splits for modelling"
        demographic_msg = "The dataset includes the following distribution of age and gender."
        gender_msg = "Self-declared gender information, percentage refers to the number of clips annotated with this gender."
        age_msg = "Self-declared age information, percentage refers to the number of clips annotated with this age band."
    elif lang_code == "es":
        demographic_info_title = "Información demográfica"
        text_corpus_title = "Corpus de texto"
        age_section = "Edad"
        gender_section = "Género"
        domains_section = "Dominios textuales"
        age_header = "| Rango de edad | Porcentaje |\n|-|-|"
        gender_header = "| Género | Porcentaje |\n|-|-|"
        domain_header = "| Dominio | Cuenta |\n|-|-|"
        language_title = "Idioma"
        data_splits_title = "Partición de datos para modelado"
        demographic_msg = "El conjunto de datos incluye la siguiente distribución de edad y género."
        gender_msg = "Información de género autodeclarada, el porcentaje se refiere al número de clips anotados con este género."
        age_msg = "Información de edad autodeclarada, el porcentaje se refiere al número de clips anotados con este rango de edad."
    else:
        return

    # Ensure parent sections exist
    if demographic_info_title not in ds._section_map:
        new_sec = DatasheetSection(raw_text=f"## {demographic_info_title}\n{demographic_msg}")
        ds.add_section(new_sec, relative_to_title=language_title, position="below")

    if gender_section not in ds._section_map:
        new_sec = DatasheetSection(raw_text=f"### {gender_section}\n{gender_msg}")
        ds.add_section(new_sec, relative_to_title=demographic_info_title, position="below")

    if age_section not in ds._section_map:
        new_sec = DatasheetSection(raw_text=f"### {age_section}\n{age_msg}")
        ds.add_section(new_sec, relative_to_title=gender_section, position="below")

    if text_corpus_title not in ds._section_map:
        new_sec = DatasheetSection(raw_text=f"## {text_corpus_title}\n")
        ds.add_section(new_sec, relative_to_title=data_splits_title, position="below")

    if domains_section not in ds._section_map:
        new_sec = DatasheetSection(raw_text=f"### {domains_section}\n")
        ds.add_section(new_sec, relative_to_title=text_corpus_title, position="below")

    # fill age
    age_table = make_table(scs_demographic_data.get("age"), age_header)
    template.append_content(age_section, age_table)
    # replace old final ds data
    ds.replace_content(age_section, template._section_map[age_section].content)

    # Fill gender
    gender_table = make_table(scs_demographic_data.get("gender"), gender_header)
    template.append_content(gender_section, gender_table)
    ds.replace_content(gender_section, template._section_map[gender_section].content)

    # Fill domains
    domain_table = make_table(
        scs_demographic_data.get("sentence_domain"), domain_header
    )
    template.append_content(domains_section, domain_table)
    ds.replace_content(domains_section, template._section_map[domains_section].content)


def main():
    # Create folder sctructure for release for Scripted Release only
    output_path = os.path.join(OUTPUT_PATH_BASE, "scs", RELEASE_VERSION)
    os.makedirs(output_path, exist_ok=True)
    en_folder = os.path.join(PREV_FINAL_RELEASE_PATH, "en")
    es_folder = os.path.join(PREV_FINAL_RELEASE_PATH, "es")
    metadata = download_release_metadata()
    locales = metadata.get("locales")
    total_files = len(locales)

    for i, (lang, data) in enumerate(locales.items(), start=1):
        print(f"#{i}/{total_files} Updating {lang}")

        # Load final from previous release
        lang_file = lang + ".md"
        out_lang_path_en = os.path.join(output_path, "en")
        out_lang_path_es = os.path.join(output_path, "es")
        os.makedirs(out_lang_path_en, exist_ok=True)
        os.makedirs(out_lang_path_es, exist_ok=True)

        final_out_path_en = os.path.join(out_lang_path_en, lang_file)
        final_out_path_es = os.path.join(out_lang_path_es, lang_file)

        if os.path.exists(final_out_path_en) or os.path.exists(final_out_path_es):
            print(f"\t[INFO] {lang} already exists in current release. Skipping.")
            continue

        # Load final from previous release
        final_datasheet = None
        template_lang = None
        template = None

        if lang_file in os.listdir(en_folder):
            final_datasheet = read_datasheet(os.path.join(en_folder, lang_file))
            template_lang = "en"
            template = read_datasheet(TEMPLATE_PATH.format(lang=template_lang))
            final_out_path = final_out_path_en
        elif lang_file in os.listdir(es_folder):
            final_datasheet = read_datasheet(os.path.join(es_folder, lang_file))
            template_lang = "es"
            template = read_datasheet(TEMPLATE_PATH.format(lang=template_lang))
            final_out_path = final_out_path_es
        else:
            # TODO: Create a New Datasheet
            print(f"\t[WARN] {lang} not found in previous release. Skipping.")
            continue

        # Update first paragraph
        fill_paragraph(lang, final_datasheet, data, template.header.content)
        # Update demographic information
        fill_demographic_data(final_datasheet, template, data.get("splits"), template_lang)

        # Save it
        with open(final_out_path, "w+") as out_file:
            out_file.write(final_datasheet.to_markdown(include_empty_sections=True))

if __name__ == "__main__":
    main()
