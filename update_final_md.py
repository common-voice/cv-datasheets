import csv
import pathlib

from scripts.datasheet import CVDatasheet, DatasheetSection

RELEASE_VERSION = "23.0-2025-09-17"
MODALITIES = ["scs", "sps"]
LANG_CODES = ["es", "en"]
DRAFT_MD_FOLDER = "cv-corpus/{modality}/{release_version}/{release_mode}/{lang_code}/"

SECTION_ORDER = {
    "community_links": "get_involved",
    "fields": "posprocessing",
    "funding": "license",
}


def read_markdown_file(file_path: pathlib.Path) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def write_markdown_file(file_path: pathlib.Path, content: str):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def get_localize_section(lang_code: str, section: str) -> str:
    i8n = {
        "es": {
            "gender": "Género",
            "age": "Edad",
            "sample": "Muestra",
            "community_links": "Enlaces comunitarios",
            "license": "Licencia",
            "fields": "Campos",
            "get_involved": "¡Involúcrate!",
            "funding": "Financiamiento",
        },
        "en": {
            "gender": "Gender",
            "age": "Age",
            "sample": "Sample",
            "community_links": "Community links",
            "license": "License",
            "fields": "Fields",
            "get_involved": "Get involved!",
            "funding": "Funding",
        },
    }
    return i8n[lang_code][section]


def replace_content_section(
    draft_ds: CVDatasheet, final_ds: CVDatasheet, section_title: str, lang_code: str
):
    section_title = get_localize_section(lang_code, section_title)
    draft_section = draft_ds._section_map.get(section_title, None)
    final_ds.replace_content(section_title, draft_section.content)


def append_content_section(
    draft_ds: CVDatasheet, final_ds: CVDatasheet, section_title: str, lang_code: str
):
    section_title = get_localize_section(lang_code, section_title)
    draft_section = draft_ds._section_map.get(section_title, None)
    final_ds.append_content(section_title, draft_section.content)


def add_section(
    final_ds: CVDatasheet,
    section_title: str,
    level: int,
    content: str,
    place_after: str,
):
    if section_title in final_ds._section_map:
        print(f"Section {section_title} already exists. Skipping addition.")
        return
    new_section_md = "#" * level + f" {section_title}\n\n{content}"
    new_section = DatasheetSection(raw_text=new_section_md)
    # Find the index to insert after
    sections = final_ds.sections
    insert_index = -1
    for i, sect in enumerate(sections):
        if sect.title == place_after:
            insert_index = i + 1
            break
    if insert_index == -1:
        print(f"Place after section {place_after} not found. Appending to the end.")
        final_ds.sections.append(new_section)
    else:
        final_ds.sections.insert(insert_index, new_section)
    final_ds._section_map[section_title] = new_section
    return new_section


def smart_update_section(
    draft_ds: CVDatasheet, final_ds: CVDatasheet, section_title: str, lang_code: str
):
    localized_section = get_localize_section(lang_code, section_title)
    draft_section = draft_ds._section_map.get(localized_section, None)
    final_section = final_ds._section_map.get(localized_section, None)
    if final_section is None:
        print(f"\t\tNo final section {section_title} found. Creating section")
        final_section = add_section(
            final_ds,
            localized_section,
            level=3,
            content=draft_section.content,
            place_after=get_localize_section(
                lang_code,
                SECTION_ORDER.get(
                    section_title, get_localize_section(lang_code, "license")
                ),
            ),
        )
    final_content = final_section.content.lower()
    if section_title == "community_links" and "pontoon" in final_content:
        # Skip adding pontoon sections
        return
    elif section_title == "funding" and (
        "multingual speech fund" in final_content or "omfs" in final_content
    ):
        # Skip adding founding string
        return

    final_ds.append_content(localized_section, draft_section.content)


