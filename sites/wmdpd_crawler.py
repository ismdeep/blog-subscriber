from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class WmdpdCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://wmdpd.com/',
            __post_item_xpath__='//h2[@class="c-post-card__title"]/a',
            __post_url_func__=lambda url: 'https://wmdpd.com' + url
        )
        return posts


class WmdpdCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(WmdpdCrawler)
