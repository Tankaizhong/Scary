from movie.spiders.movie import MovieSpider

from scrapy import cmdline

cmdline.execute('scrapy crawl movie'.split())
