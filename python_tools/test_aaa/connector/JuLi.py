from geopy.distance import geodesic
import requests
import time
import test_aaa.common.mysql


def baidu_dis(address):
    body = {"keyWord": address}
    url = f"http://api.tianditu.gov.cn/geocoder?ds={body}&tk=a0be488f7b6890d31cc424814a297c51"
    headers = {"referrer": "","referrerPolicy": "strict-origin-when-cross-origin"}

    response_json = requests.get(url, headers=headers).json()
    if response_json['msg'] == "ok":
        coordinates = (response_json['location']['lon'], response_json['location']['lat'],response_json['location']['keyWord'])
        return coordinates
    else:
        return None
    # return response_json
def reverse_geography(lon,lat):
    body = {'lon':lon,'lat':lat,'ver':1}
    url = f"http://api.tianditu.gov.cn/geocoder?postStr={body}&tk=a0be488f7b6890d31cc424814a297c51"
    headers = {"referrer": "", "referrerPolicy": "strict-origin-when-cross-origin"}

    response_json = requests.get(url, headers=headers).json()
    if response_json['msg'] == "ok":
        coordinates = (response_json['result']['formatted_address'])
        return coordinates
    else:
        return None
    # return response_json
def driving_planning(starting,end):
    body = {"orig":starting,"dest":end,"style":"1"}
    url = f"http://api.tianditu.gov.cn/drive?postStr={body}&type=search&tk=a0be488f7b6890d31cc424814a297c51"
    headers = {"referrer": "", "referrerPolicy": "strict-origin-when-cross-origin"}
    response_json = requests.get(url, headers=headers).text

    return response_json




def calculate_distance(coord1, coord2):
    """
    计算两个经纬度之间的距离。

    Args:
        coord1: 第一个经纬度，格式为 (纬度, 经度)。
        coord2: 第二个经纬度，格式为 (纬度, 经度)。

    Returns:
        两个经纬度之间的距离，单位为千米。
    """
    distance = geodesic(coord1, coord2).kilometers*1000
    return distance




if __name__  == '__main__':
    pass
    # coord1 = (28.157595, 112.983789)
    # coord2 = (28.149685, 112.986088)
    # distance_m = calculate_distance(coord1, coord2)
    # print(distance_m)

    # print(reverse_geography(121.63552,29.84586))
    # print(baidu_dis("浙江省宁波市鄞州区邱隘镇振兴路90号"))

    print(driving_planning("121.82153, 29.7224800000001","121.63552,29.84586"))



