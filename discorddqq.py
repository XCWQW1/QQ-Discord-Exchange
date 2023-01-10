import sys
import discord
import requests

intents = discord.Intents.default()  # 抄官方示例的 我也不知道是啥 滑稽
intents.message_content = True  # 也是抄的
client = discord.Client(intents=intents)  # 还是抄的


@client.event  # 又是抄的 (ctrl C + V yyds
async def on_message(message):  # 接收到消息触发下方代码
    if message.author == client.user:  # 如果消息发送者为BOT本身不做处理，防止死循环
        return  # 返回
    if message.channel.id == 频道ID:  # 验证是否为目标频道ID 记得改成你需要互通的频道ID
        requests.get(url='http://记得改这里啊IP:PROT你go-cqhttp的HTTPAPI地址/send_msg?group_id=要发的群号&message=[Discord]' + message.author.name + ": " + message.content)  # 通过 HTTP API 向 GO-CQHTTP 发送消息 , 详细请查阅 GO-CQHTTP 官方文档


client.run('你discord机器人的TOKEN 和 WEBHOOK是2个东西 不一样 这个教程挺多的百度吧')  # Discord 机器人的 TOKEN (这里会提示拼写错误是我没想到的
