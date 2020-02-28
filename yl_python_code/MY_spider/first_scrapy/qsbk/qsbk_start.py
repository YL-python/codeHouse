from scrapy import cmdline

# cmdline.execute("scrapy crawl qsbk_spider".split())   因为命令窗需要输入列表才行代码等价
cmdline.execute(['scrapy','crawl','qsbk_spider'])