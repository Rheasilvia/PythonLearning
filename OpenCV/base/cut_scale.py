import cv2

img = cv2.imread('lena.bmp')
# 缩放200x200
img_200x200 = cv2.resize(img, (200, 200))
# fx和fy指定的是缩放比例
img_200x300_1 = cv2.resize(img, (300, 200))  # 1
# 插值方法，刚好默认是cv2.inter_linear，这里指定的为最近邻插值
img_200x300_2 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)  # 2

cv2.imwrite('lena_200x200.jpg', img_200x200)
cv2.imwrite('lena_200x300_1.jpg', img_200x300_1)
cv2.imwrite('lena_200x300_2.jpg', img_200x300_2)

# 在上图基础上，上下各贴50像素的黑边生成300x300
img_300x300 = cv2.copyMakeBorder(img, 50, 50, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))  # 填充颜色最后的value
cv2.imwrite('lena_300x300.jpg', img_300x300)

# 裁剪
patch_pic = img[20:200, -300:-50]
cv2.imwrite('lena_patch.jpg', patch_pic)
