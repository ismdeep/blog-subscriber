from crawler_util.crawler_with_parsel import CrawlerParsel


class WmdpdCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://wmdpd.com/',
            __post_item_xpath__='//h2[@class="c-post-card__title"]/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
        for post in posts:
            post['url'] = 'https://wmdpd.com' + post['url']
        return posts
