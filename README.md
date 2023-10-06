# Converting Matty's Tokenomics Book to eBook

[This tokenomics guide](https://tokenomics-guide.notion.site/tokenomics-guide/Tokenomics-for-Builders-The-Comprehensive-Practitioner-s-Guide-to-Token-b5154feba117415cafd67678355e317b) looks so incredibly comfy, I really wanted to tuck in with it on my Kindle.

This is probably a waste of time since Matty could just export it from Notion as a PDF. But hey, sometimes these little challenges are a fun change of pace.

## What needs to be done

Here's the basic steps:

- [x] Copy the markdown from Notion and paste it in one file
- [x] To make the titles register as chapters, tweak the headings a bit so only chapter titles are h1
- [ ] Save all the images locally and update the image links in the markdown file
- [x] Remove any html such as `<aside>`
- [ ] Convert the final markdown file to `.mobi` and `.epub`
- [ ] Make sure it all looks nice with [Kindle Previewer](https://www.amazon.com/Kindle-Previewer/b?node=21381691011)

I tried to keep the commit history clean so you can see the results of any changes i made.

## Reference

- [The Original Book](https://tokenomics-guide.notion.site/tokenomics-guide/Tokenomics-for-Builders-The-Comprehensive-Practitioner-s-Guide-to-Token-b5154feba117415cafd67678355e317b)
- [Dockerized KindleGen](https://github.com/koenrh/docker-kindlegen)
- [Calibre Download](https://calibre-ebook.com/download_linux)
- [md2mobi](https://github.com/lapwat/md2mobi)
