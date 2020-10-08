from crawler_util.crawler_with_parsel import CrawlerParsel


class MrMetroCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='http://miccall.tech/',
            __post_item_xpath__='//section[@class="link_box special"]',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a//h2/text()'
        )
        for post in posts:
            post['url'] = 'http://miccall.tech' + post['url']
        return posts
