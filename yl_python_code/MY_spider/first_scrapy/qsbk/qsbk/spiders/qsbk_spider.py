# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from first_scrapy.qsbk.qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    print("111111111111111111111111")
    name = 'qsbk_spider'   # 爬虫名称
    allowed_domains = ['qiushibaike.com']   # 允许的域名
    start_urls = ['https://www.qiushibaike.com/text/page/1/']   # 目标URL  列表 可以传递多个URL
    pinjie_url= 'https://www.qiushibaike.com'

# 执行parse时数据已经爬取下来了 以response传递给parse 现在，在parse里面对response处理

    def parse(self, response):
        data_xpath = response.xpath("//div[@id='content-left']/div")
        for data in data_xpath:
            zuozhe = data.xpath(".//h2//text()").get().strip()
            duanzhi = data.xpath(".//span/text()").extract()
            duanzhi = ''.join(duanzhi).strip()
            item = QsbkItem(zuozhe = zuozhe,duanzhi = duanzhi)
            yield item
            # data_duanzhi = {'zuozhe':zuozhe,"duanzhi":duanzhi}
            # yield data_duanzhi
        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.pinjie_url+next_url,callback=self.parse) #callback是 对返回的response进行什么操作的函数
