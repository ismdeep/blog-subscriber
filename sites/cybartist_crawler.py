from crawler_util.crawler_with_parsel import CrawlerParsel


class CybartistCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://cybart.ist/',
            __post_item_xpath__='//article[@class="item"]//header',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/h2/text()'
        )
        for post in posts:
            post['url'] = 'https://cybart.ist' + post['url']
        return posts
