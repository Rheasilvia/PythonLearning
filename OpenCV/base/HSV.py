import cv2

# 通过cv2.cvtColor把图像从BGR转换到HSV
img = cv2.imread('yello.jpg')

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# H空间，绿色比黄色的值高一点，所以给每个像素+15，黄色的树叶就会变绿
turn_green_hsv = img_hsv.copy()
turn_green_hsv[:, :, 0] = (turn_green_hsv[:, :, 0] + 15) % 180
turn_green_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('turn_green.jpg', turn_green_img)

# 减小饱和度会让图像损失鲜艳变得更灰
colorless_hvs = img_hsv.copy()
colorless_hvs[:, :, 1] = 0.5 * colorless_hvs[:, :, 1]
colorless_img = cv2.cvtColor(colorless_hvs, cv2.COLOR_HSV2BGR)
cv2.imwrite('colorless.jpg', colorless_img)
# 减小明度为原来一半
darker_hsv = img_hsv.copy()
darker_hsv[:, :, 2] = 0.5 * darker_hsv[:, :, 2]
darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('darker.jpg', darker_img)
