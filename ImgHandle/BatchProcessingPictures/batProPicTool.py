
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox 

import numpy as np
import cv2
import os
from PIL import Image, ImageTk
import math


file_dir = ''
dataset_dir = ''
output_dir = ''

image = object()
hlsImg = object()
hlsCopy = object()

# 滑动条最大值
MAX_VALUE = 100
# 滑动条最小值
MIN_VALUE = 0


def loadImage(hlsCopy):
    global save_lsImg
    show_lsImg = cv2.cvtColor(hlsCopy, cv2.COLOR_HLS2BGR)
    show_lsImg = show_lsImg * 255
    show_lsImg = show_lsImg.astype(np.uint8)
    #顺序不能乱调整
    save_lsImg = show_lsImg
    show_lsImg = cv2.cvtColor(show_lsImg,cv2.COLOR_BGR2RGB)
    
    Rgb_Img = Image.fromarray(show_lsImg)
    
    #图片大小更改
    Source_Img_Height = show_lsImg.shape[0]
    Source_Img_Width = show_lsImg.shape[1]
    #缩放比例
    scalingratio = Source_Img_Height / Source_Img_Width
    print(scalingratio)
    x = root.winfo_screenwidth() * 0.3
    #获取当前屏幕的宽
    y = root.winfo_screenheight()
    print(x)
    Img_realHeight = int(x)
    Img_realWidth = round(Img_realHeight / scalingratio) 
    Rgb_Img = Rgb_Img.resize((Img_realWidth , Img_realHeight), Image.ANTIALIAS)
    Rgb_Img = ImageTk.PhotoImage(Rgb_Img)
    lab_Image.configure(image=Rgb_Img)
    lab_Image.image = Rgb_Img

def ocrImage(filename):
    print(filename)
    global file_dir
    file_dir = filename
    # 加载图片 读取彩色图像归一化且转换为浮点型
    image = cv2.imread(file_dir, cv2.IMREAD_COLOR).astype(np.float32) / 255.0
    # 颜色空间转换 BGR转为HLS
    hlsImg = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    # 复制原图
    hlsCopy = np.copy(hlsImg)
    loadImage(hlsCopy)
    
def btnActionSelectModelPic():
    btnSelectM.config(state=tkinter.DISABLED)  # 按钮失效
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        lab_1.config(text="您选择的文件是："+filename)
        sl_lightness.set(0)
        sl_saturation.set(0)
        ocrImage(filename)
    else:
        lab_1.config(text="您没有选择任何文件")
    btnSelectM.config(state=tkinter.ACTIVE)  # 激活按钮

#亮度函数回调
def lightnessAdjustment(text):
    print('text = ', text)
    print('v_saturation = ', v_saturation.get())
    satura = v_saturation.get()
    if len(file_dir) == 0:
        tkinter.messagebox.showinfo('提示','请选择样图')
        return
    print('text = ', text)
    image = cv2.imread(file_dir, cv2.IMREAD_COLOR).astype(np.float32) / 255.0
    hlsImg = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)     
    hlsCopy = np.copy(hlsImg)
    # 得到 lightness 和 saturation 的值
    lightness = float(text)
    saturation = float(satura)
    # 调整亮度
    hlsCopy[:, :, 1] = (1.0 + lightness / float(MAX_VALUE)) * hlsCopy[:, :, 1]
    hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1
    # 饱和度
    hlsCopy[:, :, 2] = (1.0 + saturation / float(MAX_VALUE)) * hlsCopy[:, :, 2]
    hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1
    loadImage(hlsCopy)

#饱和度调整回调
def saturationAdjustment(text):
    print('text = ', text)
    print('v_lightness = ', v_lightness.get())
    light = v_lightness.get()
    if len(file_dir) == 0:
        tkinter.messagebox.showinfo('提示','请选择样图')
        return
    print('text = ', text)
    image = cv2.imread(file_dir, cv2.IMREAD_COLOR).astype(np.float32) / 255.0
    hlsImg = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)     
    hlsCopy = np.copy(hlsImg)
    # 得到 lightness 和 saturation 的值
    lightness = float(light)
    saturation = float(text)
    # 调整亮度
    hlsCopy[:, :, 1] = (1.0 + lightness / float(MAX_VALUE)) * hlsCopy[:, :, 1]
    hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1
    # 饱和度
    hlsCopy[:, :, 2] = (1.0 + saturation / float(MAX_VALUE)) * hlsCopy[:, :, 2]
    hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1
    loadImage(hlsCopy)

