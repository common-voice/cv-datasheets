import sys
import csv

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

    Parameters
    ----------
    file_name: str
        Metadata tsv filename
    Returns
    -------
    dict:
        Dictionary metadata by modality (scs, sps), by locale with keys english_name,
        native_name, speakers, hours_recorded, hours_validated.

    """
    # modality	code	native_name	english_name	speakers	hours_recorded	hours_validated
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


template_languages = get_template_languages_data(languages_file)
metadata = get_metadata_data(metadata_file)


for modality in metadata:
    for locale in metadata[modality]:
        draft_output_dir = output_dir + "/%s/%s/draft/%s" % (
            modality,
            version,
            template_languages[modality][locale],
        )
        template = open(
            "templates/%s/%s.md" % (modality, template_languages[modality][locale])
        ).read()
        print(locale, metadata[modality][locale])
        english_name = metadata[modality][locale]["english_name"]
        native_name = metadata[modality][locale]["native_name"]
        version_readable = version.split("-")[0]
        if english_name == "" or english_name == "_":
            english_name = "[" + native_name + "]"
        if native_name == "" or native_name == "_":
            native_name = "[" + english_name + "]"
        filled_template = template.replace("{{LOCALE}}", locale)
        filled_template = filled_template.replace("{{VERSION}}", version_readable)
        filled_template = filled_template.replace("{{ENGLISH_NAME}}", english_name)
        filled_template = filled_template.replace("{{NATIVE_NAME}}", native_name)
        filled_template = filled_template.replace(
            "{{SPEAKERS}}", metadata[modality][locale]["speakers"]
        )
        filled_template = filled_template.replace(
            "{{HOURS_RECORDED}}", metadata[modality][locale]["hours_recorded"]
        )
        filled_template = filled_template.replace(
            "{{HOURS_VALIDATED}}", metadata[modality][locale]["hours_validated"]
        )

        output_fd = open(draft_output_dir + "/" + locale + ".md", "w+")
        print(filled_template, file=output_fd)
        output_fd.close()
