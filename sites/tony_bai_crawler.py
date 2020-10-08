from crawler_util.crawler_with_parsel import CrawlerParsel


class TonyBaiCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://tonybai.com/articles/',
            __post_item_xpath__='//div[@class="post-content"]//ul/li/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
