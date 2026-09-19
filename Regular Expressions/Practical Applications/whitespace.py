import re

def clean_text(html):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html)

    # Replace multiple spaces, tabs, and newlines with one space
    text = re.sub(r'\s+', ' ', text)

    # Remove spaces from beginning and end
    return text.strip()


html = """
<p>Hello    World!</p>
<div>This is    a test.</div>

<strong>Python</strong>
"""

print(clean_text(html))