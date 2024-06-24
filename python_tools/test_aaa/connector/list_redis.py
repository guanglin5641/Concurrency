import http.client
import mimetypes
from codecs import encode
import json

def redis_link(promotion_id):

    host = "bwc.ds44.top"
    conn = http.client.HTTPSConnection("bwc.ds44.top")
    boundary = ''
    payload = ''
    headers = {
        'version': '1',
        'token': '',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': host,
        'Connection': 'keep-alive',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("GET", "/shopapi/test/test?promotion_id={}".format(promotion_id), payload, headers)
    res = conn.getresponse()
    data = res.read()
    return (data.decode("utf-8"))



if __name__ == '__main__':
    print(redis_link())

