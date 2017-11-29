import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
], dtype=np.uint8)

# 用matplotlib存储
plt.imsave('img_plyplot.jpg', img)
cv2.imwrite('img_cv2.jpg', img)

# 读取
color_img = cv2.imread('img_cv2.jpg')
print(color_img.shape)

# 读取单通道
gray_img = cv2.imread('img_cv2.jpg', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)

# 单通道图片保存后，再次读取，仍然是3通道，相当于单通道的只赋值到3个通道保存
cv2.imwrite('test_grayscale.jpg', gray_img)
reload_grayscale = cv2.imread('test_grayscale.jpg')
print(reload_grayscale.shape)

# cv2.IMWRITE_JPEG_QUALITY指定jpg质量，范围为0~100，默认95
cv2.imwrite('test_imwrite.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 80))

# 指定png格式的质量,范围0~9，默认3
cv2.imwrite('test_imwrite.png', color_img, (cv2.IMWRITE_PNG_COMPRESSION, 5))