#保存单张图片
def saveSignlPic():
    save_signlbtn1.config(state=tkinter.DISABLED)  # 按钮失效
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        lab_1.config(text="您选择的文件是："+filename)
        strlist = file_dir.split('/')
        print(strlist)	
        output_img_path = filename +'/' + strlist[-1]
        if cv2.imwrite(output_img_path, save_lsImg) is not None:
            tkinter.messagebox.showinfo('提示','保存成功')
        # cv2.imwrite(output_img_path, save_lsImg)
        # HandwritingOCRImage(filename)
    else:
        lab_1.config(text="您没有选择任何文件夹")
    save_signlbtn1.config(state=tkinter.ACTIVE)  # 激活按钮

#保存单张图片
def saveSignlPic():
    save_signlbtn1.config(state=tkinter.DISABLED)  # 按钮失效
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        lab_1.config(text="您选择的文件是："+filename)
        strlist = file_dir.split('/')
        print(strlist)	
        output_img_path = filename +'/' + strlist[-1]
        if cv2.imwrite(output_img_path, save_lsImg) is not None:
            tkinter.messagebox.showinfo('提示','保存成功')
        # cv2.imwrite(output_img_path, save_lsImg)
        # HandwritingOCRImage(filename)
    else:
        lab_1.config(text="您没有选择任何文件夹")
    save_signlbtn1.config(state=tkinter.ACTIVE)  # 激活按钮

#选择目标文件夹
def inputFloderSelect():
    imgs_inputBtn1.config(state=tkinter.DISABLED)  # 按钮失效
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        imgs_inputBtn1.config(text="您选择的目标文件夹是："+filename)
        global dataset_dir
        dataset_dir = filename
        
    else:
        imgs_inputBtn1.config(text="请选择目标文件夹")
    imgs_inputBtn1.config(state=tkinter.ACTIVE)  # 激活按钮

#选择保存文件夹
def outputFloderSelect():
    imgs_outputBtn1.config(state=tkinter.DISABLED)  # 按钮失效
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        imgs_outputBtn1.config(text="您选择的保存文件是："+filename)
        global output_dir
        output_dir = filename
    else:
        imgs_outputBtn1.config(text="请选择保存文件夹")
    imgs_outputBtn1.config(state=tkinter.ACTIVE)  # 激活按钮



#批量处理回调
def update(input_img_path, output_img_path, lightness, saturation):
    """
    用于修改图片的亮度和饱和度
    :param input_img_path: 图片路径
    :param output_img_path: 输出图片路径
    :param lightness: 亮度
    :param saturation: 饱和度
    """
    # 加载图片 读取彩色图像归一化且转换为浮点型
    image = cv2.imread(input_img_path, cv2.IMREAD_COLOR).astype(np.float32) / 255.0

    # 颜色空间转换 BGR转为HLS
    hlsImg = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    # 1.调整亮度（线性变换)
    hlsImg[:, :, 1] = (1.0 + lightness / float(MAX_VALUE)) * hlsImg[:, :, 1]
    hlsImg[:, :, 1][hlsImg[:, :, 1] > 1] = 1
    # 饱和度
    hlsImg[:, :, 2] = (1.0 + saturation / float(MAX_VALUE)) * hlsImg[:, :, 2]
    hlsImg[:, :, 2][hlsImg[:, :, 2] > 1] = 1
    # HLS2BGR
    lsImg = cv2.cvtColor(hlsImg, cv2.COLOR_HLS2BGR) * 255
    lsImg = lsImg.astype(np.uint8)
    cv2.imwrite(output_img_path, lsImg)

