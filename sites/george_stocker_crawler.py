from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class GeorgeStockerCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://georgestocker.com/',
            __post_item_xpath__='//section[@class="widget widget_recent_entries"]/ul/li/a'
        )


class GeorgeStockerCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(GeorgeStockerCrawler)
