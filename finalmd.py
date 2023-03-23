import markdown
from bs4 import BeautifulSoup
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

markdown_text = '''
# My no

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

# Convert the markdown to HTML
html = markdown.markdown(markdown_text, extensions = ['markdown.extensions.tables', 'markdown.extensions.fenced_code', 'toc'])

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all the headings in the HTML
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Create a table of contents
toc = '<ul>'
for heading in headings:
    toc += '<li><a href="#{}">{}</a></li>'.format(heading.get('id'), heading.text)
toc += '</ul>'

# Find all the code blocks in the HTML
code_blocks = soup.find_all('code')

# Highlight the code blocks with Pygments
for code_block in code_blocks:
    # Get the code and language
    code = code_block.text
    language = code_block.get('class')[0] if code_block.has_attr('class') else None

    language = 'python'

    # Get the lexer for the language
    lexer = get_lexer_by_name(language) if language else None

    # Highlight the code
    if lexer:
        highlighted_code = highlight(code, lexer, HtmlFormatter(style='one-dark'))
    else:
        highlighted_code = '<pre><code>{}</code></pre>'.format(code)

    # Replace the code block with the highlighted code
    code_block.replace_with(highlighted_code)

# Add the table of contents to the HTML
html = toc + html

# Write the HTML to a file
with open('output.html', 'w') as f:
    f.write(html)
