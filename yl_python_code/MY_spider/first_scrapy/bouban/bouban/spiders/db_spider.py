# -*- coding: utf-8 -*-
import scrapy
from bouban.items import BoubanItem

class DbSpiderSpider(scrapy.Spider):
    name = 'db_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0']
    pjie_url = 'https://movie.douban.com/top250'

    def parse(self, response):
        print("%"*40)
        datas = response.xpath('//ol[@class="grid_view"]/li')
        for data in datas:
            dy_paimin = data.xpath('.//div[@class="pic"]/em/text()').get()
            dy_name = data.xpath('.//div[@class="hd"]/a/span[konachan_spider]/text()').get().strip()
            item = BoubanItem(排名 = dy_paimin,电影名 = dy_name)
            yield item
        next_url = response.xpath('//span[@class="next"]/a/@href').get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.pjie_url+next_url,callback=self.parse)
            print("%" * 40)
