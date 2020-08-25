import numpy as np
import cv2
import os

file_dir = r'ImgHandle/9987443.JPG'
# 加载图片 读取彩色图像归一化且转换为浮点型
image = cv2.imread(file_dir, cv2.IMREAD_COLOR).astype(np.float32) / 255.0

# 颜色空间转换 BGR转为HLS
hlsImg = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

# 滑动条最大值
MAX_VALUE = 100
# 滑动条最小值
MIN_VALUE = 0

# 调节饱和度和亮度的窗口
cv2.namedWindow("lightness and saturation", cv2.WINDOW_GUI_NORMAL)

# 创建滑动块
cv2.createTrackbar("lightness", "lightness and saturation",
                    MIN_VALUE, MAX_VALUE, lambda x:x)
cv2.createTrackbar("saturation", "lightness and saturation",
                    MIN_VALUE, MAX_VALUE, lambda x:x)

# 调整饱和度和亮度
while True:
    print('11111')
    # 复制原图
    hlsCopy = np.copy(hlsImg)
    # 得到 lightness 和 saturation 的值
    lightness = cv2.getTrackbarPos('lightness', 'lightness and saturation')
    saturation = cv2.getTrackbarPos('saturation', 'lightness and saturation')
    # 调整亮度
    hlsCopy[:, :, 1] = (1.0 + lightness / float(MAX_VALUE)) * hlsCopy[:, :, 1]
    hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1
    # 饱和度
    hlsCopy[:, :, 2] = (1.0 + saturation / float(MAX_VALUE)) * hlsCopy[:, :, 2]
    hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1
    # HLS2BGR
    lsImg = cv2.cvtColor(hlsCopy, cv2.COLOR_HLS2BGR)
    # 显示调整后的效果
    cv2.imshow("lightness and saturation", lsImg)
    ch = cv2.waitKey(5)
    # 按 ESC 键退出
    if ch == 27:
        break
    elif ch == ord('s'):
        # 按 s 键保存并退出
        lsImg = lsImg * 255
        lsImg = lsImg.astype(np.uint8)
        cv2.imwrite("lsImg.jpg", lsImg)
        break

# 关闭所有的窗口
cv2.destroyAllWindows()

# from tkinter import *  
# root = Tk()  
# sb = Scrollbar(root)
# sb.pack(side = LEFT,fill = Y)#fill属性前边文章有介绍X\Y\BOTH
# #下面的这句是关键：指定Listbox的yscrollbar的回调函数为Scrollbar的set 
# lb = Listbox(root,yscrollcommand = sb.set)
# for i in range(1000):
#     lb.insert(END,str(i))
# lb.pack(side = LEFT,fill = BOTH)
# #下面的这句是关键：指定Scrollbar的command的回调函数是Listbar的yview  
# sb.config(command = lb.yview) #用config函数设置属性
# root.mainloop() 