import hashlib

def crack_md5_hash(md5_hash, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            word = line.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            if hashed_word == md5_hash:
                return f"Found: {word}"

    return "Not found in the wordlist"

# 示例
md5_hash_to_crack = "098f6bcd4621d373cade4e832627b4f6"  # 这是 "test" 的 MD5 哈希值
wordlist_path = "common_passwords.txt"  # 你的密码字典文件路径

result = crack_md5_hash(md5_hash_to_crack, wordlist_path)
print(result)
