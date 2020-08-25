
#方法一
from skimage import data, exposure, img_as_float,io
import matplotlib.pyplot as plt

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

file_dir = r'/Users/any/Desktop/ajt/practice/Python/item/pyItemPrce/ImgHandle/9987443.JPG'
# image = get_file_content(file_dir)
image = io.imread(file_dir)
# image = img_as_float(img)
# image = skimage.io.imread(file_dir, as_grey=False)

gam1= exposure.adjust_gamma(image, 2)   #调暗
gam2= exposure.adjust_gamma(image, 0.8)  #调亮
plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(131)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')

plt.subplot(132)
plt.title('gamma=2')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')

plt.subplot(133)
plt.title('gamma=0.8')
plt.imshow(gam2,plt.cm.gray)
plt.axis('off')

plt.show()

# save_dir = r'/Users/any/Desktop/ajt/practice/Python/item/pyItemPrce/ImgHandle/handle12557.JPG'
# io.imsave(save_dir,gam2)


