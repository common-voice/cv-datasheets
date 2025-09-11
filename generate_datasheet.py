import sys
import csv
from scripts.datasheet import CVDatasheet


# global path variables
TEMPLATE_PATH = "templates/{modality}/{lang_code}.md"
DRAFT_OUTPUT_PATH = (
    "{output_dir}/{modality}/{version}/draft/{template_lang}/{locale}.md"
)
ORIGINAL_PR_DATA_PATH = "metadata/language-requests.tsv"
COMMON_VOICE_URL = "https://commonvoice.mozilla.org"


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
    header_content = template.header.content

    filled_header_content = header_content.replace("{{VERSION}}", version_readable)
    filled_header_content = filled_header_content.replace(
        "{{ENGLISH_NAME}}", english_name
    )
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
    contribute_links = [
        f"* {COMMON_VOICE_URL}/{locale}/speak",
        f"* {COMMON_VOICE_URL}/{locale}/write",
        f"* {COMMON_VOICE_URL}/{locale}/listen",
        f"* {COMMON_VOICE_URL}/{locale}/review",
    ]
    # TODO: Think how to manage this correctly
    if lang_code == "en":
        section = "Contribute"
    elif lang_code == "es":
        section = "Contribuir"
    elif lang_code == "zh-TW":
        section = "貢獻"
    template.append_content(section, "\n".join(contribute_links))


def fill_community_links(template: CVDatasheet, locale: str, lang_code: str) -> None:
    # TODO: Original PR will be periodically fetched from github
    original_pr_data = read_tsv_file(ORIGINAL_PR_DATA_PATH)


template_languages = get_template_languages_data(languages_file)
metadata = get_metadata_data(metadata_file)

for modality in metadata:
    for locale in metadata[modality]:
        lang_code = template_languages[modality][locale]
        # Reading md template
        template_path = TEMPLATE_PATH.format(modality=modality, lang_code=lang_code)
        with open(template_path, "r") as template_file:
            template = template_file.read()
        ds = CVDatasheet(template)
        fill_template_header(ds, locale, modality, metadata)
        fill_contribute_links(ds, locale, lang_code)
        draft_output_path = DRAFT_OUTPUT_PATH.format(
            output_dir=output_dir,
            modality=modality,
            version=version,
            template_lang=template_languages[modality][locale],
            locale=locale + "_new",
        )
        with open(draft_output_path, "w+") as out_file:
            out_file.write(ds.to_markdown(include_empty_sections=True))
