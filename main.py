# coding=UTF-8
import datetime
import json
import random
import requests

import push

# 加载数据文件
with open('./DATA', 'r', encoding='utf8') as fp:
    datas = eval(fp.read())

for data in datas:
    sub_data = data[0]
    cent = data[1]['cent']
    pushKey = data[1]['pushKey']
    appToken = data[1]['appToken']
    uid = data[1]['uid']

    # 随机体温
    if not sub_data['tiwen']:
        sub_data['tiwen'] = random.choice(cent)
    if not sub_data['tiwen1']:
        sub_data['tiwen1'] = random.choice(cent)
    if not sub_data['tiwen2']:
        sub_data['tiwen2'] = random.choice(cent)

    # 发送日报信息
    url = "https://yqdwxx.sau.edu.cn/ADDJKTB"
    res = requests.post(url=url, json=sub_data)

    # 推送通知
    pushbody = f'学工号: {sub_data["userid"]}\n姓名: {sub_data["xingming"]}\n手机号: {sub_data["shoujihao"]}\n单位院系: {sub_data["dwyx"]}\n当前所在省份: {sub_data["shengfen"]}\n所在城市: {sub_data["chengshi"]}\n14日内是否有中高风险地区旅居史、接触史: {sub_data["ljsjcs"]}\n是否按照要求向学校、社区及时上报: {sub_data["sqsb"]}\n是否离沈: {sub_data["sfls"]}\n离沈去向: {sub_data["lsqx"]}\n是否隔离观察: {sub_data["sfgl"]}\n是否身体有疑似典型症状: {sub_data["sfys"]}\n是否发热: {sub_data["sffr"]}\n其他信息: {sub_data["other"]}\n体温(早): {sub_data["tiwen"]}\n体温(中): {sub_data["tiwen1"]}\n体温(晚): {sub_data["tiwen2"]}'
    code = res.status_code
    if code == 200:
        resbody = json.loads(res.text)
        if resbody['status'] == 'OK':
            pushmessage = ["疫情填报成功！" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                           f"**填报信息**\n---\n```\n{pushbody}\n```"]
            exit_code = 0
        else:
            pushmessage = ["疫情填报失败！" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                           f"**请检查配置并手动填报！**\n\n**服务器返回信息：{res.text}**\n\n**填报信息**\n---\n```\n{pushbody}\n```"]
            exit_code = -1
    else:
        pushmessage = ["疫情填报失败！服务器连接错误！" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), "**请检查服务器地址！**"]
        exit_code = -1
    print(pushmessage[0], '\n', res.text, '\n')
    if appToken:
        push.wxpusher(apptoken=appToken, content=pushmessage[1], summary=pushmessage[0], uids=uid)
        print('具体信息请查看WxPusher内推送\n')

    if pushKey:
        push.pushdeer('', pushKey, pushmessage[0], pushmessage[1])
        print('具体信息请查看pushdeer内推送\n')
