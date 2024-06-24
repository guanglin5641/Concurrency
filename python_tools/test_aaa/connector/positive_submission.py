import http.client
import json
import time
def get_submit(image):
    import http.client
    import json

    conn = http.client.HTTPSConnection("api.dac8.cn")
    payload = json.dumps({
        "image": image,
        "type": 1
    })
    headers = {
        'S-Open-User': '{{open_id}}',
        'S-Platform': 'h5',
        'S-Ip': '192.168.101.45',
        'S-Version': '1.124',
        'S-City': '330101',
        'S-Trace-Id': '11',
        'S-Time': '1223',
        'S-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDbGllbnRVc2VySWQiOjEwMTgyNDY5OCwiVXNlck5hbWUiOiIiLCJleHAiOjE3MDIwOTQ3MDIsImlhdCI6MTY5OTQ5NTUwMiwibmJmIjoxNjk5NDk1NTAyfQ.dxiEvq8piaOhOD_sHsu4h742Jbr2LIO1FJZYcW1DD3M',
        'S-Login-User': '101824698',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': 'api.dac8.cn',
        'Connection': 'keep-alive'
    }
    conn.request("POST", "/mobile/marketing/submit_comment_cashback", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return (data.decode("utf-8"))

if __name__ == '__main__':
    print(get_submit('https://img.dac6.cn/file/image/mobile/1699612698c50de962d06f6d9f2aca5029e45e253e.png'))