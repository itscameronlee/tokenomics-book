import os
import ebooklib
from ebooklib import epub
from markdown2 import markdown

# I had Chat-GPT spit this out. It's a good start. It
# includes two options for creating a .mobi file, I opted
# for the Calibre option. In the end that may be unnecessary
# since Amazon is apparently using the .epub format now.


os.makedirs('../dist', exist_ok=True)

def convert_md_to_html(md_file_path):
    print(md_file_path)
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
        html_content = markdown(md_content)
    return html_content

def create_epub(html_content, epub_file_path):
    book = epub.EpubBook()
    book.set_identifier('id123456')
    book.set_title('Tokenomics Book')
    book.set_language('en')

    content = epub.EpubHtml(title='Content', content=html_content)
    book.add_item(content)

    book.toc = (epub.Link('content.html', 'Content', 'content'), )
    book.spine = ['nav', content]

    epub.write_epub(epub_file_path, book)

def create_mobi_calibre(epub_file_path, mobi_file_path):
    # User must have Calibre installed and ebook-convert accessible from the command line
    command = f'ebook-convert {epub_file_path} {mobi_file_path}'
    os.system(command)

def create_mobi_kindlegen(epub_file_path, mobi_file_path):
    # User must have KindleGen installed and accessible from the command line
    command = f'kindlegen {epub_file_path} -o {os.path.basename(mobi_file_path)}'
    os.system(command)

def main():
    md_file_path = '/workspace/tokenomics-book.md'
    epub_file_path = '../dist/tokenomics-book.epub'
    mobi_file_path = '../dist/tokenomics-book.mobi'

    html_content = convert_md_to_html(md_file_path)
    create_epub(html_content, epub_file_path)

    # Choose one of the following two lines based on the conversion tool you have installed:
    create_mobi_calibre(epub_file_path, mobi_file_path)  # Requires Calibre
    # create_mobi_kindlegen(epub_file_path, mobi_file_path)  # Requires KindleGen

if __name__ == '__main__':
    main()
