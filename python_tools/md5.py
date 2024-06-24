import hashlib
def decrypt_md5(md5_hash):
    # 将MD5哈希值转换为十六进制字符串
    md5_hash = md5_hash.lower()
     # 尝试使用常见的字典进行解密
    with open('common_passwords.txt', 'r') as file:
        for password in file:
            password = password.strip()
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            if hashed_password == md5_hash:
                return password
     # 如果没有找到匹配的解密结果，则返回空值
    return None
 # 示例用法
hashed = 'e10adc3949ba59abbe56e057f20f883e'  # 要解密的MD5哈希值
result = decrypt_md5(hashed)
if result:
    print(f"解密结果：{result}")
else:
    print("未找到匹配的解密结果")