from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)



# HTML을 주는 부분
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main.html')
def main():
    return render_template('main.html')


# API 역할을 하는 부분
@app.route('/', methods=['POST'])
def play_map():

    return jsonify({'result': 'success','stars_list':stars})


@app.route('/api/like', methods=['POST'])
def star_like():

    return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def star_delete():

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
