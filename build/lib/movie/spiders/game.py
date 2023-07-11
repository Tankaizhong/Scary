import scrapy


class GameSpider(scrapy.Spider):
    name = "game"  # 爬虫名字
    allowed_domains = ["4399.com"]  # 域名

    start_urls = ["http://4399.com/"]  # 起始页面

    def parse(self, response):
        # print(response)
        # 拿到源代码,直接提取数据
        # response.xpath()  # xpath进行数据解析
        # response.css()  # xcss选择器 解析
        text = response.xpath("//ul[@class='tm_list']/li/a/text()").extract()  # 数据提取
        print(text)

        pass
