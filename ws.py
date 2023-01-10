import requests
import asyncio
import websockets
import re
from json_jx import wsjson
from json_jx import jsonname


def qqd():  # 往Discord发消息的
    WEBHOOK_URL = '写你discord频道的WEBHOOK链接'  # discord 频道 WEBHOOK 链接 服务器设置>整合>webhook

    f = open('discord1.txt', 'r', encoding='utf-8')  # 群名片
    f1 = open('discord.txt', 'r', encoding='utf-8')  # 群消息
    a = f.read()
    b = f1.read()
    requests.post(WEBHOOK_URL, {"content": "[QQ] [" + b + "] : " + a})  # QQ 消息发送到 Discord


async def hello(uri):  # 将 GO-CQHTTP WS 给的JSON处理为需要的
    async with websockets.connect(uri) as websocket:
        while True:
            WsText = await websocket.recv()  # 获取ws链接后返回的信息
            if "nickname" in WsText:  # json中没有群名片则不做处理
                with open('qq.txt', 'w', encoding='utf-8') as f:  # 打开文本 写入json 后 送到json_jx 进行json解析处理
                    f.write(WsText)
                    f.close()
                jsonname()  # 调用解析名片
                wsjson(JSL='message')  # 调用解析消息
                qqd()  # 调用发送到discord


asyncio.get_event_loop().run_until_complete(hello('ws://IP:PORT'))  # 正向WS链接 注意修改自己的IP和端口
