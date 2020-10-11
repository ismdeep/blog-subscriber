import sys
import logging
import json
import redis
import asyncio

import os

from telethon.sync import TelegramClient
from telethon import functions

from sites.program_think_crawler import ProgramThinkCrawler
from sites.coolshell_crawler import CoolShellCrawler
from sites.cybartist_crawler import CybartistCrawler
from sites.nine_two_ez_crawler import NineTwoEZCrawler
from sites.mr_metro_crawler import MrMetroCrawler
from sites.yakoazz_crawler import YakoazzCrawler
from sites.crazyacking_crawler import CrazyackingCrawler
from sites.ackerman_crawler import AckermanCrawler
from sites.yinwang_crawler import YinwangCrawler
from sites.freebuf_crawler import FreeBufCrawler
from sites.wmdpd_crawler import WmdpdCrawler
from sites.icoder_tech_crawler import ICoderTechCrawler
from sites.t00ls_crawler import T00lsCrawler
from sites.linux_cn_crawler import LinuxCnTechCrawler, LinuxCnTalkCrawler, LinuxCnNewsCrawler, LinuxCnShareCrawler
from sites.oschina_crawler import OSChinaIndustryCrawler, OSChinaBlogCrawler
from sites.toutiao_io_crawler import ToutiaoIOCrawler
from sites.mark_karpov_crawler import MarkKarpovCrawler
from sites.tony_bai_crawler import TonyBaiCrawler
from sites.robert_talbert_crawler import RobertTalbertCrawler
from sites.gkogan_co_crawler import GkoganCoCrawler
from sites.mysql_taobao_org_monthly_crawler import MysqlTaobaoOrgMonthlyCrawler
from sites.george_stocker_crawler import GeorgeStockerCrawler
from sites.samcurry_net_crawler import SamCurryNetCrawler
from sites.ismdeep_crawler import IsmdeepCrawler

work_dir = None
redis_config = None

REDIS_KEY_NAME = 'blogger_posts'

api_id = None
api_hash = None
channel_share_link = None
pool = None
client = None
channel = None


async def is_saved(__url__):
    conn = redis.Redis(connection_pool=pool)
    return conn.hexists(REDIS_KEY_NAME, __url__)


async def push_to_redis(__url__, __title__):
    conn = redis.Redis(connection_pool=pool)
    conn.hset(REDIS_KEY_NAME, __url__, __title__)
    logging.info('Pushed => %s' % __url__)


def init_logging():
    logging.basicConfig(
        filename=work_dir + '/product.log',
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s[%(levelname)s][line:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(filename)s[%(levelname)s][line:%(lineno)d] %(message)s')
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)


async def func(__blogger_tag__, __crawler__):
    posts = await __crawler__.fetch()
    for post in posts[::-1]:
        if not await is_saved(post['url']):
            await client(functions.messages.SendMessageRequest(
                peer=channel,
                message='%s\n%s\n%s' % (__blogger_tag__, post['title'], post['url']),
                no_webpage=False
            ))
            await push_to_redis(post['url'], post['title'])
            logging.info('Sent to channel => {%s, %s}' % (post['url'], post['title']))


def main():
    loop = asyncio.get_event_loop()
    tasks = [
        func('#coolshell', CoolShellCrawler),
        func('#编程随想', ProgramThinkCrawler),
        func('#cybartist', CybartistCrawler),
        func('#92ez', NineTwoEZCrawler),
        func('#mr_metro', MrMetroCrawler),
        func('#yakoazz', YakoazzCrawler),
        func('#crazyacking', CrazyackingCrawler),
        func('#ackerman', AckermanCrawler),
        func('#王垠', YinwangCrawler),
        func('#freebuf', FreeBufCrawler),
        func('#完美的胖达', WmdpdCrawler),
        func('#司徒公子', ICoderTechCrawler),
        func('#T00ls', T00lsCrawler),
        func('#Linux中国 #技术', LinuxCnTechCrawler),
        func('#Linux中国 #新闻', LinuxCnNewsCrawler),
        func('#Linux中国 #分享', LinuxCnShareCrawler),
        func('#Linux中国 #观点', LinuxCnTalkCrawler),
        func('#开源中国 #综合资讯', OSChinaIndustryCrawler),
        func('#开源中国 #博客', OSChinaBlogCrawler),
        func('#开发者头条', ToutiaoIOCrawler),
        func('#Mark_Karpov', MarkKarpovCrawler),
        func('#Tony_Bai', TonyBaiCrawler),
        func('#Robert_Talbert', RobertTalbertCrawler),
        func('#gkogan', GkoganCoCrawler),
        func('#数据库内核月报', MysqlTaobaoOrgMonthlyCrawler),
        func('#GeorgeStocker', GeorgeStockerCrawler),
        func('#SamCurry', SamCurryNetCrawler),
        func('#ismdeep', IsmdeepCrawler)
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    client.disconnect()
    loop.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 blogger-subscriber.py {work_dir}')
        exit(0)
    # 1. Fetch Working Directory
    work_dir = sys.argv[1]
    os.chdir(work_dir)
    # 2. Initialize logging Configuration
    init_logging()
    # 3. Get Redis Configuration
    redis_config = json.load(open(work_dir + '/redis.json', 'r'))
    pool = redis.ConnectionPool(host=redis_config['host'], port=redis_config['port'])
    try:
        redis.Redis(connection_pool=pool).ping()
    except Exception as e:
        print(e)
        exit(-1)
    # Set Telegram Bot
    telegram_bot_config = json.load(open(work_dir + '/telegram_bot.json', 'r'))
    api_id = telegram_bot_config['api_id']
    api_hash = telegram_bot_config['api_hash']
    channel_share_link = telegram_bot_config['channel_share_link']
    # 4. client connect
    # client2 = TelegramClient('anon', api_id, api_hash)
    # client2.start()
    # client2.disconnect()
    client = TelegramClient('anon', api_id, api_hash)
    client.connect()
    channel = client.get_entity(channel_share_link)
    # 4. Start main()
    main()
