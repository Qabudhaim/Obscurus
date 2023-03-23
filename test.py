import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html, HtmlFormatter
from pygments.styles import get_style_by_name

# The markdown text you want to convert
markdown_text = """
# My Document

[[toc]]

## Introduction

This is the introduction section.

## Overview

This is the overview section.

### Subsection

This is a subsection.

## Conclusion

This is the conclusion section.
Some **bold** and _italic_ text.

```python
print("Hello, world!")
```
"""

html_text = markdown.markdown(markdown_text, extensions=['toc'])
# print(html_text)

lexer = get_lexer_by_name("python", stripall=True)
style = get_style_by_name("one-dark")
formatter = html.HtmlFormatter(style=style)
html_text = html_text.replace("<code>", '<code class="highlight">', 1)
highlighted_code = highlight(html_text, lexer, formatter)


html_output = """
<!DOCTYPE html>
<html>
<head>
  <title>My Markdown Document</title>
  <link rel="stylesheet" href="one-dark.css">
</head>
<body>
  {content}
</body>
</html>
""".format(content=highlighted_code)

pygments_css=formatter.get_style_defs('.highlight')

with open("one-dark.css", "w") as f:
    f.write(pygments_css)

with open("output.html", "w") as f:
    f.write(html_output)

# from pygments.styles import get_all_styles

# styles = list(get_all_styles())
# print(styles)


import markdown
from markdown.extensions.toc import TocExtension

# Define the Markdown content
md_content = """

[[TOC]]

# My Document

## Introduction

This is the introduction section.

## Overview

This is the overview section.

### Subsection

This is a subsection.

## Tables

| Column 1 Header | Column 2 Header |
|-----------------|------------------|
| Row 1 Column 1  | Row 1 Column 2   |
| Row 2 Column 1  | Row 2 Column 2   |

## Images

![Alt Text](/path/to/image.jpg "Optional Title")

"""

# Define the extensions including TocExtension, tables, and fenced_code
extensions = ['markdown.extensions.tables', 'markdown.extensions.fenced_code', TocExtension()]

# Convert the Markdown to HTML with the table of contents
html_content = markdown.markdown(md_content, extensions=extensions)


# Define the extensions including tables and fenced_code
extensions = ['toc', 'markdown.extensions.tables', 'markdown.extensions.fenced_code']

# Convert the Markdown to HTML with the table of contents
html_content = markdown.markdown(md_content, extensions=extensions)

# Print the HTML output with the table of contents
print(html_content)

html_output = """
<!DOCTYPE html>
<html>
<head>
  <title>My Markdown Document</title>
  <link rel="stylesheet" href="one-dark.css">
</head>
<body>
  {content}
</body>
</html>
""".format(content=html_content)

pygments_css=formatter.get_style_defs('.highlight')

with open("one-dark.css", "w") as f:
    f.write(pygments_css)

with open("output.html", "w") as f:
    f.write(html_output)
