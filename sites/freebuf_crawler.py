from crawler_util.crawler_with_parsel import CrawlerParsel


class FreeBufCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://www.freebuf.com/',
            __post_item_xpath__='//div[@class="article-item"]//div[@class="title-view"]/div[@class="title-left"]/a[1]',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/span/text()'
        )
        for post in posts:
            post['url'] = 'https://www.freebuf.com' + post['url']
        return posts
