# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        f1 = open("./sina_rasult.txt",'w')
        list1 = response.selector.css("div.section")
        with open("./sina_rasult.txt",'a') as f:
            for tit1 in list1:
                print("="*80)
                s1 = str("="*80)
                f.write(s1+"\n\r")
                tit = ""
                for m in tit1.css("h2.tit01::text").extract():
                    tit += m
                print(tit)
                f.write(tit+"\n\r")
                i = 1
                for n in tit1.css("div.clearfix"):
                    print(str(i)+".",end=" ")
                    print(n.css("h3.tit02 a::text").extract_first())
                    s2 = n.css("h3.tit02 a::text").extract_first()
                    #print(type(s2))
                    f.write(str(i)+". "+str(s2))
                    i += 1
                    print("-"*80)
                    s3 = "-"*80
                    f.write(s3+"\n\r")
                    for k in n.css("ul li a::text").extract():
                        print(k,end="、") 
                        f.write(k+"、") 
                    print("\n\n")
                    f.write("\n\r\n\r")
