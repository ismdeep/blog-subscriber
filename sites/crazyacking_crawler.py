from crawler_util.crawler_with_parsel import CrawlerParsel
from parsel import Selector
import unittest


class CrazyackingCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://www.cnblogs.com/crazyacking/',
            __post_item_xpath__='//div[@class="postTitle"]/a',
            __post_title_xpath__='//a/span',
            __post_title_func__=lambda __title__: Selector(__title__).xpath('//span/text()').extract()[-1].strip()
        )
        return posts


class CrazyackingCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(CrazyackingCrawler)
