import commen.interface
import commen.mysql
def test ():
    # mysql = commen.mysql.BD
    interface = commen.interface.HttpClient
    http = 'http://bwc.ds44.top'
    url = '/adminapi/hp_rec.hp_rec/audit'
    data = {
        "promotion_order_id":11564,
        "order_status":3
    }
    header = {
        'version':'2.4.0',
        'Content-Type':'application/json',
        'Accept':'application/json, text/plain, */*',
        'token':'09e6aa6e29e7bbae7193459920f42863'
    }
    res = interface(http).post(url,data,header)
    return res
if __name__ == '__main__':
    print(test())