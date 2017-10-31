###########
# Created by Jizhizi Li @ 31/10/2017
# A shell file to help run 
#
# Input: iconicSpider.py and iconicDownloader.py
# Output: two folder: ~image and ~text to store resultes
###########

#!/bin/bash
rm -rf iconic.json
rm -r text
rm -r image
echo '--------LETS ROCK--------'
echo '......Crawling the website ICONIC.......'
scrapy runspider iconicSpider.py -o iconic.json -s LOG_ENABLED=False
echo '......Downloading images and text into folder......'
mkdir image
mkdir text
python3 iconicDownloader.py
echo '--------FINISHED--------'