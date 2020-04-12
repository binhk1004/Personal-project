from flask import Flask, render_template, jsonify, request
import requests
from urllib.parse import unquote

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Project_DB

# HTML을 주는 부분
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/main', methods=['POST'])
def find_list():
    NB_receive = request.form['local_NB']
    local_result = list(db.Local_DB.find({'법정동명':NB_receive}, {'_id': False}))
    local_num = local_result[0]['법정동코드']
    print(local_num)

    result_list = []

    for i in range(2015, 2020):
        result_list.append(change_year(i,local_num))

    print(result_list)
    return jsonify({'result':'success', 'msg': result_list})


def change_year(year,local_num):
    params = {
        'ServiceKey': unquote(
            'jFJq%2B%2BJgU2Mc8PrE5BxRZetsGiBrM%2BXDSku%2FUFCuzZ7j8FrslWnJ%2BR2xa7QbRStVG9HfSDU%2BmBQz3SCSfZmfXw%3D%3D'),
        'ldCode': local_num, 'stdrYear': year, 'format': 'json', 'numOfRows': '10', 'pageNo': '1'
    }
    result = requests.get('http://apis.data.go.kr/1611000/nsdi/ReferLandPriceService/attr/getReferLandPriceAttr', params=params)

    return result.json()





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
