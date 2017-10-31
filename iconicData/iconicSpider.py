###########
# Created by Jizhizi Li @ 31/10/2017
# A simple web crawler class to crawl images and text
# from Iconic website (https://www.theiconic.com.au)
# to be used as raw data in a coming fashion-hack-day
#
# Input: Last page of Iconic website womens clothing jeans
# Output: a file [~/iconic.json] to store each imageurl and text
###########


import scrapy
class IconicSpider(scrapy.Spider):
    name = "Iconic"
    start_urls = [
        # 'https://www.theiconic.com.au/womens-clothing-jeans/'
        'https://www.theiconic.com.au/womens-clothing-jeans/?page=15'
    ]
    def parse(self, response):
        print ('Crawling page: ' +str(response))
        b = 0
        for quote in response.css('div.medium-4'):
            # print('-------quote-----')
            # print(quote)
            for a in quote.css('span.image-frame'):
                # print('-------image------')
                # print(str(b))
                arcString = 'None'
                if(a.css('img ::attr(data-src)').extract_first() is not None):
                    arcString = 'https:'+a.css('img ::attr(data-src)').extract_first()
                elif(a.css('img ::attr(src)').extract_first() is not None):
                    arcString = 'https:'+a.css('img ::attr(src)').extract_first()
                else:
                    arcString = 'None'
                b = b+1
                yield {
                'imageurl': arcString,
                'text': a.css('img ::attr(alt)').extract_first()
                }
        
        next_page = response.css('li.arrow a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)