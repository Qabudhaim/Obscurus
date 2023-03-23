import markdown
from bs4 import BeautifulSoup
import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html, HtmlFormatter
from pygments.styles import get_style_by_name

def markdown_to_html_with_toc(markdown_text):
    # Convert markdown to HTML
    html = markdown.markdown(markdown_text, extensions = ['markdown.extensions.tables', 'markdown.extensions.fenced_code', 'toc'])

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the headings in the HTML
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # Create a table of contents
    toc_html = '<ul>'
    for heading in headings:
        # Get the text and ID of the heading
        heading_text = heading.text.strip()
        heading_id = heading.get('id')

        # Add the heading to the table of contents
        toc_html += f'<li><a href="#{heading_id}">{heading_text}</a></li>'

        # Add the ID to the heading if it doesn't already have one
        if not heading_id:
            heading['id'] = heading_text.replace(' ', '-').lower()

    toc_html += '</ul>'

    # Add the table of contents to the HTML
    soup.insert(0, BeautifulSoup(toc_html, 'html.parser'))

    # Return the modified HTML
    return str(soup)


markdown_text = '''
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

![Alt Text](https://images.unsplash.com/photo-1631378961385-21bee7eb41ad?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=736&q=80 "Optional Title")


```python
print("Hello, world!")
```
'''

html_with_toc = markdown_to_html_with_toc(markdown_text)

lexer = get_lexer_by_name("python", stripall=True)
style = get_style_by_name("one-dark")
formatter = html.HtmlFormatter(style=style)
html_text = html_with_toc.replace("<code>", '<code class="highlight">', 1)
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



from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>Example</title>
</head>
<body>
<p>This is some text.</p>
<code>print("Hello, world!")</code>
<p>This is some more text.</p>
<code>for i in range(10):\n    print(i)</code>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Find all code tags in the HTML
code_tags = soup.find_all('code')

# Print the text content of each code tag
for code_tag in code_tags:
    print(code_tag.text)

print(code_tags)