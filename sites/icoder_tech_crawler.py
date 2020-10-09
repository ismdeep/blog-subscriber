from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class ICoderTechCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://icoder.tech/',
            __post_item_xpath__='//article//header[@class="article-header"]//a[@class="article-title"]',
            __post_url_func__=lambda url: 'https://icoder.tech' + url
        )
        return posts


class ICoderTechCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(ICoderTechCrawler)
