import requests
import json
import pandas
def city_is_bwc(lng,lat):
    url = "http://apitest.waimai.biyingniao.com/mobile/tool/get_city_by_position"

    payload = json.dumps({
       "latitude": lat,
       "longitude": lng
    })
    headers = {
       'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
       'Content-Type': 'application/json',
       'Accept': '*/*',
       'Host': 'apitest.waimai.biyingniao.com',
       'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    #将response转为json格式
    response = response.json()
    #打印.data.current_city.is_bwc
    is_bwc = response['data']['current_city']['is_bwc']
    city_name = response['data']['current_city']['name']
    city_code = response['data']['current_city']['id']
    city_address = response['data']['current_city']['address']
    return is_bwc,city_name,city_code,city_address
#读取excel文件
data = pandas.read_excel(r'C:\Users\EDY\Desktop\city.xls')
#将文件第一列和第二列组成列表
lng_list = data['lng'].tolist()
lat_list = data['lat'].tolist()
#遍历列表
for i in range(len(lng_list)):
    lng = lng_list[i]
    lat = lat_list[i]
    is_bwc,city_name,city_code,city_address = city_is_bwc(lng,lat)
    print(is_bwc,city_name,city_code,city_address)
    # 将结果写入excel文件

    data.loc[i,'city_code'] = city_code
    data['is_bwc'] = data['is_bwc'].astype(object)
    data['city_name'] = data['city_name'].astype(object)
    data['city_address'] = data['city_address'].astype(object)

    # 然后进行赋值
    data.at[i, 'is_bwc'] = bool(is_bwc)  # 转换为布尔值
    data.at[i, 'city_name'] = str(city_name)  # 转换为字符串
    data.at[i, 'city_address'] = str(city_address)  # 转换为字符串



