from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# HTML을 주는 부분
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/main.html', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        result = request.form
        return render_template('main.html', prediction = result)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
