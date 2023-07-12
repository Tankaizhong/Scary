from flask import Flask, jsonify
from extension import cors


import json

app = Flask(__name__)
cors.init_app(app)  # 跨域请求伪造


@app.route('/')
def hello_world():
    return "hello"


@app.route('/scrape', methods=['GET'])
def scrape():
    # 从JSON文件中读取数据
    with open('../output.json', 'r', encoding='utf8', errors='ignore') as f:
        data = json.load(f)

    # 将数据作为JSON响应发送给前端
    return jsonify(data)


# @app.route('/test', methods=['GET'])
# def execute_script():
#     # cmdline.execute('scrapy crawl movie'.split())
#     result = test.execute()  # 调用Python文件中的函数或方法
#     return "result"


if __name__ == '__main__':
    app.run()
