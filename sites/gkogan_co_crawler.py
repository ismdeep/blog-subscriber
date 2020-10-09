from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class GkoganCoCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://www.gkogan.co/blog/',
            __post_item_xpath__='//ul[@class="post-list"]/li/a',
            __post_url_func__=lambda post_url: 'https://www.gkogan.co' + post_url
        )
        return posts


class GkoganCoCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(GkoganCoCrawler)