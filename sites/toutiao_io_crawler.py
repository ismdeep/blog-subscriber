from crawler_util.crawler_with_parsel import CrawlerParsel


class ToutiaoIOCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://toutiao.io/posts/hot/7',
            __post_item_xpath__='//div[@class="post"]//h3[@class="title"]/a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
        for post in posts:
            post['url'] = 'https://toutiao.io' + post['url']
        return posts