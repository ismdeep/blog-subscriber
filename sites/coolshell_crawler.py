from crawler_util.crawler_with_parsel import CrawlerParsel


class CoolShellCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://coolshell.cn/',
            __post_item_xpath__='//h2[@class="entry-title"]/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
