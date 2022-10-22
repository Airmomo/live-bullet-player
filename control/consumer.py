from util import redisUtil, pyAutoGuiUtil
import time
import setting


LOOP_SEC = setting.LOOP_SEC
PRESS_SEC = setting.PRESS_SEC
LIST_KEY = setting.REDIS_LIST_KEY
GAME_KEY_MAP = setting.GAME_KEY_MAP


def consumerMain():
    """
        启动Redis服务，监听队列中的指令，并依次出列执行
        该服务启动后才可以执行按键指令操作
    """
    control_redis = redisUtil.getRedis()
    # print("开始监听弹幕消息, loop_sec =", loop_sec)
    while True:
        if redisUtil.getBulletSwitchStatus():
            name = control_redis.lpop(LIST_KEY)
            if not name:
                continue
            # 如果处理所有水友发送的全部弹幕指令，一定会存在消费不过来的问题。
            # 所以每次只取出一个指令，然后把list清空，也就是这个时间窗口内其他弹幕都扔掉！
            control_redis.delete(LIST_KEY)
            print("执行指令：" + name)
            # 执行指令
            key_name = GAME_KEY_MAP[name]
            if key_name == "mouseLeft":
                pyAutoGuiUtil.mouseLeftClick()
            elif key_name == "mouseRight":
                pyAutoGuiUtil.mouseRightClick()
            else:
                pyAutoGuiUtil.tap(key_name, PRESS_SEC)
            time.sleep(LOOP_SEC)


if __name__ == '__main__':
    consumerMain()
