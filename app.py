from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Project_DB

# HTML을 주는 부분
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/main.html', methods=['GET'])
def result():
    if request.method == 'GET':
        return jsonify({'result':'success', 'msg': '데이터베이스 접속 성공'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
