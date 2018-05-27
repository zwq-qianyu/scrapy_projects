# scrapy_projects
<head>
<style>
.shadow {
　　　　-moz-box-shadow: 5px 5px 5px #ccc;
　　　　-webkit-box-shadow: 5px 5px 5px #ccc;
　　　　box-shadow: 5px 5px 5px #ccc;
　　}
</style>
</head>

<h2>目前内含有三个项目文件：</h2>

<h3><center>sina、renren、dangdang</center></h3>

1. 运行sina时先进入sina目录，然后执行: scrapy crawl sina
效果如下：
<img src="./show_img/sina.png" alt="sina爬虫案例图片“ style="radius=10px;width:100%;" class="shadow">

2. 进入renren爬虫项目文件后，爬虫运行命令: scrapy crawl login
   运行中如果产生验证码，请到项目文件中找到check.jpg，输入验证码后回车即可。

3. 运行dangdang时，先进入该目录下，然后项目文件中的需要导入pybook.sql数据库  最后执行：scrapy crawl pybook
