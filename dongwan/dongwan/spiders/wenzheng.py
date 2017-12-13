# -*- coding: utf-8 -*-
import scrapy
from ..items import DongwanItem


class WenzhengSpider(scrapy.Spider):
    name = "wenzheng"
    allowed_domains = ["wz.sun0769.com"]
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        links = response.xpath("//div[@class='greyframe']/table//td/a[@class='news14']/@href").extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)
        if self.offset <= 83910:
            self.offset += 30
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_item(self, response):
        item = DongwanItem()
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(":")[-1]
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()

        item['url'] = response.url
        yield item

