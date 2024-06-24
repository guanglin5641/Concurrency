import pandas as pd

def match_and_modify_excel(file1, file2, match_field, modify_field):
    # 读取两个Excel文件
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # 根据指定字段进行匹配
    merged_df = pd.merge(df1, df2, on=match_field, how='inner')

    # 修改匹配结果
    merged_df[modify_field] = '修改后的值'

    # 保存修改后的结果到新的Excel文件
    merged_df.to_excel('修改后的表格.xlsx', index=False)

# 调用函数进行匹配和修改
match_and_modify_excel('表格1.xlsx', '表格2.xlsx', '字段名1', '字段名2')