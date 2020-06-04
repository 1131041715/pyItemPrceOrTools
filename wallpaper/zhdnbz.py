# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import os
from time import sleep


class downloader(object):

    def __init__(self):

        self.target = 'https://www.zhihu.com/question/267536123/answer/383320956'

        self.save_path = './image'

    def download(self):    
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        r = requests.get(self.target, headers=headers,cookies=cookies)
        r.encoding = "utf-8"
        html = r.text
        div_bf = BeautifulSoup(html, features='lxml')

        for ul in div_bf.find_all('figure'):
            imgTmp = ul.find('img',class_='origin_image zh-lightbox-thumb lazy')
            image_url = imgTmp['data-original']
            name = image_url.strip().split('/')[-1]
            print(name)

            try:
                self.get_image(name, image_url)
            except Exception:
                continue


    def get_image(self, name, url):

        sleep(0.2)

        try:

            r = requests.get(url)
            save_path = os.path.join(self.save_path, name+'.jpg')

            if not os.path.exists(save_path):

                image = r.content

                with open(save_path, 'wb') as f:
                    f.write(image)

                print('{}保存成功'.format(save_path))
            else:

                print('{}已存在'.format(save_path))        
        except Exception as e:

            print('{}保存失败'.format(save_path), e)


# 需要F12查看属性 最好全部替换
headers = {
    'Host': 'www.zhihu.com',
    'method': 'GET',
    'path': '/api/v4/members/sizhuren/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding': 'utf-8',
    'accept-language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'cache-control': 'max-age=0',
    # 'cookie':  'SESSIONID=wY0iP4cXwQxQpugo4WTPqldFMatQ6ByXEbGgBPbqFB6; JOID=UF8XB05vJ78lwi0gQWklY_4_n3VQSQGaB-YLBmRLAZkA4AkGZwWgaH3ALSNGOiPD6DV0eaOQ2oufmZs0UdS1q0U=; osd=UVAQCkJuKLgoziwvRmQpYvE4knlRRgaXC-cEAWlHAJYH7QUHaAKtZHzPKi5KOyzE5Tl1dqSd1oqQnpY4UNuypkk=; _zap=27807c3b-dd5d-4fbc-846e-1ef76065779c; d_c0="ADBQ-DIYMRGPTqPNJhFqbk9DYxFrsBGDlxQ=|1588132454"; _ga=GA1.2.680938254.1588132457; capsion_ticket="2|1:0|10:1588840520|14:capsion_ticket|44:YTk1MjlhYzA5YWUzNDcyMGE4YWJlYWU4YzA1M2MxYjk=|41d2b9605de9969f9c4848b4159455a1d32f0e8da41ecc2826a4e0f14f3445cc"; q_c1=50df568e51ea4ad88ee4526517d4c4a2|1588138884000|1588138884000; r_cap_id="N2I0NzU2YjdjMmUwNDk2YWI4ZTg0NTUxNDA4YjRjNmY=|1588138884|34fe6faaea54e3c7c111bbd6570337efd7e6e9d4"; cap_id="MmYwNTQwMWZlODFkNDk3ZGI2NDY0ZTMzNzEzMGYyMTc=|1588138884|5699c94bf29e05f3efa34773d18a6d0b02bacbe8"; l_cap_id="OTAyZGU1MDU2YmUzNDRlYTk4MjQ4MzBhYjYyOTlmNTc=|1588138884|6e97a4da369681ed3c01c8ed175792accfff4d81"; __utma=51854390.680938254.1588132457.1588138890.1588138890.1; __utmz=51854390.1588138890.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20200429=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1590571894,1590627517,1590649182,1590723672; z_c0="2|1:0|10:1588840562|4:z_c0|92:Mi4xLXNQc0JBQUFBQUFBTUZENE1oZ3hFU2NBQUFDRUFsVk5jbFhiWGdCRUE4QUlYUFJjeUZuN3dsUnpXYXhiV3ZUOTFn|8bcb7747a6575faeb48ca200f3365dac9c6fa989ade2508d7b35f6cf289309cf"; tst=r; _gid=GA1.2.1475999957.1590385492; _xsrf=b55d66cf-6557-4dd5-aedf-d5ffd567a0be; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1590724427|1590723668; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1590724260',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0'
}



cookies = {
    "__utma":"51854390.680938254.1588132457.1588138890.1588138890.1",
    "__utmv":"51854390.000--|3=entry_date=20200429=1",
    "__utmz":"51854390.1588138890.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
    "_ga":"GA1.2.680938254.1588132457",
    "_gid":"GA1.2.1475999957.1590385492",
    "_xsrf":"b55d66cf-6557-4dd5-aedf-d5ffd567a0be",
    "_zap":"27807c3b-dd5d-4fbc-846e-1ef76065779c",
    "cap_id":"MmYwNTQwMWZlODFkNDk3ZGI2NDY0ZTMzNzEzMGYyMTc=|1588138884|5699c94bf29e05f3efa34773d18a6d0b02bacbe8",
    "capsion_ticket":"2|1:0|10:1588840520|14:capsion_ticket|44:YTk1MjlhYzA5YWUzNDcyMGE4YWJlYWU4YzA1M2MxYjk=|41d2b9605de9969f9c4848b4159455a1d32f0e8da41ecc2826a4e0f14f3445cc",
    "d_c0":"ADBQ-DIYMRGPTqPNJhFqbk9DYxFrsBGDlxQ=|1588132454",
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49":"1590724260",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49":"1590571894,1590627517,1590649182,1590723672",
    "JOID":"UF8XB05vJ78lwi0gQWklY_4_n3VQSQGaB-YLBmRLAZkA4AkGZwWgaH3ALSNGOiPD6DV0eaOQ2oufmZs0UdS1q0U=",
    "KLBRSID":"d6f775bb0765885473b0cba3a5fa9c12|1590724427|1590723668",
    "l_cap_id":"OTAyZGU1MDU2YmUzNDRlYTk4MjQ4MzBhYjYyOTlmNTc=|1588138884|6e97a4da369681ed3c01c8ed175792accfff4d81",
    "osd":"UVAQCkJuKLgoziwvRmQpYvE4knlRRgaXC-cEAWlHAJYH7QUHaAKtZHzPKi5KOyzE5Tl1dqSd1oqQnpY4UNuypkk=",
    "q_c1":"50df568e51ea4ad88ee4526517d4c4a2|1588138884000|1588138884000",
    "r_cap_id":"N2I0NzU2YjdjMmUwNDk2YWI4ZTg0NTUxNDA4YjRjNmY=|1588138884|34fe6faaea54e3c7c111bbd6570337efd7e6e9d4",
    "SESSIONID":"wY0iP4cXwQxQpugo4WTPqldFMatQ6ByXEbGgBPbqFB6",
    "tst":"r",
    "z_c0":"2|1:0|10:1588840562|4:z_c0|92:Mi4xLXNQc0JBQUFBQUFBTUZENE1oZ3hFU2NBQUFDRUFsVk5jbFhiWGdCRUE4QUlYUFJjeUZuN3dsUnpXYXhiV3ZUOTFn|8bcb7747a6575faeb48ca200f3365dac9c6fa989ade2508d7b35f6cf289309cf"
}

if __name__ == "__main__":
    target = downloader()
    target.download()
