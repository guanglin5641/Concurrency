from flask import Flask, request

app = Flask(__name__)

@app.route('/check-ip', methods=['GET'])
def check_ip():
    client_ip = request.remote_addr
    return f"请求方的IP地址是: {client_ip}"

if __name__ == '__main__':
    app.run()