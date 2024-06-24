import requests
import  random
def request():
    ip_pool = ["http://1.224.3.122:3888"]
    url = "http://localhost:5000/check-ip"

    ip = random.choice(ip_pool)

    proxies = {
        "http": ip,
        "https": ip
    }

    try:
        r = requests.get(url, proxies=proxies, verify=False)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.RequestException as e:
        print("请求发生异常:", e)

if __name__ == "__main__":
    request()