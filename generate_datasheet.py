import sys
import csv
import json

from scripts.datasheet import CVDatasheet


# TODO: Think how to manage localization correctly

# global path variables
TEMPLATE_PATH = "templates/{modality}/{lang_code}.md"
DRAFT_OUTPUT_PATH = (
    "{output_dir}/{modality}/{version}/draft/{template_lang}/{locale}.md"
)
ORIGINAL_PR_DATA_PATH = "metadata/language-requests.tsv"
# Non public data
SPS_STATS_PATH = "metadata/sps-stats.json"
# Non public data
SCS_DEMOGRAPHIC_PATH = "metadata/cv-corpus-23.0-2025-09-05.json"
# Extracted using scripts/fetch_scs_sentences.py
SCS_SENTENCES_PATH = "metadata/scs-sentences.json"

# Global constants URL
PONTOON_URL = "https://pontoon.mozilla.org/{locale}/common-voice/contributors/"
COMMON_VOICE_URL = "https://commonvoice.mozilla.org"
COMMON_VOICE_PR_URL = "https://github.com/common-voice/common-voice/issues/{issue}"

metadata_file = sys.argv[1]
languages_file = sys.argv[2]
version = sys.argv[3]
output_dir = sys.argv[4]


def read_tsv_file(file_name: str) -> list[list[str]]:
    """Read a tsv file

    Parameters
    ----------
    file_name: str
        File name

    Return
    ------
    list:
        List with lists where each list is a row and each internal list
        has strings
    """
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file, delimiter="\t")
        # Skipping the header
        next(reader, None)
        data = list(reader)
    return data


def read_json_file(file_name: str) -> dict:
    """Read json file from dist

    Parameters
    ----------
    file_name : str
        File name

    Returns
    -------
    dict
        json data as python dict
    """
    with open(file_name, "r") as f:
        data = json.load(f)
    return data


def get_template_languages_data(file_name: str) -> dict:
    """Parse tsv languages file to dictionary

    Parameters
    ----------
    file_name: str
        Template languages tsv filename

    Returns
    -------
    dict:
        Dictionary with languages data by modality (scs, sps)
        with locale as key and language as value
    """
    data = {"scs": {}, "sps": {}}
    for line in read_tsv_file(file_name):
        modality, locale, template_language = line
        data[modality][locale] = template_language
    return data


def get_metadata_data(file_name: str) -> dict:
    """Parse metadata tsv file to dictionary

    Each row has (in this order) the next structure:
    modality\tcode\tnative_name\tenglish_name\tspeakers\thours_recorded\thours_validated

    Parameters
    ----------
    file_name: str
        Metadata tsv filename
    Returns
    -------
    dict:
        Dictionary metadata by modality (scs, sps), by locale (lang code) with keys english_name,
        native_name, speakers, hours_recorded, hours_validated.
        Example:
    'tar': {
        'english_name': 'Central Tarahumara',
        'native_name': '_',
        'speakers': '17',
        'hours_recorded': '11',
        'hours_validated': '10'
    }

    """
    data = {"scs": {}, "sps": {}}

    for line in read_tsv_file(file_name):
        (
            modality,
            locale,
            native_name,
            english_name,
            speakers,
            hours_recorded,
            hours_validated,
        ) = line
        if locale not in data[modality]:
            data[modality][locale] = {}
        data[modality][locale]["english_name"] = english_name
        data[modality][locale]["native_name"] = native_name
        data[modality][locale]["speakers"] = speakers
        data[modality][locale]["hours_recorded"] = hours_recorded
        data[modality][locale]["hours_validated"] = hours_validated
    return data


