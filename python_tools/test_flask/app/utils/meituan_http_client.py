import http.client
import urllib.parse
import json
import time

def make_request():
    try:
        conn = http.client.HTTPSConnection("maf.meituan.com")
        timesmp = int(time.time() * 1000)
        payload = ''
        headers = {
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Accept': '*/*',
            'Host': 'maf.meituan.com',
            'Connection': 'keep-alive'
        }

        # URL编码
        params = {
            'optimus_code': '10',
            'optimus_risk_level': '71',
            'key': 'be9427ec-bca4-4bfa-b981-9314f6a1adc7',
            'location': '120.503134,30.099414',
            'region': 'CITY',
            'orderby': 'weight',
            'radius': '50000',
            'pageSize': '20',
            'page': '1',
            'scenario': 'WAIMAI',
            'city': '杭州',
            'keyword': '浙江省杭州市富阳区宝龙(文居街店)',
            'wmUuidDeregistration': '0',
            'wmUserIdDeregistration': '0',
            'openh5_uuid': '6CE75D4B0A44B4836A2221DDACF876D9EBD910C1557D6578A55667DF7E870919',
            'uuid': '6CE75D4B0A44B4836A2221DDACF876D9EBD910C1557D6578A55667DF7E870919',
            '_': '1718344464608',
            'yodaReady': 'h5',
            'csecplatform': '4',
            'csecversion': '2.4.0',
            'mtgsig': '{"a1":"1.1","a2":1718344464610,"a3":"u2132v22v39u5681y96x00853855077680984564v4497958v1y20509","a5":"Epy8B1K9kz+iCfxS3KAP44GHJrj4//4lBc==","a6":"hs1.4aOG4x69iuIGtADfqn9IKccpCffPQ1A0Vkcb3Tzq2kqioLVmx+k8s0mSlEtJcaCnjHMtXUjMFUOTcj1MqhXakhQ==","x0":4,"d1":"dc8a8b54211db771d3a2004dfd973c6a"}'
        }
        encoded_params = urllib.parse.urlencode(params)
        url = f"/search?{encoded_params}"

        conn.request("GET", url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

    except Exception as e:
        print(f"请求失败: {e}")
        return None
    finally:
        conn.close()

if __name__ == '__main__':
    # 调用方法
    response = make_request()
    print(response)
    if response:
        response_json = json.loads(response)
        pois = response_json.get('result', {}).get('pois', [])
        if len(pois) > 1:
            b = pois[1]
            print(b["name"], b["location"])
        else:
            print("没有找到足够的POI点")
    else:
        print("请求失败或返回数据为空")
    


