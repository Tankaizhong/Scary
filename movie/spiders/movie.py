import scrapy
from movie.items import DoubanItem
from lxml import etree

# 创建lxml解析器对象
parser = etree.HTMLParser()


class MovieSpider(scrapy.Spider):
    name = "movie"  # 爬虫名字
    allowed_domains = ["movie.douban.com"]  # 域名
    start_urls = ["https://movie.douban.com/top250"]  # 起始页面
    custom_settings = {
        'ITEM_PIPELINES': {
            'movie.pipelines.MoviePipeline': 300,
        }
    }

    def parse(self, response):

        movie_list = response.xpath("//ol[@class='grid_view']/li").extract()  # 获取全部电影列表

        for selector in movie_list:
            tree = etree.fromstring(selector, parser)
            item = DoubanItem()
            item['name'] = tree.xpath('//span[@class="title"]/text()')[0]
            item['ranking'] = tree.xpath("//em/text()")
            item['star'] = tree.xpath("//span[@class='rating_num']/text()")
            item['describe'] = tree.xpath("//span[@class='inq']/text()")
            print(item)
            yield item  # 将结果item对象返回给Item管道
            # 下一个网页
        next_link = response.xpath("//span[@class='next']/a[1]/@href").extract_first()
        if next_link:
            next_link = "https://movie.douban.com/top250" + next_link
            print(next_link)
            # 将Request请求提交给调度器
            yield scrapy.Request(next_link, callback=self.parse)
            # 爬取网页中的下一个页面url信息
        pass
