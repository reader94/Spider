# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    #职位名称
    position_name = scrapy.Field()
    #招聘人数
    position_num = scrapy.Field()




#//td[@class='l square']/a/text()
