from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class RobertTalbertCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='http://rtalbert.org/',
            __post_item_xpath__='//article/header[@class="post-header"]/h2/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
        for post in posts:
            post['url'] = 'http://rtalbert.org' + post['url']
        return posts


class RobertTalbertCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        posts = RobertTalbertCrawler.fetch()
        for post in posts:
            print(post)
