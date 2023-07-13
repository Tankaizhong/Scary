# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json


# 它们会在蜘蛛开始爬取时打开对应的文件，并在处理每个数据项时将其写入文件。在蜘蛛关闭时，文件将被关闭。
class MoviePipeline:

    def open_spider(self, spider):
        self.file = open('movie.json', 'w', encoding='utf-8')
        self.data = []

    def close_spider(self, spider):
        json.dump(self.data, self.file, ensure_ascii=False, indent=4)
        self.file.close()

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item


class GamePipeline:

    def open_spider(self, spider):
        self.file = open('game.json', 'w', encoding='utf-8')
        self.data = []

    def close_spider(self, spider):
        json.dump(self.data, self.file, ensure_ascii=False, indent=4)
        self.file.close()

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item
