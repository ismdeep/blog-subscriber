from crawler_util.crawler_with_parsel import CrawlerParsel


class ProgramThinkCrawler:
    @staticmethod
    async def fetch():
        return await CrawlerParsel.fetch(
            __url__='https://program-think.blogspot.com/',
            __post_item_xpath__='//div[@class="blog-posts hfeed"]//h1[@class="post-title entry-title"]/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
