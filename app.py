from flask import Flask, render_template, jsonify, request
import json
from bs4 import BeautifulSoup
import requests, jinja2
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

@app.route('/main', methods=['POST','GET'])
def find_list():
    NB_receive = request.form['local_NB']
    local_result = list(db.Local_DB.find({'법정동명':NB_receive}, {'_id': False}))
    local_num = local_result[0]['법정동코드']

    result_list = []

    for i in range(2015, 2020):
        result_list.append(change_year(i,local_num))


    graph_data = result_list

    row_data1 = graph_data[0]['referLandPrices']['field'][0]
    row_data2 = graph_data[1]['referLandPrices']['field'][0]
    row_data3 = graph_data[2]['referLandPrices']['field'][0]
    row_data4 = graph_data[3]['referLandPrices']['field'][0]
    row_data5 = graph_data[4]['referLandPrices']['field'][0]

    fin_data = row_data1['pblntfPclnd'], row_data2['pblntfPclnd'], row_data3['pblntfPclnd'], row_data4['pblntfPclnd'], row_data5['pblntfPclnd']
    show_news(NB_receive)
    return fin_data

def show_news(NB_receive):
    NB_receive = request.form['local_NB']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683'}

    data = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + NB_receive + ' 부동산', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    news = soup.select('#main_pack > .news > .type01 > li')


    news_list = {}

    for new in news:
        link = new.select_one('dl > dt > a')
        if not link == None:
            news_list['news_show'] = [link]
            html_news = news_list['news_show']
            html_data1 = json.dumps(html_news[0]['href'])
            html_data2 = json.dumps(html_news[0]['title'], ensure_ascii=False)
            final_data = html_data1

    return jsonify({'result': 'success', 'msg' : list(fin_data), 'data': final_data})


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
