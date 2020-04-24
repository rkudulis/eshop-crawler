# -*- coding: utf-8 -*-
import scrapy
from gera_dovana.items import GeraDovanaItem
import re



class MainCrawlerSpider(scrapy.Spider):
    name = 'main_crawler'
    allowed_domains = ['www.geradovana.lt']
    start_urls = ['http://www.geradovana.lt/patirtis?showtree=1']

    def parse(self, response):
        # crawl categories

        # Get names of categories
        categories = response.css("p.name span::text").getall()

        # Get link of each category
        categoryXPath = ".//a[contains(@class, 'list-item')]/@href"
        hrefs = response.xpath(categoryXPath)

        for category, category_href in zip(categories, hrefs):
            yield response.follow(category_href, callback=self.parse_category, cb_kwargs=dict(category=category))

    def parse_category(self, response, category):
        # crawl given category
        itemXPath = ".//a[contains(@class, 'productlslink')]/@href"
        for item_href in response.xpath(itemXPath):
            yield response.follow(item_href, callback=self.parse_item, cb_kwargs=dict(category=category))

    def parse_item(self, response, category):
        # crawl item and return required data

        item = GeraDovanaItem()

        item['title'] = response.css("span[itemprop=name]::text").get()
        item['category'] = category
        item['price'] = response.css("b.value::text").get()

        location_raw = response.css("div.prodlocinfoblock1::text").getall()
        if location_raw:
            item['location'] = re.sub(r"\s+", "", location_raw[1])
        
        users_raw = response.css("div.prodlocinfoblock5::text").getall()
        if users_raw:
            item['users'] = re.sub(r"\s+|(asm\.)", "", users_raw[1])
        
        item['rating'] = response.css("span[itemprop=ratingValue]::text").get()
        item['votes'] = response.css("span[itemprop=reviewCount]::text").get()

        item['url'] = response.url

        return item