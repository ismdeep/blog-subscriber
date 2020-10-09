from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class CoolShellCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://coolshell.cn/',
            __post_item_xpath__='//h2[@class="entry-title"]/a',
        )


class CoolShellCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(CoolShellCrawler)
