import markdown
from bs4 import BeautifulSoup

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

markdown_text = '''
# My no

## Introduction

This is the introduction section.

```python
print("Hello, world!")
```

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

```javascript

console.log("Hello, world!")
```

'''

# Convert the markdown to HTML
html = markdown.markdown(markdown_text, extensions = ['markdown.extensions.tables', 'markdown.extensions.fenced_code', 'toc'])

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

toc = '<ul>'
for heading in headings:
    toc += '<li><a href="#{}">{}</a></li>'.format(heading.get('id'), heading.text)
toc += '</ul>'

print(toc)

code_blocks = soup.find_all('code')

print(code_blocks)

for code_block in code_blocks:
    # Get the code and language
    code = code_block.get_text()
    language = code_block.get('class')
    language = language[0].replace('language-', "")

    lexer = get_lexer_by_name(language, stripall=True)

    highlighted_code = highlight(code, lexer, HtmlFormatter())

    new_code_block = soup.new_tag('code')
    new_code_block.string = highlighted_code
    code_block.replace_with(new_code_block)

print(str(soup))

# how to replace a block of code in html file with another using bs4
with open('output.html', 'w') as f:
    f.write(str(soup))

"""
lexer = get_lexer_by_name("python", stripall=True) # done
style = get_style_by_name("one-dark") # defined in django
formatter = html.HtmlFormatter(style=style)
html_text = html_text.replace("<code>", '<code class="highlight">', 1)
highlighted_code = highlight(html_text, lexer, formatter)

pygments_css=formatter.get_style_defs('.highlight')

with open("one-dark.css", "w") as f:
    f.write(pygments_css)
"""
