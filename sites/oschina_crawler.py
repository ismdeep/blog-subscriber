from crawler_util.crawler_with_parsel import CrawlerParsel


class OSChinaIndustryCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://www.oschina.net/news/industry',
            __post_item_xpath__='//div[@class="item news-item"]//h3[@class="header"]/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )


class OSChinaBlogCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://www.oschina.net/blog',
            __post_item_xpath__='//div[@class="item blog-item"]//a[@class="header"]',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )