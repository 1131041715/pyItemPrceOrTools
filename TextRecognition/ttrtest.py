from aip import AipOcr
from tkinter import *
import tkinter.filedialog

""" 你的 APPID AK SK """
APP_ID = '19972433'
API_KEY = 'WCpLdAKA1gQWeW7iF376zMPa'
SECRET_KEY = 'fAMGe96Eo74yinPoSypjuHHbTaKRdTFP'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

root = tkinter.Tk()
var = tkinter.StringVar()

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def ocrImage(filename):
    print(filename)
    image = get_file_content(filename)
    res=client.handwriting(image)
    words = ''
    for item in res['words_result']:
        words += item['words']
        # print(item['words'])
    print(words)
    t.insert(1.0, words)
    
    # robot = qqai.vision.ocr.GeneralOCR(app_id, app_key)  # 通用OCR
    # item_list = []
    # words = ''
    # # 通用OCR
    # with open(filename, 'rb') as image_file:
    #     result = robot.run(image_file)
    # for key in result:
    #     if key == 'data':
    #         item_list = result[key]['item_list']
    # for n in item_list:
    #     if len(n['itemstring']) > 40:
    #         words += n['itemstring']
    #     else:
    #         words += n['itemstring'] + '\n'
    # print(words)
    # t.insert(1.0, words)


def HandwritingOCRImage(filename):
    print(filename)
    image = get_file_content(filename)
    res=client.handwriting(image)
    words = ''
    for item in res['words_result']:
        words += item['words']
        # print(item['words'])
    print(words)
    t.insert(1.0, words)


    # robot = qqai.vision.ocr.HandwritingOCR(app_id, app_key)  # 手写
    # item_list = []
    # words = ''
    # # 手写OCR
    # with open(filename, 'rb') as image_file:
    #     result = robot.run(image_file)
    # for key in result:
    #     if key == 'data':
    #         item_list = result[key]['item_list']
    # for n in item_list:
    #     if len(n['itemstring']) > 40:
    #         words += n['itemstring']
    #     else:
    #         words += n['itemstring'] + '\n'
    # print(words)
    # t.insert(1.0, words)


def xz1():
    btn.config(state=tkinter.DISABLED)  # 按钮失效
    btn1.config(state=tkinter.DISABLED)  # 按钮失效
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        l.config(text="您选择的文件是："+filename)
        ocrImage(filename)
    else:
        l.config(text="您没有选择任何文件")
    btn.config(state=tkinter.ACTIVE)  # 激活按钮
    btn1.config(state=tkinter.ACTIVE)  # 激活按钮


def xz2():
    btn.config(state=tkinter.DISABLED)  # 按钮失效
    btn1.config(state=tkinter.DISABLED)  # 按钮失效
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        l.config(text="您选择的文件是："+filename)
        HandwritingOCRImage(filename)
    else:
        l.config(text="您没有选择任何文件")
    btn.config(state=tkinter.ACTIVE)  # 激活按钮
    btn1.config(state=tkinter.ACTIVE)  # 激活按钮


# 第2步，给窗口的可视化起名字
root.title('图像识别')

# 第3步，设定窗口的大小(长 * 宽)
root.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上设定标签
l = tkinter.Label(root, text='你好！这是图像识别工具', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
l.pack()    # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();

btn = tkinter.Button(root, text="通用OCR", command=xz1)
btn.pack()
btn1 = tkinter.Button(root, text="手写体OCR", command=xz2)
btn1.pack()
t = tkinter.Text(root, height=16)
t.pack()
root.mainloop()

















# # 初始化AipFace对象
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
# # 读取图片
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
 
# image = get_file_content('IMG_2795.jpg')
# # 调用通用文字识别, 图片为本地图片
# res=client.handwriting(image)
# print(res)
 
# for item in res['words_result']:
#     print(item['words'])


# import requests

# '''
# 人脸融合
# '''

# request_url = "https://aip.baidubce.com/rest/2.0/face/v1/merge"

# params = "{\"image_template\":{\"image\":\"sfasq35sadvsvqwr5q...\",\"image_type\":\"BASE64\",\"quality_control\":\"NONE\"},\"image_target\":{\"image\":\"sfasq35sadvsvqwr5q...\",\"image_type\":\"BASE64\",\"quality_control\":\"NONE\"}}"
# access_token = '[调用鉴权接口获取的token]'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/json'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print (response.json())