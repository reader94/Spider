# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem
#import mySpider.items


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = (
        'http://www.itcast.cn/channel/teacher.shtml',
    )

    def parse(self, response):

        # with open("teacher.html","w") as f:
        #     f.write(response.body)
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            item = MyspiderItem()
            name = each.xpath("h3/text()").extract_first()
            level = each.xpath("h4/text()").extract_first()
            info = each.xpath("p/text()").extract_first()

            item['name'] = name
            item['level'] = level
            item['info'] = info

            # items.append(item)
            yield item
        # return items