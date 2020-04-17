from flask import Flask, render_template, jsonify, request
import requests
import numpy as np
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

    result_list = []

    for i in range(2015, 2020):
        result_list.append(change_year(i,local_num))
        

    graph_data = result_list

    # for index, value in enumerate(graph_data):
    #     ...
    #     print(index, value)

    row_data1 = graph_data[0]['referLandPrices']['field'][0]
    row_data2 = graph_data[1]['referLandPrices']['field'][0]
    row_data3 = graph_data[2]['referLandPrices']['field'][0]
    row_data4 = graph_data[3]['referLandPrices']['field'][0]
    row_data5 = graph_data[4]['referLandPrices']['field'][0]


    last_data1 = row_data1['ldCode'], row_data1['ldCodeNm'], row_data1['pblntfPclnd'], row_data1['stdrYear']
    last_data2 = row_data2['ldCode'], row_data2['ldCodeNm'], row_data2['pblntfPclnd'], row_data2['stdrYear']
    last_data3 = row_data3['ldCode'], row_data3['ldCodeNm'], row_data3['pblntfPclnd'], row_data3['stdrYear']
    last_data4 = row_data4['ldCode'], row_data4['ldCodeNm'], row_data4['pblntfPclnd'], row_data4['stdrYear']
    last_data5 = row_data5['ldCode'], row_data5['ldCodeNm'], row_data5['pblntfPclnd'], row_data5['stdrYear']

    fin_data = row_data1['stdrYear'], row_data1['pblntfPclnd'], row_data2['stdrYear'], row_data2['pblntfPclnd'], row_data3['stdrYear'], row_data3['pblntfPclnd'], row_data4['stdrYear'], row_data4['pblntfPclnd'], row_data5['stdrYear'], row_data5['pblntfPclnd']

    return jsonify({'result':'success', 'msg': fin_data})
    return render_template('main.html', fin_data=fin_data)




def change_year(year,local_num):
    params = {
        'ServiceKey': unquote(
            'jFJq%2B%2BJgU2Mc8PrE5BxRZetsGiBrM%2BXDSku%2FUFCuzZ7j8FrslWnJ%2BR2xa7QbRStVG9HfSDU%2BmBQz3SCSfZmfXw%3D%3D'),
        'ldCode': local_num, 'stdrYear': year, 'format': 'json', 'numOfRows': '1', 'pageNo': '1'
    }
    result = requests.get('http://apis.data.go.kr/1611000/nsdi/ReferLandPriceService/attr/getReferLandPriceAttr', params=params)

    return result.json()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