def startHandleAction():
    if len(dataset_dir) == 0:
        tkinter.messagebox.showinfo('提示','请选择目标文件夹')
        return
    if len(output_dir) == 0:
        tkinter.messagebox.showinfo('提示','请选择保存文件夹')
        return
    if dataset_dir == output_dir:
        tkinter.messagebox.showinfo('提示','目标文件夹与保存文件夹一直，重新选择保存文件夹')
        return 

    # 获得需要转化的图片路径并生成目标路径
    image_filenames = [(os.path.join(dataset_dir, x), os.path.join(output_dir, x))
                    for x in os.listdir(dataset_dir)]
    light = v_lightness.get()
    lightness = float(light)
    satura = v_saturation.get()
    saturation = float(satura)

    inventory = ["jpg", "JPG", "PNG", "png", "JPEG", "jpeg"]
    # sufStr = 'jpg'
    for filepath in image_filenames:
        inputPath = filepath[0]
        suf = os.path.splitext(inputPath)[-1][1:]
        print(suf)
        if suf in inventory: #sufStr.find(suf):
            print(inputPath)
            update(filepath[0], filepath[1], lightness, saturation)
        # else:
        #     tkinter.messagebox.showinfo('提示','%s文件后缀为非照片(照片缀为%s)' % (inputPath,sufStr))
        #     return
    # loading.close
    tkinter.messagebox.showinfo('提示','处理完成')
    print('处理完成')




root = tkinter.Tk()
var = tkinter.StringVar()
# 第2步，给窗口的可视化起名字
root.title('照片处理')

wind_Width = root.winfo_screenwidth() - 20 * 2
    #获取当前屏幕的宽
wind_Height = root.winfo_screenheight() - 30 * 2
    #获取当前屏幕的高
# print(scr_Width,scr_Height)
# 第3步，设定窗口的大小(长 * 宽)
root.geometry('%dx%d+%d+%d' % (wind_Width,wind_Height,20,0))  # 这里的乘是小x '300x250+500+240' 加号设置位置，第一个为x，第二个为y，可以设置为负
# 第4步，在图形界面上设定标签
lab_1 = tkinter.Label(root, text='单图调整，可做为批量处理模板', font=('Arial', 12), width=int(wind_Width), height=2)
lab_1.pack() 

btnSelectM = tkinter.Button(root, text="请选择样图", command=btnActionSelectModelPic)
# btnSelectM.place(x=0,y=0)
btnSelectM.pack()

global lab_Image
lab_Image = tkinter.Label(root,font=('Arial', 12))
lab_Image.pack()

global sl_lightness
v_lightness = StringVar()
sl_lightness=Scale(
    root,
    from_= MIN_VALUE,  # 设置最大值
    to = MAX_VALUE,  # 设置最小值
    length = 200,
    resolution = 1,  # 设置步距值
    orient = HORIZONTAL,  # 设置水平方向
    variable=v_lightness,  # 绑定变量
    label = '亮度:',  # 设置标签值
    command = lightnessAdjustment  # 设置回调函数
    )
'''7.设置/取得Scale的值'''
sl_lightness.set(0)      #将Scale的值设置为50
# print('tttttt' , sl_lightness.get())  #打印当前的Scale的值
sl_lightness.pack()


global sl_saturation
v_saturation = StringVar()
sl_saturation=Scale(
    root,
    from_= MIN_VALUE,  # 设置最大值
    to = MAX_VALUE,  # 设置最小值
    length = 200,
    resolution = 1,  # 设置步距值
    orient = HORIZONTAL,  # 设置水平方向
    variable = v_saturation,  # 绑定变量
    label = '饱和度:',  # 设置标签值
    command = saturationAdjustment  # 设置回调函数
    )
'''7.设置/取得Scale的值'''
sl_saturation.set(0)      #将Scale的值设置为50
# print(sl_lightness.get())  #打印当前的Scale的值
sl_saturation.pack()

save_signlbtn1 = tkinter.Button(root, text="保存单张", command=saveSignlPic)
save_signlbtn1.pack()

lab_2 = tkinter.Label(root, text='可处理文件后缀(jpg、JPG、PNG、png、JPEG、jpeg)', font=('Arial', 12), width=int(wind_Width), height=2)
lab_2.pack() 

imgs_inputBtn1 = tkinter.Button(root, text="选择目标文件夹", command=inputFloderSelect)
imgs_inputBtn1.pack()

imgs_outputBtn1 = tkinter.Button(root, text="选择保存文件夹", command=outputFloderSelect)
imgs_outputBtn1.pack()

startHandleBtn1 = tkinter.Button(root, text="开始批处理", command=startHandleAction)
startHandleBtn1.pack()


root.mainloop()
