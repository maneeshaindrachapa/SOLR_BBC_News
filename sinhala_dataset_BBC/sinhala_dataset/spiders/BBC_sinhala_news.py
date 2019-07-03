# -*- coding: utf-8 -*-
import scrapy

value = 0
class BbcSinhalaNewsSpider(scrapy.Spider):
    name = 'BBC_sinhala_news'
    allowed_domains = ['https://www.bbc.com']
    start_urls = ['https://www.bbc.com/sinhala/sport','https://www.bbc.com/sinhala/world','https://www.bbc.com/sinhala/topics/f6ec89fd-3823-498e-a888-572e96f791b2','https://www.bbc.com/sinhala/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53','https://www.bbc.com/sinhala/topics/e45cb5f8-3c87-4ebd-ac1c-058e9be22862','https://www.bbc.com/sinhala/sri_lanka']
    custom_settings={ 'FEED_URI': "BBC_sinhala%(time)s.json",
                    'FEED_FORMAT': 'json'}
    def parse(self, response):
        print("procesing:"+response.url)
        #Extract data using css selectors
        #title = response.xpath("//div[@class='budgie-item faux-block-link']/div[@class='budgie__body']/a[@class='title-link']/h3[@class='title-link__title']/span[@class='title-link__title-text']/text()").extract()
        title=response.css('.title-link__title-text::text').extract()
        description=response.css('.eagle-item__summary::text').extract()
        category = response.xpath("//ul[@class='navigation-wide-list']/li[@class='selected']/a/span/text()").extract()

        row_data=zip(title,description)
        global value
        value =value +1
        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                'id':value,
                'page':response.url,
                'category':response.xpath("//ul[@class='navigation-wide-list']/li[@class='selected']/a/span/text()").extract(),
                'title' : item[0], #item[0] means product in the list and so on, index tells what value to assign
                'description' : item[1],
            }
            
            value+=1
            #yield or give the scraped info to scrapy
            yield scraped_info
