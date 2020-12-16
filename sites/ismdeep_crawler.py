from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class IsmdeepCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://ismdeep.com/archives/',
            __post_item_xpath__='//article//a',
            __post_url_func__=lambda url: 'https://ismdeep.com' + url
        )


class IsmdeepCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(IsmdeepCrawler)
