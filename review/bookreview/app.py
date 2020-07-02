from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reviews', methods=['POST'])
def write_review():
    title_received = request.form['title_give']
    author_received = request.form['author_give']
    review_received = request.form['review_give']

    doc = {
        'title' : title_received, 
        'author': author_received, 
        'review': review_received
        }
 
    db.reviews.insert_one(doc)
    
    return jsonify ({'result':'success', 'msg': '리뷰가 작성되었습니다!'})

@app.route('/reviews', methods=['GET'])
def read_review():
    reviews = list(db.reviews.find({},{'_id':0}))

    return jsonify({'result': 'success', 'reviews': reviews})               

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)  