def remove_placeholder_content(ds: CVDatasheet, section_title: str, lang_code: str):
    localized_section = get_localize_section(lang_code, section_title)
    section = ds._section_map.get(localized_section, None)
    if section_title == "sample":
        placeholder_texts = [
            "There follows a randomly selected sample of five sentences from the corpus.",
            "A continuación se muestran cinco oraciones seleccionadas aleatoriamente del corpus.",
        ]
        for placeholder in placeholder_texts:
            section.content = section.content.replace(placeholder, "").strip()
        automatic_msg = (
            "*Automatic random samples*"
            if lang_code == "en"
            else "*Muestras automáticas aleatorias*"
        )
        section.content = f"\n{automatic_msg}\n\n" + section.content


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


OMSF_FOUNDING = [row[0] for row in read_tsv_file("metadata/funding.tsv")]


def main():
    for modality in MODALITIES:
        for lang_code in LANG_CODES:
            draft_folder = DRAFT_MD_FOLDER.format(
                modality=modality,
                release_version=RELEASE_VERSION,
                release_mode="draft",
                lang_code=lang_code,
            )
            final_folder = DRAFT_MD_FOLDER.format(
                modality=modality,
                release_version=RELEASE_VERSION,
                release_mode="final",
                lang_code=lang_code,
            )
            print(f"Processing {draft_folder} to {final_folder}")
            # Walk through all markdown files in the draft folder
            draft_path = pathlib.Path(draft_folder)
            for md_file in draft_path.glob("*.md"):
                print(f"Processing {md_file}")
                locale = md_file.parts[-1].split(".")[0]
                md_draft_text = read_markdown_file(md_file)
                draft_datasheet = CVDatasheet(markdown_text=md_draft_text)
                try:
                    md_final_text = read_markdown_file(final_folder + md_file.name)
                except FileNotFoundError:
                    print(
                        f"\t[WARNING]: Final markdown file not found for {md_file.name}. Copying draft to final."
                    )
                    if lang_code == "es":
                        datasheet_msg = "> Esta hoja de datos ha sido generada automáticamente, nos encantaría incluir más información, si deseas ayudar, [¡ponte en contacto con nosotros!]([get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)"
                    else:
                        datasheet_msg = "> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!"
                    new_header_content = (
                        f"{datasheet_msg}\n\n {draft_datasheet.header.content}"
                    )
                    draft_datasheet.header.content = new_header_content
                    # write_markdown_file(
                    #    final_folder + md_file.name,
                    #    draft_datasheet.to_markdown(include_empty_sections=True),
                    # )
                    continue
                final_datasheet = CVDatasheet(markdown_text=md_final_text)
                # update founding only

                if locale in OMSF_FOUNDING:
                    replace_content_section(
                        draft_datasheet, final_datasheet, "funding", lang_code
                    )
                    write_markdown_file(
                        final_folder + md_file.name,
                        final_datasheet.to_markdown(include_empty_sections=True),
                    )
                continue
                print("PASSSSS")
                if modality == "scs":
                    try:
                        replace_content_section(
                            draft_datasheet, final_datasheet, "gender", lang_code
                        )
                    except KeyError:
                        print(
                            f"\t[WARNING]: No gender section found for {md_file.name} Skipping"
                        )
                    try:
                        replace_content_section(
                            draft_datasheet, final_datasheet, "age", lang_code
                        )
                    except KeyError:
                        print(
                            f"\t[WARNING]: No age section found for {md_file.name} Skipping"
                        )
                    try:
                        remove_placeholder_content(draft_datasheet, "sample", lang_code)
                        append_content_section(
                            draft_datasheet, final_datasheet, "sample", lang_code
                        )
                    except KeyError:
                        print(
                            f"\t[WARNING]: No sample section found for {md_file.name} Skipping"
                        )
                    try:
                        smart_update_section(
                            draft_datasheet,
                            final_datasheet,
                            "community_links",
                            lang_code,
                        )
                    except KeyError:
                        print(
                            f"\t[WARNING]: No community_links section found for {md_file.name} Skipping"
                        )

                    # write_markdown_file(
                    #    final_folder + md_file.name,
                    #    final_datasheet.to_markdown(include_empty_sections=True),
                    # )
                elif modality == "sps":
                    print(f"Skipping sps for now. Info {md_file.name}")


if __name__ == "__main__":
    main()
