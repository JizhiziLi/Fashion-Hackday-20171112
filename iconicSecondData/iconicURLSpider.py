###########
# Created by Jizhizi Li @ 07/11/2017
# A spider used to crawl within iconic womens-clothing-jeans homepage
# to grab url for each individual product page
#
# Input: Last page of Iconic website womens clothing jeans
# Output: a file [~/url.json] to store url for each individual product
###########

import scrapy
class IconicURLSpider(scrapy.Spider):
    name = "Iconic"
    start_urls = [
        # 'https://www.theiconic.com.au/womens-clothing-jeans/'
        'https://www.theiconic.com.au/womens-clothing-jeans/?page=15'
    ]
    def parse(self, response):
        print ('Crawling page: ' +str(response))
        b = 0
        for quote in response.css('div.medium-4'):
            for a in quote.css('figure'):
                if(a.css('a ::attr("href")').extract_first() is not None):
                    pageurl = 'https://www.theiconic.com.au'+a.css('a ::attr("href")').extract_first()
                yield {
                'imageurl': pageurl,
                }

        
        next_page = response.css('li.arrow a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)