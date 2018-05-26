# -*- coding: utf-8 -*-
import scrapy,json
from scrapy.http import Request,FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.renren.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    def start_requests(self):
        url = "http://www.renren.com/ajaxLogin/login"
        #首先爬取一下登录界面，然后进入回调函数parse()
        return [Request(url,meta={"cookiejar":1},callback=self.parse)]

    def parse(self, response):
        captcha = response.selector.css('img#verifyPic_login::sttr("src")').extract()
        print(ca)
        #设置要传递的post信息
        data = {
            'email': '17307410520',
            'icode': '',
            'origURL': 'http://www.renren.com/home',
            'domain': 'renren.com',
            'key_id': '1',
            'captcha_type': 'web_login',
            'password': '221355393d7110a907f76a3236c9fd66c6831215f7f5b819525312304e979629',
            'rkey': '5cfc39913fcf7e6a1d809c814338888e',
            'f': 'http%3A%2F%2Fwww.renren.com%2F966120994',
        }
        print("*"*80)
        print("登录中。。。")
        #next_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018461815980"
        #使用FormRequest提交信息登录
        return [FormRequest.from_response(response,
                #设置cookie信息
                meta = {'cookiejar':response.meta["cookiejar"]},
                #设置headers信息模拟浏览器
                headers = self.headers,
                #设置post表单中的数据
                formdata = data,
                #设置回调函数为next()
                callback = self.next,
                )]

    def next(self,response):
        print("此时已经登录完成并爬取了页面数据")
        print(response.selector.css("title::text")).extract_first()