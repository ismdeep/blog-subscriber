from crawler_util.crawler_with_parsel import CrawlerParsel


class MarkKarpovCrawler:
    @staticmethod
    async def fetch():
        posts = await CrawlerParsel.fetch(
            __url__='https://markkarpov.com/posts.html',
            __post_item_xpath__='//table[@class="table table-striped mt-3"]/tr//a',
            __post_url_xpath__='//a/@href',
            __post_title_xpath__='//a/text()'
        )
        for post in posts:
            if post['url'][0] == '/':
                post['url'] = 'https://markkarpov.com' + post['url']
        return posts
