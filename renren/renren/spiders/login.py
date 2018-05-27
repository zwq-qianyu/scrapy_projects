# -*- coding: utf-8 -*-
import scrapy,json,re
from scrapy.http import Request,FormRequest
from urllib.request import urlretrieve
import requests

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/SysHome.do']
    s = requests.Session()
    #设置headers信息
    headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '315',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'anonymid=jhma20h7-d2ia5g; depovince=GW; _r01_=1; ln_uact=17307410520; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; JSESSIONID=abckMEdiTQ9rj-2Dl6Bow; ick_login=da23df9f-9bd3-4b41-8629-6d8b6f2f5569; first_login_flag=1; XNESSESSIONID=abc_jO9MNM_VmhwgxeCow; jebe_key=344542d5-2872-4328-aa41-c2b8aa16899a%7C610613683b498cf74aca75e4aed23ce7%7C1527271812440%7C1%7C1527383773920; loginfrom=null; wp_fold=0; jebecookies=61f33938-3189-49f7-ae28-be6489cc6846|||||',
    'Host': 'www.renren.com',
    'Origin': 'http://www.renren.com',
    'Referer': 'http://www.renren.com/SysHome.do',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.56 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    }

    def parse(self, response):
        #获取验证码图片地址
        captcha = response.selector.xpath('//img[@id="verifyPic_login"]/@src').extract()
        #将验证码图片存在本地
        urlretrieve(captcha[0],"./check.jpg")
        print("请查看项目中的本地文件check.jpg图片并输入验证码：")
        #获取验证码内容
        captcha_value = input()
        if len(captcha)>0:
            print("此时有验证码")
            #设置要传递的post信息
            data = {
                'email': '17307410520',
                'icode': captcha_value,
                'origURL': 'http://www.renren.com/home',
                'domain': 'renren.com',
                'key_id': '1',
                'captcha_type': 'web_login',
                'password': '0e0ca38e0c94518927bc8fae47bed3ff9f0db295e362d0afcfa9a2bcfc81f5ce',
                'rkey': '4b386eddf6a2bbc4c050788aabf08d7b',
                'f': 'http%3A%2F%2Fwww.renren.com%2F966120994',
            }
            
        else:
            print("此时没有验证码")
            #设置要传递的post信息
            data = {
                'email': '17307410520',
                'icode': '',
                'origURL': 'http://www.renren.com/home',
                'domain': 'renren.com',
                'key_id': '1',
                'captcha_type': 'web_login',
                'password': '0e0ca38e0c94518927bc8fae47bed3ff9f0db295e362d0afcfa9a2bcfc81f5ce',
                'rkey': '4b386eddf6a2bbc4c050788aabf08d7b',
                'f': 'http%3A%2F%2Fwww.renren.com%2F966120994',
            }
        print("*"*80)
        print("登录中。。。")
        login_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018461815980"
        res = self.s.post(login_url,data=data)
        
        '''访问会员中心，并爬取信息'''
        url ='http://www.renren.com/966120994'
        res = self.s.get(url)
        html = res.content.decode('utf-8')
        #html = gzip.decompress(res.read()).decode('utf-8')
        #print(html)
        print("此时已经登录完成并爬取了页面数据")
        #print(re.findall("<title>(.*?)</title>",html))
        #使用FormRequest提交信息登录
        '''
        return [FormRequest.from_response(response,
                #设置headers信息模拟浏览器
                headers = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                    'Connection': 'keep-alive',
                    'Content-Length': '315',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Cookie': response.headers['Set-Cookie'],
                    'Host': 'www.renren.com',
                    'Origin': 'http://www.renren.com',
                    'Referer': 'http://www.renren.com/SysHome.do',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.56 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest',
                },
                #设置post表单中的数据
                formdata = data,
                #设置回调函数为next()
                callback = self.next,
                )]
        

    def next(self,response):
        print("此时已经登录完成并爬取了页面数据")
        print(response.selector.css("title::text")).extract_first()
    '''