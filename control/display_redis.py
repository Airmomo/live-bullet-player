from util import redisUtil
import time
import setting

LOOP_SEC = setting.LOOP_SEC
LIST_KEY = setting.REDIS_LIST_KEY


if __name__ == '__main__':
    """
        启动Redis服务，监听队列中等待执行的指令，可以不启动
    """
    r = redisUtil.getRedis()
    # print("开始监听弹幕消息, loop_sec =", loop_sec)
    while True:
        time.sleep(LOOP_SEC)
        print("等待执行的指令：", r.lrange(LIST_KEY, 0, -1))
