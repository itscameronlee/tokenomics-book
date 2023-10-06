# Converting Matty's Tokenomics Guide for Kindle

[This tokenomics guide](https://tokenomics-guide.notion.site/tokenomics-guide/Tokenomics-for-Builders-The-Comprehensive-Practitioner-s-Guide-to-Token-b5154feba117415cafd67678355e317b) looks so incredibly comfy, I really wanted to tuck in with it on my Kindle.

This is probably a waste of time since Matty could just export it from Notion as a PDF. But hey, sometimes these little challenges are a fun change of pace.

## What needs to be done

Here's the basic steps:

- [x] Copy the markdown from Notion and paste it in one file
- [x] To make the titles register as chapters, tweak the headings a bit so only chapter titles are h1
- [x] Save all the images locally and update the image links in the markdown file
- [x] Remove any html such as `<aside>`
- [ ] Find a good way to get the tweets in there
- [ ] Add the relevant metadata (author, title, etc)
- [ ] Convert the markdown to `.epub` format
- [x] Convert the doc to `.mobi` format
- [ ] Make sure it all looks nice with [Kindle Previewer](https://www.amazon.com/Kindle-Previewer/b?node=21381691011)

I tried to keep the commit history clean so you can see the results of any changes I made.

## Aaaaand MOBI is being deprecated

I skipped exporting the EPUB and pushed out a test `.mobi` file using Calibre. I sent it via email to my Kindle and got this email from Amazon:

> We wanted to inform you that on November 1 2023, we will start winding down support for sending MOBI (.mobi, .azw, .prc) files through Send to Kindle. [...] MOBI documents already in your Kindle library and other document formats will not be affected by this change.  

>MOBI is an older file format and does not support the latest Kindle features for documents. [...] You can find a list of compatible formats here. EPUB (.epub) is one such compatible format, and you can send it to your library from the Send to Kindle web app.

Looks like I'll need to put in the last bit of work to get this into EPUB format. Hopefully I can do that over the weekend.

## Links for my own reference

- [The Original Book](https://tokenomics-guide.notion.site/tokenomics-guide/Tokenomics-for-Builders-The-Comprehensive-Practitioner-s-Guide-to-Token-b5154feba117415cafd67678355e317b)
- [Dockerized KindleGen](https://github.com/koenrh/docker-kindlegen)
- [Calibre Download](https://calibre-ebook.com/download_linux)
- [md2mobi](https://github.com/lapwat/md2mobi)
