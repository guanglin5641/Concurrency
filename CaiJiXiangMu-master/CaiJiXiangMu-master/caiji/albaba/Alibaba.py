# import requests
# import json
#
# url = "https://h5api.m.1688.com/h5/mtop.1688.shop.data.get/1.0/?jsv=2.7.0&appKey=12574478&t=1696019668723&sign=7534a0775b3b00d67454c9e1824b27f8&api=mtop.1688.shop.data.get&v=1.0&type=json&valueType=string&dataType=json&timeout=10000"
# headers = {
#     'Accept': 'application/json',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Content-Length': '592',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': 'cna=wBueHV36ZRoCAX13ZVybTLfu; xlly_s=1; taklid=26ed99a804014f9cab1b53b82ccef15c; _m_h5_tk=0e306ed8af22c0c3b96307b23c9885ba_1696025148150; _m_h5_tk_enc=1d0e983dbac4894b8dd47d1a0f925765; _csrf_token=1696019271678; __cn_logon__=false; cookie2=143cde3657caa015f1dec6b968baa123; t=ef96b08b833f32ad6d1e27180aa8abe3; _tb_token_=f33b768973665; isg=BHt7DgkvmpVNwKYhcNcj50M5Cl_l0I_SLUNXqm04InqQzJqu9KXHIvRN4myCaOfK; l=fBPKXmOmPN81KAo5BOfZourza77tMIRbmuPzaNbMi9fPOQ1B5GsAW1HomRT6CnGVesBBJ3J_8YVHB0YPsyCSnxv9-Grj3K5r3dLHR3zC.; tfstk=dNOXJsfufoqj2EJAQPgydvbCyz1sYnGFWP_9-FF4WsCAXPtJWNeYHiI-5H7OWZIYMUp57wrTXFnDfCsJWqxqosK_CHtC71JV0NpWmeBV_CTg1NL9jqjZoY8Do1ftYDRsTEYDEnZhGEP0jhNG6DoETX8Do1f93osOxGwmyfo4xEo7w7N3n46tTlBN3Q_feY8f22O2wZtRAEd76OkaTMTOyRa5K5_5Y4g7IR0-HZ1V.',
#     'Origin': 'https://shop25933le021370.1688.com',
#     'Referer': 'https://shop25933le021370.1688.com/',
#     'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Windows"',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
# }
# data: {"dataType":"moduleData","argString":"{\"memberId\":\"b2b-22162948651091a8ed\",\"appName\":\"pcmodules\",\"resourceName\":\"wpOfferColumn\",\"type\":\"view\",\"version\":\"1.0.0\",\"appdata\":{\"sortType\":\"wangpu_score\",\"sellerRecommendFilter\":false,\"mixFilter\":false,\"tradenumFilter\":false,\"quantityBegin\":null,\"pageNum\":1,\"count\":30}}"}
import requests
import json
import requests
url = "https://h5api.m.1688.com/h5/mtop.1688.shop.data.get/1.0/?jsv=2.7.0&appKey=12574478&t=1696020906302&sign=9e1091b9978266426cafa60aa0659475&api=mtop.1688.shop.data.get&v=1.0&type=json&valueType=string&dataType=json&timeout=10000"
headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Cookie': 'cna=wBueHV36ZRoCAX13ZVybTLfu; xlly_s=1; taklid=26ed99a804014f9cab1b53b82ccef15c; _m_h5_tk=0e306ed8af22c0c3b96307b23c9885ba_1696025148150; _m_h5_tk_enc=1d0e983dbac4894b8dd47d1a0f925765; _csrf_token=1696019271678; __cn_logon__=false; cookie2=143cde3657caa015f1dec6b968baa123; t=ef96b08b833f32ad6d1e27180aa8abe3; _tb_token_=f33b768973665; isg=BHt7DgkvmpVNwKYhcNcj50M5Cl_l0I_SLUNXqm04InqQzJqu9KXHIvRN4myCaOfK; l=fBPKXmOmPN81KAo5BOfZourza77tMIRbmuPzaNbMi9fPOQ1B5GsAW1HomRT6CnGVesBBJ3J_8YVHB0YPsyCSnxv9-Grj3K5r3dLHR3zC.; tfstk=dNOXJsfufoqj2EJAQPgydvbCyz1sYnGFWP_9-FF4WsCAXPtJWNeYHiI-5H7OWZIYMUp57wrTXFnDfCsJWqxqosK_CHtC71JV0NpWmeBV_CTg1NL9jqjZoY8Do1ftYDRsTEYDEnZhGEP0jhNG6DoETX8Do1f93osOxGwmyfo4xEo7w7N3n46tTlBN3Q_feY8f22O2wZtRAEd76OkaTMTOyRa5K5_5Y4g7IR0-HZ1V.'
}
data = {
    'dataType': 'moduleData',
    'argString': '{"memberId":"b2b-22162948651091a8ed","appName":"pcmodules","resourceName":"wpOfferColumn","type":"view","version":"1.0.0","appdata":{"sortType":"wangpu_score","sellerRecommendFilter":false,"mixFilter":false,"tradenumFilter":false,"quantityBegin":null,"pageNum":1,"count":30}}'
}
response = requests.post(url, headers=headers, data=data)
response_json = response.json()
print(json.dumps(response_json, indent=4, ensure_ascii=False))
