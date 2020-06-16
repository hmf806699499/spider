# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 就是 ITEM PIPELINES模块 用来存储数据
# 想要执行这个文件，setting 文件中 解开 ITEM_PIPELINES

# 导入文件使用，
# import json
#
# class SpiderPipeline(object):
#
#     # 爬虫开始时打开的文件，也可以放再open函数中
#     def __init__(self):
#         # 爬虫数据要写入的文件
#         self.fp = open("saveText.json", 'w', encoding='utf-8')
#
#     # 爬虫打开之后就会调用这个函数
#     def open_spider(self, spider):
#         print("爬虫开始了......")
#
#     # 爬虫运行过程中的传递数据调用这个函数
#     def process_item(self, item, spider):
#         # 需要将传入的数据 item，导入json
#         # 将字典 dict 转换成字符串 str,并解释成中文
#         # item_json = json.dumps(item, ensure_ascii=False)
#
#         # item是 ITEM模型传过来的啊，用dict转变数据类型
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(item_json + "\n")
#         return item
#
#     # 爬虫调用完成之后调用
#     def close_spider(self, spider):
#         self.fp.close()
#         print("爬虫结束了......")


# PIPELINES 优化存储方式:导入方式：一个字典{}是列表中的一项，不是前面的一个字典一行
# 缺点是不能存储太大的数据
# from scrapy.exporters import JsonItemExporter
#
# class SpiderPipeline(object):
#
#     # 爬虫开始时打开的文件，也可以放再open函数中
#     def __init__(self):
#         # 爬虫数据要写入的文件(wb 二进制写入 JsonItemExporter必须用这个)
#         # 同时二进制写入就不再指定编码方式
#         self.fp = open("saveText.json", 'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         # 开始导入
#         self.exporter.start_exporting()
#
#     # 爬虫打开之后就会调用这个函数
#     def open_spider(self, spider):
#         print("爬虫开始了......")
#
#     # 爬虫运行过程中的传递数据调用这个函数
#     def process_item(self, item, spider):
#         # 需要将传入的数据 item，导入json
#         # 将字典 dict 转换成字符串 str,并解释成中文
#         # item_json = json.dumps(item, ensure_ascii=False)
#
#         # item是 ITEM模型传过来的啊，用dict转变数据类型
#         # item_json = json.dumps(dict(item), ensure_ascii=False)
#         # self.fp.write(item_json + "\n")
#         # return item
#
#         self.exporter.export_item(item)
#         return item
#
#     # 爬虫调用完成之后调用
#     def close_spider(self, spider):
#         # 完成导入
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束了......")


# 第三种方式和第一中类似：结果是一个字典一行，但不能将其当做一整个字符串
from scrapy.exporters import JsonLinesItemExporter

class SpiderPipeline(object):

    # 爬虫开始时打开的文件，也可以放再open函数中
    def __init__(self):
        # 爬虫数据要写入的文件(wb 二进制写入 JsonItemExporter必须用这个)
        # 同时二进制写入就不再指定编码方式
        self.fp = open("saveText.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        # 不需要开始导入
        # self.exporter.start_exporting()

    # 爬虫打开之后就会调用这个函数
    def open_spider(self, spider):
        print("爬虫开始了......")

    # 爬虫运行过程中的传递数据调用这个函数
    def process_item(self, item, spider):
        # 需要将传入的数据 item，导入json
        # 将字典 dict 转换成字符串 str,并解释成中文
        # item_json = json.dumps(item, ensure_ascii=False)

        # item是 ITEM模型传过来的啊，用dict转变数据类型
        # item_json = json.dumps(dict(item), ensure_ascii=False)
        # self.fp.write(item_json + "\n")
        # return item

        self.exporter.export_item(item)
        return item

    # 爬虫调用完成之后调用
    def close_spider(self, spider):
        # 不需要完成导入
        # self.exporter.finish_exporting()
        self.fp.close()
        print("爬虫结束了......")
