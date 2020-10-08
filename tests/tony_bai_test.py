import unittest
from sites.tony_bai_crawler import TonyBaiCrawler


class TonyBaiCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        posts = TonyBaiCrawler.fetch()
        for post in posts:
            print(post)
