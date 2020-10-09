from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class MarkKarpovCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://markkarpov.com/posts.html',
            __post_item_xpath__='//table[@class="table table-striped mt-3"]/tr//a',
            __post_url_func__=lambda url: 'https://markkarpov.com' + url if url[0] == '/' else url
        )
        return posts


class MarkKarpovCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(MarkKarpovCrawler)