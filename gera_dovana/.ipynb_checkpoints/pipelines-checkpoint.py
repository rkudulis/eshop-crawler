# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class GeraDovanaPipeline(object):

    def open_spider(self, spider):
        self.file = codecs.open("scraped_data_utf8.json", 'w', encoding='utf-8')
        self.item_no = 0
        self.file.write("{")

    def process_item(self, item, spider):
        data = json.dumps(dict(item), ensure_ascii=False)
        line =  f'"{self.item_no}": {data},'
        self.file.write(line)
        self.item_no += 1
        return item
    
    def spider_closed(self, spider):
        self.file.write("}")
        self.file.close()
