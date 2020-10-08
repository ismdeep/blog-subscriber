from crawler_util.crawler_with_parsel import CrawlerParsel


class T00lsCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://www.t00ls.net/tech.html',
            __post_item_xpath__='//div[@class="item_content"]/h4/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
        for post in posts:
            post['url'] = 'https://www.t00ls.net/' + post['url']
        return posts
