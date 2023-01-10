import json


def wsjson(JSL): # json 解析 大部分代码源自菜鸟 详细就去看菜鸟 python3 json 吧 懒得解释了 滑稽 这里第一层对象都可以解析，只要输入JSL即可
    def json_jx(Json_J, Json_L):
        data2 = json.loads(Json_J)
        print(data2[Json_L])
        with open('discord1.txt', 'w', encoding='utf-8') as f1:
            f1.write(data2[Json_L])
            f1.close()

    f = open('qq.txt', 'r', encoding='utf-8')
    json_jx(Json_J=f.read(), Json_L=JSL)
    f.close()


def jsonname():  # json 解析 单独解析QQ名片的应为QQ名片在一个对象内所以分开走了 只不过这样子会导致没有修改名片就默认名字的话发到discord是空的 应为默认加群不改名片是没有群名片的
    def json_jx(Json_J):
        data2 = json.loads(Json_J)
        print(data2['sender']['card'])
        with open('discord.txt', 'w', encoding='utf-8') as f2:
            f2.write(data2['sender']['card'])
            f2.close()

    f = open('qq.txt', 'r', encoding='utf-8')
    json_jx(Json_J=f.read())
    f.close()
