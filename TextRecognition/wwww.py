from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '19972433'
API_KEY = 'WCpLdAKA1gQWeW7iF376zMPa'
SECRET_KEY = 'fAMGe96Eo74yinPoSypjuHHbTaKRdTFP'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
image = get_file_content('/Users/any/Desktop/IMG_2795.jpg')
# 调用通用文字识别, 图片为本地图片
res=client.handwriting(image)
print(res)
 
for item in res['words_result']:
    print(item['words'])