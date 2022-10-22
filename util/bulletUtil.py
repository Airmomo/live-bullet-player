from datetime import datetime
from itertools import combinations

# 日志级别名称
LIVE_DOUYU_NAME = "Douyu"
LIVE_DOUYIN_NAME = "Douyin"
LIVE_HUYA_NAME = "Huya"
LIVE_BILIBILI_NAME = "Bilibili"
# 日志颜色 # \033[显示方式;前景色;背景色m 要输出的内容 \033[m
LIVE_DOUYU_COLOR = "31m "  # 红色
LIVE_DOUYIN_COLOR = "32m "  # 绿色
LIVE_HUYA_COLOR = "33m "  # 黄色
LIVE_BILIBILI_COLOR = "34m "  # 蓝色


def _getLiveColor(live):
    live_color = "0;0;0m "
    if live == LIVE_DOUYU_NAME:
        live_color = LIVE_DOUYU_COLOR
    elif live == LIVE_DOUYIN_NAME:
        live_color = LIVE_DOUYIN_COLOR
    elif live == LIVE_HUYA_NAME:
        live_color = LIVE_HUYA_COLOR
    elif live == LIVE_BILIBILI_NAME:
        live_color = LIVE_BILIBILI_COLOR
    return live_color


def printBullet(live, room_id, name, content):
    color_pre = "\033["
    color_set = _getLiveColor(live)
    color_tail = " \033[0m"
    start = datetime.now()
    start_time = start.strftime('%Y-%m-%d %H:%M:%S')
    header = "[" + start_time + "]" + "--" \
             + "[" + live.center(8) + "]" + "--" \
             + "[" + room_id.center(8) + "]" + " -> "
    bullet = "[" + name + "]" + "--" + "[" + content + "]"
    print_str_list = [color_pre, color_set, header, bullet, color_tail]
    print_str = "".join(print_str_list)
    print(print_str, end="\r\n")


def splitBullet(s):
    res = []
    if len(s) == 0:
        return res
    elif len(s) == 1:
        res.append(s)
        return res
    elif len(s) == 2:
        res.append(list(s))
        res.append([s])
    else:
        k = len(s) - 1
        for indexes in combinations(range(1, len(s)), k - 1):
            indexes = [0] + list(indexes) + [len(s)]  # add the edges to k-1 indexes to create k parts
            res.append([s[start:end] for start, end in zip(indexes[:-1], indexes[1:])])  # concatenate the k parts
    # 结果二维数组转一维数组
    return list(set(sum(res, [])))


def bulletInKeyList(char, key_list):
    return char in key_list


if __name__ == '__main__':
    print(splitBullet("开火"))
