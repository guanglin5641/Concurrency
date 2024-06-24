from app.common.mysql import MysqlHelper
from app.routes.shenqun_routes import TEST_MYSQL
import pandas as pd

# 读取Excel文件
file_path = r'C:\Users\lenovo\Desktop\address.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# 增加新列以存储查询到的经纬度、地址和距离
df['queried_address'] = None
df['queried_long'] = None
df['queried_lat'] = None
df['distance'] = None
df['sql'] = None

# 初始化数据库连接
db = MysqlHelper(TEST_MYSQL)

# 遍历 DataFrame 中的每一行，将 address、long 和 lat 数据组合成一个元组，并添加到列表中
for index, row in df.iterrows():
    address = row['address']
    sql = "SELECT formatted_address, location FROM shenquan.business_district_location bdl WHERE formatted_address = %s"
    params = (address,)
    db_data = db.get_one(sql, params)

    if db_data:
        db_formatted_address, db_lo_la = db_data
        try:
            db_longitude, db_latitude = map(float, db_lo_la.split(','))
        except ValueError:
            print(f"Error parsing location for address: {address}")
            continue

        longitude = row['long']
        latitude = row['lat']

        # 确认查询到的经纬度和 Excel 中的地址在同一行
        if db_longitude and db_latitude:
            sql_address = """
                SELECT ST_Distance_Sphere(
                    POINT(%s, %s),
                    POINT(%s, %s)
                ) AS distance
            """
            params_address = (longitude, latitude, db_longitude, db_latitude)
            distance = db.get_one(sql_address, params_address)

            if distance:
                distance_m = distance[0]
                distance_km = distance_m / 1000
                df.at[index, 'queried_address'] = db_formatted_address
                df.at[index, 'queried_long'] = db_longitude
                df.at[index, 'queried_lat'] = db_latitude
                df.at[index, 'distance'] = distance_km
                df.at[index, 'sql'] = sql_address

# 将更新后的 DataFrame 写入 Excel 文件
df.to_excel(file_path, sheet_name='Sheet1', index=False)

print("Updated Excel file with queried address, coordinates, and distances.")
