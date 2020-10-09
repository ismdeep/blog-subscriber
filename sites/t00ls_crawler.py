from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class T00lsCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://www.t00ls.net/tech.html',
            __post_item_xpath__='//div[@class="articles_content"]//div[@class="item_content"]/h4/a',
            __post_url_func__=lambda url: 'https://www.t00ls.net/' + url
        )
        return posts


class T00lsCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(T00lsCrawler)
