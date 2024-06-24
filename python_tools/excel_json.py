
import json
import pandas as pd

# 读取Excel文件
excel_file = r'C:\Users\EDY\Desktop\rizhi.xlsx'
xls = pd.ExcelFile(excel_file)

# 初始化JSON对象
json_data = {}

# 遍历工作簿
for sheet_name in xls.sheet_names:
    # 读取工作簿数据
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    sheet_data = {}

    # 遍历每列
    for col_name in df.columns:
        # 将列名作为二级键
        col_data = df[col_name].tolist()
        sheet_data[col_name] = col_data

    # 将工作簿名作为一级键
    json_data[sheet_name] = sheet_data

# 将数据写入JSON文件
json_file = 'output.json'
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)

print("JSON文件已生成：", json_file)

