from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class YakoazzCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://www.cnblogs.com/yakoazz/',
            __post_item_xpath__='//div[@class="post"]/h2/a',
            __post_title_xpath__='//a/span/text()'
        )


class YakoazzCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(YakoazzCrawler)
