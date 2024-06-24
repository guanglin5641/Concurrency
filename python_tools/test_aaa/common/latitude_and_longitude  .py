import http.client
import json

def get_coordinates(address):
    conn = http.client.HTTPSConnection("nominatim.openstreetmap.org")
    params = f"/search?q={address}&format=json&limit=1"
    conn.request("GET", params)
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    conn.close()

    data = json.loads(data)
    if data:
        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])
        return latitude, longitude
    else:
        return None

address = "浙江省宁波市鄞州区潘火街道沧海路2332号"
coordinates = get_coordinates(address)
if coordinates:
    latitude, longitude = coordinates
    print("纬度：", latitude)
    print("经度：", longitude)
else:
    print("无法获取地址的经纬度")


if __name__ == "__main__":
    pass