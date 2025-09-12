"""
A very minimal implementation for converting between a datasheet markdown file 
and a Python object. It is capable of parsing markdown sections, extracting 
comments, and converting back to markdown format. It currently doesn't parse 
anything in the section content, but instead treats everything as raw text.

Example usage:

    > datasheet = CVDatasheet(markdown_text=txt)
    > print(datasheet.sections)

    > section_title = datasheet.sections[2].title
    > datasheet.append_content(section_title, "New content")
    > markdown_text = datasheet.to_markdown(include_empty_sections=True)

Note: The "header" section referred to throughout the code is the top-most 
      section of the datasheet 
      e.g. 
      "# *Aragonés* &mdash; Aragonese (`an`)
      This datasheet is for version 23.0 of the the Mozilla Common Voice 
      *Scripted Speech* dataset for Aragonese (`an`)."
"""
import re

class DatasheetSection(object):
    """
    Represents a section of a datasheet, including minimally consists of a 
    title (of any level), and can also contain comments and textual content.
    """

    def __init__(self, raw_text: str = None):
        """
        Initializes a DatasheetSection instance.

        Arguments
        ---------
        raw_text: str, optional 
            The raw text of the section, including title, comments, and content. 
            If provided, the section will be parsed automatically.
        """
        self.title = ""
        self.title_level = ""
        self.comments = []
        self.content = ""

        if raw_text is not None:
            #self.parse_section_text(raw_text.split("\n"))
            self.parse_section_text(re.split("(\n+)", raw_text))
    def __repr__(self):
        return self.title

    def parse_section_text(self, line_list):
        """
        Parses the section text from a list of lines, extracting the title, 
        comments, and content.

        Arguments
        ---------
        line_list: List[str] 
            A list of lines of text in a single section, including comments.

        """
        lines = [line for line in line_list]  # if line.strip()]
        title_line = lines[0]
        match = re.match(r"^#+", title_line)
        deg = len(match.group(0)) if match else 0
        title_text = title_line.replace("#", "").strip()
        
        #
        # extract html-style comments (<!-- ... -->), possibly spanning 
        # multiple lines
        #
        text = "".join(lines[1:])
        
        comment_blocks = [
            m.group(1).strip() for m in 
            re.finditer(r'<!--(.*?)-->', text, re.DOTALL)
        ]

        content = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL).strip()
        self.comments = comment_blocks

        self.title = title_text
        self.title_level = deg
        self.content = content

    def to_markdown(self):
        """
        Converts the DatasheetSection back to markdown format.

        Returns
        -------
        str
            The markdown representation of the section, including title, 
            comments, and content.
        """
        lines = [f"{'#' * self.title_level} {self.title}\n"]
        for comment in self.comments:
            lines.append(f"<!-- {comment} -->\n")
        lines.append(self.content)
        return "".join(lines)

    
class CVDatasheet(object):
    """
    Represents an MDC CommonVoice datasheet parsed from markdown text.
    This class provides methods to parse, manipulate, and export datasheet 
    sections from markdown-formatted text.
    """
    
    def __init__(self, markdown_text: str = None):
        self.header = None
        self._section_map = {}
        self.sections = []
        if markdown_text is not None:
            self.parse_markdown(markdown_text)

    def parse_markdown(self, markdown_text: str):
        """
        Parses markdown text into datasheet sections. The sections
        are added to the section and _section_map attributes.

        Arguments
        ---------
        markdown_text: str 
            Markdown-formatted datasheet text.

        >>> ds = CVDatasheet()
        >>> ds.parse_markdown("# Header\\nIntro\\n# Section\\nContent")
        >>> ds.header.title
        'Header'
        >>> ds.sections[0].title
        'Section'
        """
        current_section = []
        
        for line in markdown_text.split("\n"):
            if line.startswith("#"):
                if current_section:
                    current_ds_sect = DatasheetSection(
                        raw_text="\n".join(current_section)
                    )
                    if self.header is None:
                        self.header = current_ds_sect
                    else:
                        self._section_map[current_ds_sect.title] = current_ds_sect
                        self.sections.append(current_ds_sect)

                    current_section = [line]
                    continue
            
            current_section.append(line)

        current_ds_sect = DatasheetSection(raw_text="\n".join(current_section))
        if self.header is None:
            self.header = current_ds_sect
        else:
            self.sections.append(current_ds_sect)
            self._section_map[current_ds_sect.title] = current_ds_sect

    def replace_content(self, title, new_content):
        """
        Replaces the content of a section, uising the section 
        title as the key.

        Arguments
        ---------
        title: str
            The title of the section to replace.
        new_content: str 
            The new content for the section.

        >>> ds = CVDatasheet("# Header\\nIntro\\n# Section\\nOld Content")
        >>> ds.replace_content("Section", "New Content")
        >>> ds._section_map["Section"].content
        'New Content'
        """
        self._section_map[title].content = new_content

    def append_content(self, title, additional_content):
        """
        Appends text to a section, using the section title as
        the key.

        Arguments
        ---------
        title: str 
            The title of the section to append to.

        additional_content: str 
            The content to append.

        >>> ds = CVDatasheet("# Header\\nIntro\\n# Section\\nA")
        >>> ds.append_content("Section", "B")
        >>> ds._section_map["Section"].content
        'A\\nB'
        """
        self._section_map[title].content += "\n" + additional_content

    def prepend_content(self, title, additional_content):
        """
        Prepends text content to a section, using the section title as
        the key.

        Arguments
        ----------
        title: str 
            The title of the section to prepend to.
        
        additional_content: str 
            The content to prepend.
        
        >>> ds = CVDatasheet("# Header\\nIntro\\n# Section\\nA")
        >>> ds.prepend_content("Section", "B")
        >>> ds._section_map["Section"].content
        'B\\nA'
        """
        self._section_map[title].content = (
            additional_content + "\n" + self._section_map[title].content
        )

    def to_markdown(self, include_empty_sections=False):
        """
        Converts the datasheet back to markdown format.

        Arguments
        ---------
        include_empty_sections: bool 
            Whether to include sections with empty content.
        
        Returns
        -------
        str
            The datasheet as markdown-formatted text.

        >>> ds = CVDatasheet("# Header\\nIntro\\n## Section\\n\\nThis is test\\nYes\\n\\n## End Section\\nContent")
        >>> print(ds.to_markdown())
        # Header
        Intro
        <BLANKLINE>
        ## Section
        This is a test
        Yes
        <BLANKLINE>
        ## End Section
        Content
        """
        sections = (
            [self.header if self.header is not None else ""] + self.sections
        )
        return "\n\n".join(
            [section.to_markdown() for section in sections 
            if section.content or include_empty_sections]
        )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
