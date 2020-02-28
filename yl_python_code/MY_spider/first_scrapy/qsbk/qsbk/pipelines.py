# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("data.json","wb")
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding = 'utf-8')

    def open_spider(self,spider):
        print("爬虫开始。。。")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        print("爬虫结束。。。")

    # 第一个是方便代码少 但是存的文件是一个个的字典之后使用的时候就要一行一行的读 数据量大的时候使用
    # 第二个是代码多但是存的文件是列表 之后使用可以一次性的读 数据量小的时候使用 是先写到内存 在self.exporter.export_item(item)时一次性写入
    # 第三个是最原始的方法

# from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter
#
# class QsbkPipeline(object):
#     def __init__(self):
#         print("6666666666666666666")
#         self.fp = open("data.json","wb")
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding = 'utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self,spider):
#         print("333333333333333333333333")
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         print("4444444444444444444444")


# class QsbkPipeline(object):
#     def __init__(self):
#         print("6666666666666666666")
#         self.fp = open("data.json","w",encoding='utf-8')
#
#     def open_spider(self,spider):
#         print("333333333333333333333333")
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+'\n')
#         return item
#
#     def close_spider(self,spider):
#         self.fp.close()
#         print("4444444444444444444444")
