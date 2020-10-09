from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class ProgramThinkCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://program-think.blogspot.com/',
            __post_item_xpath__='//div[@class="blog-posts hfeed"]//h1[@class="post-title entry-title"]/a'
        )


class ProgramThinkCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(ProgramThinkCrawler)
