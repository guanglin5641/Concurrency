from flask import Flask, jsonify, request
from text1 import test
app = Flask(__name__)
t = test(10,20)
@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json
    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000 ,debug=True)
