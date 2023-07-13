from flask import Flask, jsonify, request
from extension import cors

import json

app = Flask(__name__)
cors.init_app(app)  # 跨域请求伪造


@app.route('/')
def hello_world():
    return request.url


@app.route('/movie', methods=['GET'])
def scrape():
    # 从JSON文件中读取数据
    with open('../Scripts/movie.json', 'r', encoding='utf8', errors='ignore') as f:
        data = json.load(f)
    # 将数据作为JSON响应发送给前端
    return jsonify(data)


@app.route('/game', methods=['GET'])
def game():
    # 从JSON文件中读取数据
    with open('../Scripts/game.json', 'r', encoding='utf8', errors='ignore') as f:
        data = json.load(f)
    # 将数据作为JSON响应发送给前端
    return jsonify(data)


if __name__ == '__main__':
    app.run()
