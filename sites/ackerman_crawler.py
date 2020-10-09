from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class AckermanCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://www.cnblogs.com/-Ackerman/',
            __post_item_xpath__='//div[@class="postTitle"]',
            __post_title_xpath__='//a/span/text()'
        )


class AckermanCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(AckermanCrawler)
