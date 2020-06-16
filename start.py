from scrapy import cmdline
# 该文件用来代替命令窗口
# cmdline.execute("scrapy crawl spider_1".split())

# 等价于
cmdline.execute(['scrapy', 'crawl', 'spider_1'])
