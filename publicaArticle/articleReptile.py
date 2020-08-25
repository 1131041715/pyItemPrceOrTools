#-*- coding:UTF-8 -*-
import json
import time
import pdfkit

import requests

base_url = 'https://mp.weixin.qq.com/mp/profile_ext'


# 这些信息不能抄我的，要用你自己的才有效
headers = {
    'Connection': 'keep - alive',
    'Accept': '* / *',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/2.4.2(0x12040210) Chrome/39.0.2171.95 Safari/537.36 NetType/WIFI WindowsWechat',
    'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzUzNzYzMzE2Mg==&scene=124&uin=MTE4Njk5MjA4MQ%3D%3D&key=9ae93b5dab71cae0af190083b0690741c14ef287221ce7f6be33c40964ca2867d3bd49a812d63c8cd70585d6ea87fe9b0f62b41f9bdf4950998183c032bad318d705385b98a07153c5127c66e8ee8a43b3d3cc4a7adc5b13d81671f10b199ae4145cb3e5c423d7f168d9319fbb8956c6d69c40b145f5320ddeb1005a2bdd2f3a&devicetype=iMac+MacBookPro12%2C1+OSX+OSX+10.15.6+build(19G2021)&version=12040210&lang=zh_CN&nettype=WIFI&a8scene=1&fontScale=100&pass_ticket=Zg%2Fvde5BIJNjf4UCKP3poDOEGIl8ZlcMp3EA9bp7lKSFHj8F7TAzlSDBV6UQIrDR',
    'Accept-Encoding': 'br, gzip, deflate'
}

cookies = {
    'devicetype': 'iMacMacBookPro121OSXOSX10.15.6build(19G2021)',
    'lang': 'zh_CN',
    'pass_ticket': 'Zg/vde5BIJNjf4UCKP3poDOEGIl8ZlcMp3EA9bp7lKSFHj8F7TAzlSDBV6UQIrDR',
    'version': '12040210',
    'wap_sid2': 'CNGfgLYEEooBeV9IS2FZWDZjbWxwR0E2UEFkM0xxd0drV3dEM0dkT1ZnYjkzaklfM0t6OHZEeXpLUTBhRWl2YnFaSzNFQXNod0Y0Mi16bFFqQ2xpN2pSRWxmZ2piaG9aSGZLQTV2RWdDRk00a3dsZlNNQmN6YnF3ZnBSMzVOempzUld1bXc0U1JZZXVCQVNBQUF+MN7v3vkFOA1AlU4=',
    'wxuin': '1186992081'
}



def get_params(offset):
    params = {
        'action': 'getmsg',
        '__biz': 'MzUzNzYzMzE2Mg==',
        'f': 'json',
        'offset': '{}'.format(offset),
        'count': '10',
        'is_ok': '1',
        'scene': '124',
        'uin': 'MTE4Njk5MjA4MQ==',
        'key': '9ae93b5dab71cae0af190083b0690741c14ef287221ce7f6be33c40964ca2867d3bd49a812d63c8cd70585d6ea87fe9b0f62b41f9bdf4950998183c032bad318d705385b98a07153c5127c66e8ee8a43b3d3cc4a7adc5b13d81671f10b199ae4145cb3e5c423d7f168d9319fbb8956c6d69c40b145f5320ddeb1005a2bdd2f3a',
        'pass_ticket': 'Zg/vde5BIJNjf4UCKP3poDOEGIl8ZlcMp3EA9bp7lKSFHj8F7TAzlSDBV6UQIrDR',
        'appmsg_token': '1074_uiwaafWldyKzptUD5cyJtCnFv55ftq5tiCOykA~~',
        'x5': '0',
        'f': 'json',
    }

    return params


def get_list_data(offset):
    res = requests.get(base_url, headers=headers, params=get_params(offset), cookies=cookies)
    data = json.loads(res.text)
    can_msg_continue = data['can_msg_continue']
    next_offset = data['next_offset']

    general_msg_list = data['general_msg_list']
    list_data = json.loads(general_msg_list)['list']

    for data in list_data:
        try:
            print(data['app_msg_ext_info'] is not None) #data['app_msg_ext_info']['copyright_stat'] == 11
            if data['app_msg_ext_info'] is not None :
                msg_info = data['app_msg_ext_info']
                title = msg_info['title']
                content_url = msg_info['content_url']
                # 自己定义存储路径
                out_path = 'publicaArticle/arrttiFiles/'+ title +'.pdf'
                # print(out_path)
                pdfkit.from_url(content_url, out_path)
                print('获取到原创文章：%s ： %s' % (title, content_url))
        except:
            print('不是图文')

    if can_msg_continue == 1:
        time.sleep(1)
        get_list_data(next_offset)


if __name__ == '__main__':

    # out_path = 'publicaArticle/arrttiFiles/'+'测试存储pdf'+'.pdf'
    # pdfkit.from_url('https://www.jianshu.com/p/ec11e3b1b46e', out_path)
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    # path_wkthmltopdf = '/usr/local/bin/wkhtmltopdf'
    # config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    # pdfkit.from_url(url, to_file, configuration=config)
    # pdfkit.from_url('http://google.com', out_path,configuration=config)
    # print('完成')

    get_list_data(0)