from crawler_util.crawler_with_parsel import CrawlerParsel


class YinwangCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='http://www.yinwang.org/',
            __post_item_xpath__='//li[@class="list-group-item title"]',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
        for post in posts:
            post['url'] = 'http://www.yinwang.org' + post['url']
        return posts
