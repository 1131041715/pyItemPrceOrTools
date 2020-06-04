# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import os
from time import sleep


class downloader(object):

    def __init__(self):

        self.target = 'http://lol.52pk.com/pifu/hero/'

        self.save_path = './image'

    def download(self):    
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        for i in range(1, 44):

            target = self.target+'hero_{}.shtml'.format(i)

            r = requests.get(target)
            r.encoding = r.apparent_encoding
            html = r.text
            div_bf = BeautifulSoup(html, features='html.parser')

            data_base = div_bf.find('div', class_='ListBigContent')

            lis = data_base('li')

            for li in lis:

                url = li.find('a', target='_blank')
                url = url.get('href')

                name, image_url = self.get_image_address(url)

                # self.data[name] = image_url
                
                # self.get_image(name, image_url)

                try:
                    self.get_image(name, image_url)
                except Exception:
                    continue

    def get_image_address(self, url):

        r = requests.get(url)
        r.encoding = r.apparent_encoding
        html = r.text
        div_bf = BeautifulSoup(html, features='html.parser')

        name_div = div_bf.find('div', class_='pifuIntroText pifuIntroText2')

        hero_name = name_div.find('h2').text
        skin_name = name_div.find('h1').text

        image_div = div_bf.find('div', class_='pifuIntroPic pifuIntroPic2')

        image_url = image_div.find('img')
        image_url = image_url.get('src')

        name = hero_name+'-'+skin_name
        name = name.replace('/', '')

        return name.replace(' ', ''), image_url

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


if __name__ == "__main__":

    target = downloader()
    target.download()
