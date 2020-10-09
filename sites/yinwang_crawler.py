from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class YinwangCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='http://www.yinwang.org/',
            __post_item_xpath__='//li[@class="list-group-item title"]',
            __post_url_func__=lambda url: 'http://www.yinwang.org' + url
        )
        return posts


class YinwangCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(YinwangCrawler)
