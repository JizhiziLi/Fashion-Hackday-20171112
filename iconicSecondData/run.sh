###########
# Created by Jizhizi Li @ 07/11/2017
# A shell file to help run 
#
# Input: iconicURLSpider.py iconicSecondSpider.py iconicDownloader.py
# Output: one folder: ~data to store resultes
###########

#!/bin/bash
rm -rf url.json
rm -r data
echo '--------LETS ROCK--------'
echo '......Crawling the website ICONIC in first level and create url.json for individual page.......'

scrapy runspider iconicURLSpider.py -o url.json -s LOG_ENABLED=False

value=($(jq -r '.[].imageurl' url.json))
length=${#value[@]}
echo 'The total number of files is:'
echo $length

mkdir data
mkdir data/JSON
mkdir data/image
mkdir data/text

echo '......Started to crawl in second level and download images/text.......'

for ((urlindex=0; urlindex<length; urlindex++)); do
   	echo '-------------now downloading: '${urlindex}'/'$length'----------'
	mkdir data/image/${urlindex}
	scrapy runspider iconicSecondSpider.py -a url=${value[urlindex]} -o data/JSON/${urlindex}.json -s LOG_ENABLED=False
	python3 iconicDownloader.py data/JSON/${urlindex}.json ${urlindex}
done

echo '--------FINISHED--------'