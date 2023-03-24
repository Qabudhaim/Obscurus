import markdown
from bs4 import BeautifulSoup
import markupsafe

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html, HtmlFormatter
from pygments.styles import get_style_by_name

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
html_text = markdown.markdown(markdown_text, extensions = ['markdown.extensions.tables', 'markdown.extensions.fenced_code', 'toc'])

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_text, 'html.parser')

headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

toc = '<ul>'
for heading in headings:
    toc += '<li><a href="#{}">{}</a></li>'.format(heading.get('id'), heading.text)
toc += '</ul>'


code_blocks = soup.find_all('code')


for code_block in code_blocks:
    # Get the code and language
    code = code_block.get_text()
    language = code_block.get('class')
    language = language[0].replace('language-', "")

    lexer = get_lexer_by_name(language, stripall=True)
    style = get_style_by_name("one-dark")
    formatter = html.HtmlFormatter(style=style)
    highlighted_code = highlight(code, lexer, formatter)
    pygments_css=formatter.get_style_defs('.highlight')
    
    with open("one-dark.css", "w") as f:
        f.write(pygments_css)

    new_code_block = soup.new_tag('code')
    new_code_block.string = markupsafe.Markup(highlighted_code)
    code_block.replace_with(new_code_block)
    
    print(new_code_block)
    

    print("**")


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
""".format(content=str(soup))

# how to replace a block of code in html file with another using bs4
with open('output.html', 'w') as f:
    f.write(html_output)


