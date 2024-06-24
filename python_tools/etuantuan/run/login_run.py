import interface.login
token = "09e6aa6e29e7bbae7193459920f42863"
promotion_order_id = [11572,11573]
order_status = 3
num = 2


for i in range(num):
    print(interface.login.to_examine(token,promotion_order_id[i],order_status,num))
if __name__ == '__main__':
    pass