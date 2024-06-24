import json
file_path = 'BUG.laketable'

try:
    with open(file_path, 'r') as file:
        # 读取整个文件内容
        # content = file.read()

        # 或者读取每一行并放入列表
        content_lines = file.readlines()

        # 打印文件内容
        # print("文件内容:\n", content)

        # 打印每一行的内容
        # print("文件内容:")
        for line in content_lines:
            a = line.strip()  # strip()用于去除每行末尾的换行符

except FileNotFoundError:
    print(f"文件 '{file_path}' 不存在")
except Exception as e:
    print(f"发生错误: {e}")
b = json.loads(a)
c = b["records"][0]["uuid"]
d = b["records"][0]["doc_id"]
e = b["records"][0]["doc_type"]
f = b["records"][0]["sheet_id"]
g = b["records"][0]["user_id"]
h = b["records"][0]["modifier_id"]
i = b["records"][0]["created_at"]
j = b["records"][0]["updated_at"]
k = json.loads(b["records"][0]["data"])
l = k["IgOHQSM3kgqCHUG5P55spDKHUiAG6hvm"]["value"][0]["src"]

print(l)