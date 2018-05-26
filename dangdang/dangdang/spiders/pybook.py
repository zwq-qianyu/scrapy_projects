# -*- coding: utf-8 -*-
import scrapy,time
from dangdang.items import PybookItem


class PybookSpider(scrapy.Spider):
    name = 'pybook'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input&page_index=1']

    p = 1   #page
    def parse(self, response):
        '''解析并获取需要的信息'''
        #获取当前页面所有的书籍信息
        res = response.selector.css('ul.bigimg')
        dlist = res.css('li')
        print(len(dlist))
        for i in dlist:
            #将信息封装到item中去
            item = PybookItem()
            item['name'] = i.xpath("./a/@title").extract_first()
            item['author'] = i.xpath(".//a[@name='itemlist-author']/@title").extract_first()
            item['pre_price'] = i.xpath('.//p[@class="price"]/span[@class="search_pre_price"]/text()').extract_first()
            item['now_price'] = i.xpath('.//p[@class="price"]/span[@class="search_now_price"]/text()').extract_first()
            item['publish'] = i.xpath(".//a[@name='P_cbs']/@title").extract_first()
            item['pic'] = i.xpath('./a/img/@data-original').extract_first()
            item['detail'] = i.xpath("./p[@class='detail']/text()").extract_first()
            yield item

            self.p += 1
            if self.p <= 2:
                next_url = 'http://search.dangdang.com/?key=python&act=input&page_index='+str(self.p)
                print("="*80)
                print("等待1秒钟获取下一页")
                time.sleep(1)
                url = response.urljoin(next_url)
                yield scrapy.Request(url=url, callback=self.parse)
