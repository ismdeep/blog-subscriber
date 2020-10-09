from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class ToutiaoIOCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://toutiao.io/posts/hot/7',
            __post_item_xpath__='//div[@class="post"]//h3[@class="title"]/a',
            __post_url_func__=lambda url: 'https://toutiao.io' + url
        )
        return posts


class ToutiaoIOCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(ToutiaoIOCrawler)
