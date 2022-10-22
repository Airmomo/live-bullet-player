import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from danmu.main import danmuMain
from danmu.douyin.main import douyinMain
from util import redisUtil
from pynput import keyboard

# 虎牙直播：https://www.huya.com/11352915
# 斗鱼直播：https://www.douyu.com/85894
# B站直播：https://live.bilibili.com/21470918
# 快手直播：https://live.kuaishou.com/u/jjworld126
# 火猫直播：
# 企鹅电竞：https://egame.qq.com/383204988
# 花椒直播：https://www.huajiao.com/l/303344861?qd=hu
# 映客直播：https://www.inke.cn/liveroom/index.html?uid=87493223&id=1593906372018299
# CC直播：https://cc.163.com/363936598/
# 酷狗直播：https://fanxing.kugou.com/1676290
# 战旗直播：
# 龙珠直播：http://star.longzhu.com/wsde135864219
# PPS奇秀直播：https://x.pps.tv/room/208337
# 搜狐千帆直播：https://qf.56.com/520208a
# 来疯直播：https://v.laifeng.com/656428
# LOOK直播：https://look.163.com/live?id=196257915
# AcFun直播：https://live.acfun.cn/live/23682490
# 艺气山直播：http://www.173.com/96


def on_press(key):
    # 监听事件，停止程序
    key = str(key)
    if key.startswith("Key."):
        key = key[4:]
    else:
        key = key[1]
    # print("按键为", key)
    if key == "f12":
        # 切换弹幕操作指令开关状态
        if redisUtil.tapBulletSwitch():
            print("弹幕操作指令状态：开启")
        else:
            print("弹幕操作指令状态：关闭")


def startKeyboardListener():
    # 键盘监听事件
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    live_urls = {
        "https://live.bilibili.com/66666",
        "https://www.douyu.com/43231",
        "https://www.douyu.com/5169209",
        "https://www.douyu.com/10718295",
        "https://www.huya.com/991111",
    }
    task_futures = []
    redisUtil.setBulletSwitchStatus(redisUtil.SWITCH_OFF_STATUS)
    # 同步asyncio.loop
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    # 最大线程数量
    max_worker_n = len(live_urls) + 2
    # 父线程捕获子线程抛出的异常
    with ThreadPoolExecutor(max_workers=max_worker_n) as executor:
        # 启动键盘监听事件
        task_futures.append(executor.submit(startKeyboardListener))
        # 启动直播弹幕线程
        for live_url in live_urls:
            task_futures.append(executor.submit(danmuMain, live_url))
        # 启动抖音弹幕线程
        douyinMain(loop)
        # task_futures.append(executor.submit(douyinMain, loop))
        for future in task_futures:
            try:
                # 当子线程中异常时，这里会重新抛出
                result = future.result()
            except Exception as e:  # 捕获子线程中的异常
                # 成功捕获异常
                print("该线程已停止 >>> main线程捕获到子线程的异常: ", e.args)
                future.result()
            else:
                print("应用程序执行完毕")
