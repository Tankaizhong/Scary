import scrapy
from movie.items import GameItem


class GameSpider(scrapy.Spider):
    name = "game"  # 爬虫名字
    allowed_domains = ["4399.com"]  # 域名

    start_urls = ["https://4399.com/"]  # 起始页面

    custom_settings = {
        'ITEM_PIPELINES': {
            'movie.pipelines.GamePipeline': 800,
        }
    }

    def parse(self, response):
        item = GameItem()
        game_list = response.xpath("//ul[@class='tm_list']/li/a/text()").extract()  # 数据提取

        for selector in game_list:
            item['name'] = selector
            print(selector)
            yield item
        pass
