# 监控的直播间地址
# 抖音直播不在这里填入地址，需要自行到danmu/douyin/main.py中进行配置
LIVE_URLS = {
    "https://live.bilibili.com/1823532",
    "https://www.douyu.com/11198626",
    "https://www.huya.com/28062122",
}
# 弹幕指令消费者的循环周期，周期越短，丢失的弹幕指令越多，但周期越长，将导致短时间内大量弹幕占用内存
LOOP_SEC = 0.2
# 按键按下间隔
PRESS_SEC = 0.25
# 按键指令队列key
REDIS_LIST_KEY = 'bullet'
# 举例：游戏按键指令列表
PUBG_KEY_LIST = ('w', 'a', 's', 'd', 'f', '蹲', '趴', '跳', '开火', '开镜')
# 允许执行的按键指令名称（必须在游戏按键映射存在）
KEY_LIST = PUBG_KEY_LIST
# 弹幕文本与按键映射
GAME_KEY_MAP = {
    "a": 'a',
    "b": 'b',
    "c": 'c',
    "d": 'd',
    "e": 'e',
    "f": 'f',
    "g": 'g',
    "h": 'h',
    "i": 'i',
    "j": 'j',
    "k": 'k',
    "l": 'l',
    "m": 'm',
    "n": 'n',
    "o": 'o',
    "p": 'p',
    "q": 'q',
    "r": 'r',
    "s": 's',
    "t": 't',
    "u": 'u',
    "v": 'v',
    "w": 'w',
    "x": 'x',
    "y": 'y',
    "z": 'z',
    "蹲": 'c',
    "趴": 'z',
    "跳": "space",
    "开火": "mouseLeft",
    "开镜": "mouseRight",
}
