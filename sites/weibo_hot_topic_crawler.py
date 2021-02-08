from crawler_util.crawler_with_parsel import CrawlerParsel, http_get_text
import unittest
import json
import time
import requests
from lxml import etree


class WeiboHotTopicCrawler:
    @staticmethod
    async def fetch():
        url = "https://s.weibo.com/top/summary?cate=realtimehot"
        headers = {
            'Host': 's.weibo.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://weibo.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            return []
        html_xpath = etree.HTML(r.text)
        data = html_xpath.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]')
        posts = []
        for tr in (data):
            title = tr.xpath('./a/text()')
            url = tr.xpath('./a/@href')
            if len(title) <= 0 or len(url) <= 0:
                continue
            title = title[0]
            url = "https://s.weibo.com{}".format(url[0])
            posts.append({
                'title': title,
                'url': url
            })
        return posts


class WeiboHotTopicCrawlerTester(unittest.TestCase):
    def test_fetch(self):
        CrawlerParsel.test_fetch(WeiboHotTopicCrawler)