def fill_template_header(
    template: CVDatasheet, locale: str, modality: str, metadata: dict
) -> None:
    """Fill header template

    Add information about language name, native name, locale, speakers count,
    hours validated, hours recorded and version

    Parameters
    ----------
    template: CVDatasheet
        Template as CVDatasheet object
    locale: str
        Common Voice language code
    modality: str
        Code for spontaneous and scripted mode
    metadata: dict
        Language metadata for fill the information

    Returns
    -------
    None:
        Information is filled in the object
    """
    english_name = metadata[modality][locale]["english_name"]
    native_name = metadata[modality][locale]["native_name"]
    version_readable = version.split("-")[0]
    if english_name == "" or english_name == "_":
        english_name = "[" + native_name + "]"
    if native_name == "" or native_name == "_":
        native_name = "[" + english_name + "]"

    # Fill title info
    header_title = template.header.title

    filled_title = header_title.replace("{{LOCALE}}", locale)
    filled_title = filled_title.replace("{{ENGLISH_NAME}}", english_name)
    filled_title = filled_title.replace("{{NATIVE_NAME}}", native_name)
    # Update title
    template.header.title = filled_title

    # Fill header content
    hours_recorded = metadata[modality][locale]["hours_recorded"]
    hours_validated = metadata[modality][locale]["hours_validated"]
    speakers = metadata[modality][locale]["speakers"]
    clips = str(metadata[modality][locale]["clips"])
    header_content = template.header.content

    filled_header_content = header_content.replace("{{VERSION}}", version_readable)
    filled_header_content = filled_header_content.replace(
        "{{ENGLISH_NAME}}", english_name
    )
    filled_header_content = filled_header_content.replace("{{CLIPS}}", clips)
    filled_header_content = filled_header_content.replace("{{LOCALE}}", locale)
    filled_header_content = filled_header_content.replace(
        "{{HOURS_RECORDED}}", hours_recorded
    )
    filled_header_content = filled_header_content.replace(
        "{{HOURS_VALIDATED}}", hours_validated
    )
    filled_header_content = filled_header_content.replace("{{SPEAKERS}}", speakers)
    # Update header content
    template.header.content = filled_header_content


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


def fill_community_links(
    template: CVDatasheet, locale: str, modality: str, lang_code: str
) -> None:
    if lang_code == "es":
        section = "Enlaces comunitarios"
        url_issue_desc = "Petición original para la lengua en GitHub"
        url_pontoon_desc = "Traductores de Common Voice en Pontoon"
    elif lang_code == "en":
        section = "Community links"
        url_issue_desc = "Original language request on GitHub"
        url_pontoon_desc = "Common Voice translators on Pontoon"

    # TODO: Original issue will be periodically fetched from github?
    original_pr_data = read_tsv_file(ORIGINAL_PR_DATA_PATH)
    pontoon_url = PONTOON_URL.format(locale=locale)
    content = f"* [{url_pontoon_desc}]({pontoon_url})\n"
    issue_url = ""
    # FIXME: Do this better
    for row in original_pr_data:
        c_locale, c_modality, issue_number = row
        if c_locale == locale and modality == c_modality:
            issue_url = COMMON_VOICE_PR_URL.format(issue=issue_number)
            break
    if issue_url:
        content += f"* [{url_issue_desc}]({issue_url})"
    template.append_content(section, content)


def fill_sps_stats(template: CVDatasheet, data: dict, lang_code: str):
    stats_section = "Transcripciones" if lang_code == "es" else "Transcriptions"

    # TODO: Localize stats strings
    stats_content = f"* Prompts: `{data.get('prompts', 0)}`\n"
    stats_content += f"* Clips: `{data.get('clips', 0)}`\n"
    stats_content += f"* Duration: `{data.get('duration')}[ms]`\n"
    stats_content += f"* Avg. Transcription Len: `{data.get('avgTranscriptLen')}`\n"
    stats_content += f"* Avg. Duration: `{data.get('avgDurationSecs')}[s]`\n"
    stats_content += f"* Valid Duration: `{data.get('validDurationSecs')}[s]`\n"
    stats_content += f"* Total hours: `{data.get('totalHrs')}[h]`\n"
    stats_content += f"* Valid hours: `{data.get('validHrs')}[h]`\n"
    template.append_content(stats_section, stats_content)


