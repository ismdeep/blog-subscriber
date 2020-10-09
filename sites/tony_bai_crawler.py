from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class TonyBaiCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://tonybai.com/articles/',
            __post_item_xpath__='//div[@class="post-content"]//ul/li/a'
        )


class TonyBaiCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(TonyBaiCrawler)
