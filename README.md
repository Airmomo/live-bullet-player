# live-bullet-player
获取直播实时弹幕，将弹幕内容转为键盘指令，通过PyAutoGUI执行指令操作电脑
# 支持平台
19 个直播平台的弹幕获取：抖音直播、斗鱼直播、虎牙直播、哔哩哔哩直播、快手直播、火猫直播、企鹅电竞、花椒直播、映客直播、网易 CC 直播、酷狗直播、龙珠直播、PPS 奇秀、搜狐千帆、战旗直播、来疯直播、网易 LOOK 直播、AcFun 直播、艺气山直播。
# 扩展功能
- 增加获取抖音弹幕并支持弹幕指令操作
- 增加多线程和异常捕获，支持同时获取多个直播间的弹幕
- 弹幕内容分割功能，原项目只能通过分割后的单个字符来映射指令
  - 存在缺陷：用户发送任意包含单一字符的弹幕就能触发多次操作指令
  - 本项目完善该功能：
    - 对弹幕内容重复指令进行去重
    - 支持使用字符串映射指令
  - 在`setting.py`中统一了一些变量：
    - `GAME_KEY_MAP`：弹幕指令映射表
    - `KEY_LIST`：允许触发指令的弹幕字符串，必须先在`GAME_KEY_MAP`中定义映射关系
- 提供`util`层封装相关操作
- bulletUtil：输出弹幕信息格式化等功能
- redisUtil：单例化Redis连接对象等功能
- pyAutoGuiUtil：封装PyAutoGUI操作等功能
# 使用方式
## 使用步骤
- 安装Python3.9和项目依赖
- 安装并启动Redis服务
- 在`setting.py`中设置好相应的全局变量
- 修改`main.py`中变量`live_urls`待获取弹幕的直播间地址列表
- 运行`main.py`和`control/consumer.py`
- 可以通过自定义的热键（默认`F12`）来控制是否弹幕操作电脑
## 抖音直播的弹幕获取的方式
- 在`danmu/douyin/main.py`中配置WebSocket的地址和端口
- 直接运行`danmu/douyin/main.py`启动WebSocket服务
- 用浏览器进入待获取弹幕的抖音直播间
- 按F12进入开发者模式
- 在`danmu/douyin/barrage.js`中配置相同的WebSocket的地址和端口
- 创建并执行`danmu/douyin/barrage.js`脚本，启动WebSocket服务
- 通过js脚本将弹幕消息封装为json数据对象，通过WebSocket传递json数据对象到服务端解析
# 实现原理
Fork的Github项目
```
https://github.com/wbt5/real-url
```
- 获取个大平台直播的实时弹幕
```
https://github.com/qqxx6661/live_comment_control_stream
```
- 接收弹幕指令并控制电脑操作
- 使用Redis存储消息队列
- 消费者接受消息，将弹幕内容转为键盘指令
- PyAutoGUI执行指令操作电脑
```
https://github.com/XiaoXinYo/Live-Barrage
```
- 提供抓取抖音等平台弹幕的js文件以及运行示例
# 使用方法
安装requirements.txt依赖
```
pip install -r requirements.txt
```
下载并安装Redis
```
https://github.com/MicrosoftArchive/redis/releases
```
修改main.py和consumer.py里的变量
```
live_url：直播间地址
key_list：允许点击的按键列表
```
打开bilibili并用obs推流 
```
https://link.bilibili.com/p/center/index#/my-room/start-live
```
依次启动
```
main.py
display_redis.py
consumer.py
```
打开游戏，等待接收弹幕执行按键指令