import aiohttp
import asyncio


async def test_api(url, headers, data):
    # 创建一个连接池
    async with aiohttp.ClientSession() as session:
        # 创建一个请求列表
        requests = []
        num = len(data)
        for _ in range(num):
            request = session.post(url=url, headers=headers, json=data)
            requests.append(request)
            print(data)  # 打印请求对象

        # 并发发送请求
        responses = await asyncio.gather(*requests)

        # 处理响应结果
        results = []
        for response in responses:
            response_data = await response.json()
            result = (response.status, response_data)
            results.append(result)
    return results


def call_test_api(url, headers, data):
    loop = asyncio.get_event_loop()
    a = loop.run_until_complete(test_api(url, headers, data))
    return a


def to_examine(token, promotion_order_ids, order_status):
    Urls = ['https://bwc.ds44.top/adminapi/hp_rec.hp_rec/audit'] * len(promotion_order_ids)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Origin": "https://bwc.ds44.top",
        "Pragma": "no-cache",
        "Referer": "https://bwc.ds44.top/admin/ett/hp_rec/lists",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "token": token,
        "version": "2.4.0"
    }
    datas = []
    for promotion_order_id in promotion_order_ids:
        data = {
            "promotion_order_id": promotion_order_id,
            "order_status": order_status
        }
        datas.append(data)

    results = []
    for i in range(len(promotion_order_ids)):
        result = call_test_api(Urls[i], headers, datas[i])
        results.append(result)
    return results


if __name__ == '__main__':
    token = "ff1b1f651d46e516de0a27247b0486de"
    promotion_order_ids = [11614, 11615]
    order_status = 3
    print(to_examine(token,promotion_order_ids,order_status))