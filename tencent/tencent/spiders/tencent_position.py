# -*- coding: utf-8 -*-
import scrapy


class TencentPositionSpider(scrapy.Spider):
    name = "tencent_position"
    allowed_domains = ["hr.tencent.com"]
    url_ = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url_ + str(offset)]

    def parse(self, response):
        items = response.xpath('//*[contains(@class,"odd") or contains(@class,"even")]')
        for item in items:
            temp = dict(
                position_name=item.xpath('./td[1]/a/text()').extract()[0],
                position_num=item.xpath('./td[3]/text()').extract()[0]
            )
            yield temp

        if self.offset <= 2620:
            self.offset += 10
            url = self.url_ + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)
