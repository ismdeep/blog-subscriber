from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class CybartistCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://cybart.ist/',
            __post_item_xpath__='//article[@class="item"]//header',
            __post_title_xpath__='//a/h2/text()',
            __post_url_func__=lambda url: 'https://cybart.ist' + url
        )
        return posts


class CybartistCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(CybartistCrawler)
