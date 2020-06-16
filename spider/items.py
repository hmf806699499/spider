# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# 此文件用来定义爬取数据的模型或者说种类（优化的作用：针对SPIDER返回PIPELINE的数据）

import scrapy


class SpiderItem(scrapy.Item):
    # 固定写法
    author = scrapy.Field()
