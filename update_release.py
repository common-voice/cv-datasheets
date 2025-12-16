import os
import sys
from http.client import responses
from idlelib.pyshell import use_subprocess

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
# Some languages on CV API doesn't have english name
MISS_ENGLISH_NAMES = {
    "fmp": "Feʼefeʼe",
    "esu": "Central Alaskan Yupʼik"
}

PONTOON_URL = "https://pontoon.mozilla.org/{locale}/common-voice/contributors/"
COMMON_VOICE_URL = "https://commonvoice.mozilla.org"
COMMON_VOICE_PR_URL = "https://github.com/common-voice/common-voice/issues/{issue}"

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

def fill_header(lang: str, ds: CVDatasheet, metadata: dict, template_paragraph: str, update_title=False):
    lang_metadata = get_language_metadata(lang)
    native_name = lang_metadata.get("native_name", "_")
    version_readable = RELEASE_VERSION.split("-")[0]
    english_name = lang_metadata.get("english_name", "")
    if not english_name and lang in MISS_ENGLISH_NAMES:
        english_name = MISS_ENGLISH_NAMES.get(lang)

    if not english_name:
        raise Exception("API ERROR")

    if update_title:
        header_title = ds.header.title
        filled_title = header_title.replace("{{LOCALE}}", lang)
        filled_title = filled_title.replace("{{ENGLISH_NAME}}", english_name)
        filled_title = filled_title.replace("{{NATIVE_NAME}}", native_name)
        ds.header.title = filled_title

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


def fill_community_links(
        template: CVDatasheet, locale: str, lang_code: str
) -> None:
    if lang_code == "es":
        section = "Enlaces comunitarios"
        url_issue_desc = "Petición original para la lengua en GitHub"
        url_pontoon_desc = "Traductores de Common Voice en Pontoon"
    elif lang_code == "en":
        section = "Community links"
        url_issue_desc = "Original language request on GitHub"
        url_pontoon_desc = "Common Voice translators on Pontoon"

    if locale == "lzz":
        issue_url = "https://github.com/common-voice/common-voice/issues/4179"
    elif locale == "dsb":
        issue_url = "https://github.com/common-voice/common-voice/issues/4520"

    pontoon_url = PONTOON_URL.format(locale=locale)
    content = f"* [{url_pontoon_desc}]({pontoon_url})\n"
    content += f"* [{url_issue_desc}]({issue_url})"
    template.append_content(section, content)


def fill_contribute_links(template: CVDatasheet, locale: str, lang_code: str) -> None:
    if lang_code == "en":
        contribute_links = [
            f"* [Speak]({COMMON_VOICE_URL}/{locale}/speak)",
            f"* [Write]({COMMON_VOICE_URL}/{locale}/write)",
            f"* [Listen]({COMMON_VOICE_URL}/{locale}/listen)",
            f"* [Review]({COMMON_VOICE_URL}/{locale}/review)",
        ]
        section = "Contribute"
    elif lang_code == "es":
        section = "Contribuir"
        contribute_links = [
            f"* [Hablar]({COMMON_VOICE_URL}/{locale}/speak)",
            f"* [Escribir]({COMMON_VOICE_URL}/{locale}/write)",
            f"* [Escuchar]({COMMON_VOICE_URL}/{locale}/listen)",
            f"* [Revisar]({COMMON_VOICE_URL}/{locale}/review)",
        ]
    template.append_content(section, "\n".join(contribute_links))


def fill_scs_stats(template: CVDatasheet, data: dict, lang_code: str):
    if lang_code == "es":
        stats_section = "Corpus de texto"
        stats_template = "El corpus textual contiene `{total_sents}` oraciones, de las cuales `{validated_sents}` están validadas, `{unvalidated_sents}` están invalidadas y `{reported_sents}` son reportadas."
    elif lang_code == "en":
        stats_section = "Text corpus"
        stats_template = "The text corpus contains `{total_sents}` sentences, of which `{validated_sents}` are validated, `{unvalidated_sents}` are invalidated and `{reported_sents}` are reported."

    validated_sents = data.get("validatedSentences")
    unvalidated_sents = data.get("unvalidatedSentences")
    total_sents = validated_sents + unvalidated_sents
    reported_sents = data.get("reportedSentences")

    stats_content = stats_template.format(
        total_sents=total_sents,
        validated_sents=validated_sents,
        unvalidated_sents=unvalidated_sents,
        reported_sents=reported_sents,
    )

    template.append_content(stats_section, stats_content)

def fill_data_splits(
        template: CVDatasheet, data: dict, modality: str, lang_code: str
) -> None:
    data_splits_content = ""

    if lang_code == "es":
        data_splits_section = "Partición de datos para modelado"
        table_header = "| Partición | Cuenta |\n|-|-|"
        if modality == "scs":
            data_splits_template = "Las particiones de datos oficiales para el modelado de esta lengua son las siguientes. De los clips validados, {percent:.2f}% están incluidos en las particiones."
    elif lang_code == "en":
        data_splits_section = "Data splits for modelling"
        table_header = "| Split | Count |\n|-|-|"
        if modality == "scs":
            data_splits_template = "The official data splits for modelling this language are as follows. Of the validated clips, {percent:.2f}% are included in the splits."

    dev = data.get("dev")
    train = data.get("train")
    test = data.get("test")
    if modality == "scs":
        validated = data.get("validated")
        percent = (test + dev + train) / validated * 100 if validated > 0 else 0
        data_splits_content += data_splits_template.format(percent=percent)

    table = make_table({"train": train, "test": test, "dev": dev}, table_header)
    data_splits_content += f"\n\n {table}"
    template.append_content(data_splits_section, data_splits_content)


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
            print(f"\t[WARN] {lang} not found in previous release. Creating new")
            # Create a New Datasheet
            # Read template
            template_lang = "en"
            template = read_datasheet(TEMPLATE_PATH.format(lang=template_lang))
            fill_community_links(template, lang, template_lang)
            fill_contribute_links(template, lang, template_lang)
            fill_demographic_data(template, template, data.get("splits"), template_lang)
            fill_scs_stats(template, data, template_lang)
            fill_data_splits(template, data.get("buckets"), "scs", template_lang)
            fill_header(lang, template, data, template.header.content, update_title=True)
            with open(final_out_path_en, "w+") as  out_file:
                out_file.write(template.to_markdown(include_empty_sections=True))
            continue

        # Update first paragraph
        fill_header(lang, final_datasheet, data, template.header.content)
        # Update demographic information
        fill_demographic_data(final_datasheet, template, data.get("splits"), template_lang)


        # Save it
        with open(final_out_path, "w+") as out_file:
            out_file.write(final_datasheet.to_markdown(include_empty_sections=True))

if __name__ == "__main__":
    main()
