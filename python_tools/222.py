import psutil
import requests

def get_open_ports():
    open_ports = []
    # 遍历网络连接信息
    for conn in psutil.net_connections():
        # 过滤出监听状态的连接
        if conn.status == 'LISTEN':
            # 获取端口号并添加到开放端口列表中
            open_ports.append(conn.laddr.port)
    return open_ports
def check_proxy(post):
    try:
        # 构造代理字典
        proxies = {
            'http': 'http://127.0.0.1:' + post,
            'https': 'http://127.0.0.1:' + post
        }
        # 向 Google 发送 GET 请求
        response = requests.get('http://www.google.com', proxies=proxies, timeout=1)
        # 检查响应状态码
        if response.status_code == 200:
            # print("开始"+response.text+"结束")
            return True
        else:
            return False
    except Exception as e:
        # print("连接失败:", e)
        print(post,"端口无法使用")
        return False
def find_process_by_port(port):
    for conn in psutil.net_connections():
        if conn.status == 'LISTEN' and conn.laddr.port == port:
            return psutil.Process(conn.pid)
    return None

if __name__ == "__main__":
    if 0.000000 == 0:

        print("true")
    else:
        print("false")
