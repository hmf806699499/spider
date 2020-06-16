# -*- coding: utf-8 -*-
import scrapy


# 用来写爬虫代码---就是框架的 SPIDER 部分

# 引用ITEM模型 （引用类）
from spider.items import SpiderItem

class Spider1Spider(scrapy.Spider):
    # 必须唯一
    name = 'spider_1'
    # 限制的域名
    allowed_domains = ['finance.591hx.com/lista/jygl.shtml']
    # 发送的请求地址 SPEDER -> ENGINE...
    start_urls = ['http://finance.591hx.com/lista/jygl.shtml/']

    # 定义基本域名:方便爬取多网页时,地址拼接
    base_domain = "http://finance.591hx.com/lista/jygl.shtml/"

    # 接收 DOWNLOADER数据，该方法 parse() 是对其进行解析 （数据存在response中）
    # response 的数据类型 scrapy.http.response.html.HtmlResponse

    from scrapy.http.response.html import HtmlResponse
    # contentLet(reponse.xpath) 返回的数据类型 scrapy.selector.unified.SelectorList
    from scrapy.selector.unified import SelectorList

    def parse(self, response):
        # 这个表示有40个 ==
        # response 返回数据的方法xpath,css 但是通常用 xpath
        # print("==" * 40)
        # 第一个div 是获取的整体内容，第二个div是下属的
        # SelectorList 结合类型,注意  div的 id 要取 大id
        # contentLeft = response.xpath("//div[@id='content']/div")

        contentLeft = response.xpath("//div[@id='content']/div")
        # Selector
        for content in contentLeft:
            # 这是获取作者等单条记录的方法,只有一个标签的时候使用
            # author = content.xpath(".//li/text()").get().strip()
            # author = content.xpath(".//div[@class='line']//text()").getall()
            author = content.xpath(".//div[@class='line']//text()").getall()

            # 变成字符串的方法
            author = "".join(author).strip()
            # print(author)

            # 方法一：构造成生成器，给PIPELINE 使用  ？生成器的作用
            # text = {'text': author}
            # yield text

            # 方法二（建议）：引用ITEMS模型
            item = SpiderItem(author = author)
            # 返回当前item
            yield item

            # 多个页面爬取：继续爬取
            # next_url = response.xpath("//div[@class='page']/a[last()]/@href")

            # next_url = response.xpath("//div[@class='page']/a[3]/@href")
            # if not next_url:
            #     return
            # else:
            #     yield scrapy.Request(self.base_domain + next_url, callback=self.parse)


        # print("==" * 40)



