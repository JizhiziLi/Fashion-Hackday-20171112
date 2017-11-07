###########
# Created by Jizhizi Li @ 07/10/2017
# A simple web crawler class to crawl images and text
# from Iconic website (https://www.theiconic.com.au) 
# second-level (individual product page)
# to be used as raw data in a coming fashion-hack-day
#
# Input: individual product url
# Output: $index.json file to store image urls and text
###########


import scrapy


class IconicSecondSpider(scrapy.Spider):
    name = "Iconic"
    def __init__(self, url='', *args, **kwargs):
        super(IconicSecondSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        print ('Crawling page: ' +str(response))
        for quote in response.css('a.product-image-frame'):
            srcString = 'None'
            if(quote.css('img ::attr(data-src)').extract_first() is not None):
                srcString = 'https:'+quote.css('img ::attr(data-src)').extract_first()
            elif(quote.css('img ::attr(src)').extract_first() is not None):
                srcString = 'https:'+quote.css('img ::attr(src)').extract_first()
            else:
                srcString = 'None'
            yield {
                'imageurl': srcString
                }
        for text in response.css('div.product-description'):
            yield {
            'text':text.css('p ::text').extract()
            }
      



