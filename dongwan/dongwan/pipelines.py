# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
# import codecs


class DongwanPipeline(object):
    def __init__(self):
        self.filename = open('sunwz.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(content.encode('utf-8'))
        return item

    def spider_close(self):
        self.filename.close()