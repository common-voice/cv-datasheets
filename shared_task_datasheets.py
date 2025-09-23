import csv
import json
import re

from scripts.datasheet import CVDatasheet, DatasheetSection


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


def read_csv_file(file_name: str, delimiter: str = ",") -> list[list[str]]:
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
        reader = csv.reader(file, delimiter=delimiter)
        # Skipping the header
        next(reader, None)
        data = list(reader)
    return data


def extract_row_data(row: list):
    return {
        "locale": row[0],
        "speakers": row[1],
        "recorded": row[2],
        "transcribed": row[3],
        "validated": row[4],
    }


def add_section(
    ds: CVDatasheet,
    section: DatasheetSection,
    content: str,
    level: int,
):
    section_title = re.sub(
        r"[\[\]]",
        "",
        section.title,
    )
    if section_title in ds._section_map:
        print(f"Section {section_title} already exists. Skipping addition.")
        return
    new_section_md = "#" * level + f" {section_title}\n\n{content}"
    new_section = DatasheetSection(raw_text=new_section_md)
    # Append section
    ds.sections.append(new_section)
    ds._section_map[section_title] = new_section


LOCALE_DATASET_LINKS = read_json_file("mdc_locale_datasets_links.json")
SHARED_TASK_LANGS = read_csv_file("shared_task_langs.csv")
SHARED_TASK_STATS = read_csv_file("shared_task_stats.csv")
DATASHEETS_PATH = "cv-corpus/sps/23.0-2025-09-05/final/{lang}"


def main():
    output_ds = CVDatasheet("## Languages description\n\n### Languages Summary")
    # table = "|Language|Speakers|Recorded|Transcribed|Validated|\n|-|-|-|-|-|\n"
    stats_table = "|Language|Train [hours]|Test [hours]|\n|-|-|-|\n"
    # for row in SHARED_TASK_LANGS:
    #    row_data = extract_row_data(row)
    #    table += f"|{row_data['locale']}|{row_data['speakers']}|{row_data['recorded']}|{row_data['transcribed']}|{row_data['validated']}|\n"

    for row in SHARED_TASK_STATS:
        stats_table += f"|{row[0]}|{float(row[1]):.2f}|{float(row[2]):.2f}|\n"
    tables = "#### Stats\n\n" + stats_table
    output_ds.append_content("Languages Summary", tables)
    for row in SHARED_TASK_LANGS:
        row_data = extract_row_data(row)
        locale = row_data.get("locale")
        try:
            path = DATASHEETS_PATH.format(lang="en")
            with open(f"{path}/{locale}.md", "r") as f:
                datasheet_text = f.read()
        except FileNotFoundError:
            path = DATASHEETS_PATH.format(lang="es")
            with open(f"{path}/{locale}.md", "r") as f:
                datasheet_text = f.read()
        ds = CVDatasheet(datasheet_text)
        section_content = ds.header.content
        if "generated automatically" in section_content or "generada automáticamente":
            section_content = "".join(section_content.split("\n")[-3:])
        datasheet_link = LOCALE_DATASET_LINKS[locale]
        section_content = section_content.replace(
            "This datasheet", f"[This datasheet]({datasheet_link})"
        )
        section_content = section_content.replace(
            "Esta ficha técnica", f"[Esta ficha técnica]({datasheet_link})"
        )
        add_section(output_ds, ds.header, section_content, level=4)
    with open("shared_task_langs.md", "w") as f:
        f.write(output_ds.to_markdown())


if __name__ == "__main__":
    main()
