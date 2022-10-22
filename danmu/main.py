# 部分弹幕功能代码来自项目：https://github.com/IsoaSFlus/danmaku，感谢大佬
# 快手弹幕代码来源及思路：https://github.com/py-wuhao/ks_barrage，感谢大佬
# 仅抓取用户弹幕，不包括入场提醒、礼物赠送等。

import asyncio

from danmu import danmaku
from util import bulletUtil, redisUtil
import setting

LIST_KEY = setting.REDIS_LIST_KEY
KEY_LIST = setting.KEY_LIST


async def printer(q, room_id):
    while True:
        m = await q.get()
        if m['msg_type'] == 'danmaku':
            live = m["live"]
            name = m["name"]
            content = m["content"]
            bulletUtil.printBullet(live, room_id, name, content)
            for bullet in bulletUtil.splitBullet(content):
                bullet = bullet.lower()
                if bulletUtil.bulletInKeyList(bullet, KEY_LIST):
                    redisUtil.rPushBullet(LIST_KEY, bullet)


async def main(live_url):
    q = asyncio.Queue()
    room_id = live_url.split('/')[-1]
    dmc = danmaku.DanmakuClient(live_url, q)
    asyncio.create_task(printer(q, room_id))
    await dmc.start()


def danmuMain(live_url):
    asyncio.run(main(live_url))


if __name__ == '__main__':
    url = input('请输入直播间地址：\n')
    asyncio.run(main(url))

