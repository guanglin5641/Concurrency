import socket

def main():
    # 定义服务器地址和端口
    HOST = '120.26.50.195'  # 监听本地连接
    PORT = 8888 # 监听端口号

    # 创建 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定地址和端口
        s.bind((HOST, PORT))
        # 开始监听
        s.listen()
        print(f"Server listening on {HOST}:{PORT}...")
        # 接受连接并处理
        while True:
            # 等待客户端连接
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # 接收客户端发送的数据
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received data: {data.decode()}")
                # 假设这里是对接收到的数据进行处理的代码
                # 这里可以根据接收到的数据执行相应的操作
                # 例如，可以根据接收到的命令执行不同的功能
                # 这里只是简单地将接收到的数据发送回客户端
                conn.sendall(data)

if __name__ == "__main__":
    main()
