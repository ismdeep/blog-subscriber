from crawler_util.crawler_with_parsel import CrawlerParsel
import unittest


async def linux_cn_common_fetch(__url__):
    return await CrawlerParsel.fetch(
        __url__=__url__,
        __post_item_xpath__='//span[@class="title"]/a',
        __post_title_xpath__='//a/span/text()'
    )


class LinuxCnTechCrawler:
    @staticmethod
    async def fetch():
        return await linux_cn_common_fetch('https://linux.cn/tech/')


class LinuxCnNewsCrawler:
    @staticmethod
    async def fetch():
        return await linux_cn_common_fetch('https://linux.cn/news/')


class LinuxCnTalkCrawler:
    @staticmethod
    async def fetch():
        return await linux_cn_common_fetch('https://linux.cn/talk/')


class LinuxCnShareCrawler:
    @staticmethod
    async def fetch():
        return await linux_cn_common_fetch('https://linux.cn/share/')


class LinuxCnCrawlerTester(unittest.TestCase):
    def test_news_fetch(self):
        CrawlerParsel.test_fetch(LinuxCnNewsCrawler)

    def test_tech_fetch(self):
        CrawlerParsel.test_fetch(LinuxCnTechCrawler)

    def test_talk_fetch(self):
        CrawlerParsel.test_fetch(LinuxCnTalkCrawler)

    def test_share_fetch(self):
        CrawlerParsel.test_fetch(LinuxCnShareCrawler)
