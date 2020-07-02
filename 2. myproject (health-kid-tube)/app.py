from pymongo import MongoClient           # pymongo를 임포트 하기
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pytube import YouTube

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posting', methods=['POST'])
def saving():
    type_receive = request.form['type_give']
    memo_receive = request.form['memo_give']
    url_receive = request.form['url_give']

    
    yt = YouTube(url_receive)

    title = yt.title
    image_url = yt.thumbnail_url

    #크롤링
    # headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get(url_receive, headers=headers)
    # soup = BeautifulSoup(data.text, 'html.parser')

    doc = {
        'type': type_receive,
        'title': title,
        'memo' : memo_receive,
        'url' : url_receive,
        'image': image_url
    }

    db.kidtube.insert_one(doc)

    return jsonify({'result': 'success', 'msg':'운동 카드 POST 되었습니다!'})

@app.route('/posting/show_all', methods=['get'])
def showing():
    kidtubes = list(db.kidtube.find({},{'_id':0}))

    return jsonify({'result': 'success', 'kidtubes':kidtubes})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
