from crawler_util.crawler_with_parsel import CrawlerParsel


class ICoderTechCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://icoder.tech/',
            __post_item_xpath__='//article//header[@class="article-header"]//a[@class="article-title"]',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
        for post in posts:
            post['url'] = 'https://icoder.tech' + post['url']
        return posts
