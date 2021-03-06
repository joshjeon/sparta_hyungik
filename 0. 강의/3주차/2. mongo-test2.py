import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt'] # img 태그의 alt 속성값을 가져오기
        title = a_tag.text                                      # a 태그 사이의 텍스트를 가져오기
        star = movie.select_one('td.point').text                # td 태그 사이의 텍스트를 가져오기
        print(rank,title,star)

        # doc은 Mongo 객체집합 선언이라 보면 됨 key:value 라 생각하면됨
        doc = {
            'rank' : rank,
            'title' : title,
            'star' : star
        }
        db.movies.insert_one(doc)

        #rank : #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1)
        #title : #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
        #star : #old_content > table > tbody > tr:nth-child(2) > td.point

## "매트릭스" 평점 가져오기
target_movie = db.movies.find_one({'title':'매트릭스'})
if target_movie is not None:
    print(target_movie['star'])

## "매트릭스" 평점과 같은 영화 가져오기
target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))
for movie in movies:

    print(movie['title'])

## "매트릭스" 평점과 같은 영화 평점 "0" 으로 바꾸기

#첫번째 방법
# for movie in movies:
#     title = movie['title']
#     db.movies.update_one({'title':title},{'$set':{'star':0}})

#두번째 방법
db.movies.update_many({'star':target_star},{'$set':{'star':0}})


