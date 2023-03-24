from django import template
from markdown import markdown
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name


register = template.Library()

@register.filter
def toc(text):

    html = markdown(text, extensions = ['markdown.extensions.tables', 'markdown.extensions.fenced_code', 'toc'])

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

    return mark_safe(toc_html)


@register.filter
def markdownify(text):

    html = markdown(text, extensions = ['markdown.extensions.tables', 'markdown.extensions.fenced_code', 'toc'])

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    return mark_safe(str(soup))