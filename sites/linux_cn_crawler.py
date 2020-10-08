from crawler_util.crawler_with_parsel import CrawlerParsel


async def linux_cn_common_fetch(__url__):
    return await CrawlerParsel.fetch(
        __url__=__url__,
        __post_item_xpath__='//span[@class="title"]/a',
        __post_url_xpath__='//a/@href',
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
