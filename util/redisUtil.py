import redis

# 加载模块即初始化Redis单例对象
REDIS_PROTO = None

# Redis链接
HOST = "localhost"
PORT = 6379


def getRedis():
    global REDIS_PROTO
    if not REDIS_PROTO:
        REDIS_PROTO = redis.Redis(host=HOST, port=PORT, decode_responses=True)
    return REDIS_PROTO


def rPushBullet(list_key, char):
    global REDIS_PROTO
    REDIS_PROTO = getRedis()
    if getBulletSwitchStatus():
        return REDIS_PROTO.rpush(list_key, char) > 0
    return False


# 弹幕开关状态
BULLET_SWITCH_KEY = "bullet_switch"
SWITCH_ON_STATUS = 'on'
SWITCH_OFF_STATUS = 'off'


def getBulletSwitchStatus():
    global REDIS_PROTO
    REDIS_PROTO = getRedis()
    if REDIS_PROTO.get(BULLET_SWITCH_KEY) == SWITCH_ON_STATUS:
        return True
    return False


def setBulletSwitchStatus(status: str):
    global REDIS_PROTO
    REDIS_PROTO = getRedis()
    return REDIS_PROTO.set(BULLET_SWITCH_KEY, status) > 0


def tapBulletSwitch():
    if getBulletSwitchStatus():
        setBulletSwitchStatus(SWITCH_OFF_STATUS)
    else:
        setBulletSwitchStatus(SWITCH_ON_STATUS)
    return getBulletSwitchStatus()
