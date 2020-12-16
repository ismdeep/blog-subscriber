import requests
from parsel import Selector
import asyncio

from monitor_util.monitor_util import MonitorUtil

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/85.0.4183.121 Safari/537.36'


async def http_get_text(__url__):
    return requests.get(url=__url__, headers={'User-Agent': user_agent}).text


class CrawlerParsel:
    @staticmethod
    async def fetch(__url__, __post_item_xpath__,
                    __post_url_xpath__='//a/@href',
                    __post_title_xpath__='//a/text()',
                    __post_url_func__=None,
                    __post_title_func__=None
                    ):
        posts = []
        selector = Selector(await http_get_text(__url__))
        posts_raw = selector.xpath(__post_item_xpath__).extract()
        for post_raw in posts_raw:
            post_selector = Selector(post_raw)
            post_url = post_selector.xpath(__post_url_xpath__).extract()[0]
            post_title = post_selector.xpath(__post_title_xpath__).extract()[0].strip()
            if __post_url_func__ is not None:
                post_url = __post_url_func__(post_url)
            if __post_title_func__ is not None:
                post_title = __post_title_func__(post_title)
            posts.append({
                'url': post_url,
                'title': post_title
            })
        from urllib import parse
        if len(posts) > 0:
            try:
                await MonitorUtil.update_status('blog-subscriber.' + parse.urlparse(__url__).hostname, 'true')
            except:
                pass
        return posts

    @staticmethod
    def test_fetch(__crawler_class__):
        posts = asyncio.run(__crawler_class__.fetch())
        [print(post) for post in posts]
