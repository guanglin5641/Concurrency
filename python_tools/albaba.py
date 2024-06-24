import requests
from bs4 import BeautifulSoup

# 定义要抓取的商品链接
url = 'https://www.alibaba.com/product-detail/your-product-url'

# 发起请求
response = requests.get(url)

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 获取商品信息
product_title = soup.find('h1', class_='ma-title').text.strip()
product_price = soup.find('span', class_='ma-ref-price').text.strip()
product_description = soup.find('div', class_='ma-product-description').text.strip()

# 打印商品信息
print('商品标题:', product_title)
print('商品价格:', product_price)
print('商品描述:', product_description)