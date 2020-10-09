from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class NineTwoEZCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://www.92ez.com/',
            __post_item_xpath__='//div[@class="post-main"]/h1[@class="post-title"]'
        )


class NineTwoEZCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(NineTwoEZCrawler)
