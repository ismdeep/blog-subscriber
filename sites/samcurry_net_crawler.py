from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class SamCurryNetCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://samcurry.net/blog/',
            __post_item_xpath__='//article//header[@class="entry-header"]//h2[@class="entry-title"]/a'
        )


class SamCurryNetCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(SamCurryNetCrawler)
