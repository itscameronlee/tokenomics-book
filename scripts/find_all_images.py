import re


# A simple script to locate and print all the images
# in the book. This should make it easier to manually
# replace them in the markdown text


with open('../tokenomics-book.md', 'r') as f:
    markdown_text = f.read()

# This regex fails on alt text that includes newlines
imgs = re.findall(r'^(!.*)', markdown_text, re.MULTILINE)

for img in imgs:
    print(f"{img}\n")
