from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest
import asyncio


class OSChinaIndustryCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://www.oschina.net/news/widgets/_news_index_generic_list',
            __post_item_xpath__='//div[@class="item news-item"]//h3[@class="header"]/a'
        )


class OSChinaBlogCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://www.oschina.net/blog/widgets/_blog_index_recommend_list?classification=0',
            __post_item_xpath__='//div[@class="item blog-item"]//a[@class="header"]',
        )


class OSChinaCrawlerTester(unittest.TestCase):
    def test_industry_fetch(self):
        CrawlerParsel.test_fetch(OSChinaIndustryCrawler)

    def test_blog_fetch(self):
        CrawlerParsel.test_fetch(OSChinaBlogCrawler)
