from crawler_util.crawler_with_parsel import CrawlerParsel


class NineTwoEZCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://www.92ez.com/',
            __post_item_xpath__='//div[@class="post-main"]/h1[@class="post-title"]',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
