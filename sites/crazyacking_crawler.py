from crawler_util.crawler_with_parsel import CrawlerParsel
from parsel import Selector


class CrazyackingCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://www.cnblogs.com/crazyacking/',
            __post_item_xpath__='//div[@class="postTitle"]/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/span'
        )

        for post in posts:
            selector = Selector(post['title'])
            post['title'] = selector.xpath('//span/text()').extract()[-1].strip()
        return posts
