# -*- coding: utf-8 -*-
# 抖音直播弹幕获取
# 先启动本程序作为服务端，再用浏览器进入想要获取弹幕的直播间，并启动对应的barrage.js文件作为客户端
# 将js获取到的弹幕json通过websocket发送到服务端程序输出
# 注意：websocket的地址和端口要对应

import asyncio
import websockets
import json
import setting

from util import bulletUtil, redisUtil

LIVE = "Douyin"
ROOM_ID = "666666"
WS_HOST = 'localhost'
WS_PORT = 5000
KEY_LIST = setting.KEY_LIST
LIST_KEY = setting.REDIS_LIST_KEY


async def handle(websocket):
    # print('抖音弹幕—连接成功')
    while True:
        data = await websocket.recv()
        data = json.loads(data)
        for data_count in data:
            bullet_type = data_count.get('type')
            name = data_count.get('nickname')
            content = data_count.get('content')
            if bullet_type == 'message':
                bulletUtil.printBullet(LIVE, ROOM_ID, name, content)
                for bullet in bulletUtil.splitBullet(content):
                    bullet = bullet.lower()
                    if bulletUtil.bulletInKeyList(bullet, KEY_LIST):
                        redisUtil.rPushBullet(LIST_KEY, bullet)


async def run(websocket):
    while True:
        try:
            await handle(websocket)
        except websockets.ConnectionClosed:
            # print('抖音弹幕—断开连接')
            break


def douyinMain(loop):
    loop.run_until_complete(websockets.serve(run, WS_HOST, WS_PORT))
    loop.run_forever()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(run, WS_HOST, WS_PORT))
    asyncio.get_event_loop().run_forever()
