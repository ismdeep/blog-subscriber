from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


class MysqlTaobaoOrgMonthlyCrawler:
    @staticmethod
    async def fetch():
        month_list = await CrawlerParsel.fetch(
            __url__='http://mysql.taobao.org/monthly/',
            __post_item_xpath__='//ul[@class="posts"]/li/h3/a',
            __post_url_func__=lambda url: 'http://mysql.taobao.org' + url,
            __post_title_func__=lambda title: title.encode('raw_unicode_escape').decode('utf-8', errors='ignore')
        )
        posts = []
        for month in month_list:
            month_posts = await CrawlerParsel.fetch(
                __url__=month['url'],
                __post_item_xpath__='//ul[@class="posts"]/li/h3/a',
                __post_url_func__=lambda url: 'http://mysql.taobao.org' + url,
                __post_title_func__=lambda title: title.encode('raw_unicode_escape').decode('utf-8', errors='ignore')
            )
            [posts.append(post) for post in month_posts]
        return posts


class MysqlTaobaoOrgMonthlyCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(MysqlTaobaoOrgMonthlyCrawler)
