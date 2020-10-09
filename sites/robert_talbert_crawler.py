from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class RobertTalbertCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='http://rtalbert.org/',
            __post_item_xpath__='//article/header[@class="post-header"]/h2/a',
            __post_url_func__=lambda url: 'http://rtalbert.org' + url
        )
        return posts


class RobertTalbertCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(RobertTalbertCrawler)
