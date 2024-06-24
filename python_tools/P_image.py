import cv2
import matplotlib.pyplot as plt

# 加载图像
image = cv2.imread(r'C:\Users\EDY\Downloads\Screenshot_2023-09-02-12-05-42-511_me.ele (1).jpg')

# 进行图像处理，如灰度化、二值化等
# ...

# 进行图像识别
# ...

# 显示结果
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()