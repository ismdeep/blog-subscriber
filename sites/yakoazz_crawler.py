from crawler_util.crawler_with_parsel import CrawlerParsel


class YakoazzCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://www.cnblogs.com/yakoazz/',
            __post_item_xpath__='//div[@class="post"]/h2/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/span/text()'
        )