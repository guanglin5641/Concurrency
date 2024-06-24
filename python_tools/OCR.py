import os
import cv2
import pytesseract
from PIL import Image

def ocr(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 对图像进行二值化处理
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 创建临时图像文件
    temp_image = "temp.png"
    cv2.imwrite(temp_image, threshold)

    # 使用Tesseract进行OCR识别
    text = pytesseract.image_to_string(Image.open(temp_image), lang='eng')  # 这里使用英语作为语言，你可以根据需要更改

    # 删除临时图像文件
    os.remove(temp_image)

    return text

# 调用OCR函数并打印识别结果
image_path = r"C:\Users\EDY\Desktop/Dingtalk_20230825144110.jpg"  # 替换为你的图像路径
result = ocr(image_path)
print(result)