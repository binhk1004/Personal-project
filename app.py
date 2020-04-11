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

@app.route('/main.html', methods=['POST'])
def find_list():
    NB_receive = request.form['local_NB']
    local_result = list(db.Local_DB.find({'법정동명':"local_NB"}, {'_id': False}))
    return jsonify({'result':'success', 'msg': '데이터베이스 접속 성공'})

# @app.route('/main.html', methods=['GET'])
# def show_list():
#     # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
#     # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
#     DB = list(db.Local_DB.find({},{'_id':False}))
#     # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
#     return jsonify({'result': 'success','show_list':DB})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
