from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class MrMetroCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='http://miccall.tech/',
            __post_item_xpath__='//section[@class="link_box special"]',
            __post_title_xpath__='//a//h2/text()',
            __post_url_func__=lambda url: 'http://miccall.tech' + url
        )
        return posts


class MrMetroCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(MrMetroCrawler)