def fill_sps_samples(template: CVDatasheet, data: dict, lang_code: str):
    if lang_code == "en":
        q_section = "Questions"
        r_section = "Responses"
    elif lang_code == "es":
        q_section = "Preguntas"
        r_section = "Respuestas"

    prompts = data.get("randomPrompts")
    if prompts and set(prompts) != {""}:
        promts_content = f"\n```\n{'\n'.join(prompts)}\n```\n"
        template.append_content(q_section, promts_content)

    answers = data.get("randomTranscripts")
    if answers and set(answers) != {""}:
        answers_content = f"\n```\n{'\n'.join(answers)}\n```\n"
        template.append_content(r_section, answers_content)


def make_table(data: dict, header: str) -> str:
    # TODO: localize fields
    table = f"{header}\n"
    for field, freq in data.items():
        if freq != 0:
            clean_field = field.title().replace("_", " ") if field else "Undefined"
            table += f"| {clean_field} | {freq} |\n"
    return table


def fill_demographic_data(
    template: CVDatasheet,
    scs_demographic_data: dict,
    lang_code: str,
):
    if lang_code == "en":
        age_section = "Age"
        gender_section = "Gender"
        domains_section = "Text domains"
        age_header = "| Age Band | Frequency |\n|-|-|"
        gender_header = "| Gender | Frequency |\n|-|-|"
        domain_header = "| Domain | Count |\n|-|-|"
    elif lang_code == "es":
        age_section = "Edad"
        gender_section = "Género"
        domains_section = "Dominios textuales"
        age_header = "| Rango de edad | Frecuencia |\n|-|-|"
        gender_header = "| Género | Frecuencia |\n|-|-|"
        domain_header = "| Dominio | Cuenta |\n|-|-|"

    # fill age
    age_table = make_table(scs_demographic_data.get("age"), age_header)
    template.append_content(age_section, age_table)

    # Fill gender
    gender_table = make_table(scs_demographic_data.get("gender"), gender_header)
    template.append_content(gender_section, gender_table)

    # Fill domains
    domain_table = make_table(
        scs_demographic_data.get("sentence_domain"), domain_header
    )
    template.append_content(domains_section, domain_table)


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


def fill_scs_samples(template: CVDatasheet, data: list[str], lang_code: str):
    samples_section = "Muestra" if lang_code == "es" else "Sample"
    samples_content = f"\n```\n{'\n'.join(data)}\n```\n"
    template.append_content(samples_section, samples_content)


template_languages = get_template_languages_data(languages_file)
metadata = get_metadata_data(metadata_file)
# TODO: By now only for scripted dataheets
demographic_data = read_json_file(SCS_DEMOGRAPHIC_PATH).get("locales")
sps_stats_data = read_json_file(SPS_STATS_PATH)
scs_sentences = read_json_file(SCS_SENTENCES_PATH)

for modality in metadata:
    for locale in metadata[modality]:
        lang_code = template_languages[modality][locale]
        # Reading md template
        template_path = TEMPLATE_PATH.format(modality=modality, lang_code=lang_code)
        with open(template_path, "r") as template_file:
            template = template_file.read()
        ds = CVDatasheet(template)
        fill_community_links(ds, locale, modality, lang_code)
        if modality == "scs":
            # Cotribute links with locale only for scripted mode
            fill_contribute_links(ds, locale, lang_code)
            data = demographic_data.get(locale)
            if data:
                fill_demographic_data(ds, data.get("splits"), lang_code)
                fill_scs_stats(ds, data, lang_code)
            sentences = scs_sentences.get(locale)
            fill_scs_samples(ds, sentences, lang_code)
            clips = data.get("clips", 0)
        elif modality == "sps":
            stats = sps_stats_data.get(locale)
            if stats:
                fill_sps_samples(ds, stats, lang_code)
                fill_sps_stats(ds, stats, lang_code)
                clips = stats.get("clips", 0)
            else:
                # english case
                clips = 0
        metadata[modality][locale]["clips"] = clips
        fill_template_header(ds, locale, modality, metadata)
        # Text stats empty for scs
        draft_output_path = DRAFT_OUTPUT_PATH.format(
            output_dir=output_dir,
            modality=modality,
            version=version,
            template_lang=template_languages[modality][locale],
            locale=locale,
        )
        with open(draft_output_path, "w+") as out_file:
            out_file.write(ds.to_markdown(include_empty_sections=True))
