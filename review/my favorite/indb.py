import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta



def get_urls():

    url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#old_content > table > tbody > tr')
    #old_content > table > tbody > tr:nth-child(2) > td.title > a

    urls = []
    for tr in trs:
        a = tr.select_one('td.title > a')
        if a is not None:
            base_url = 'https://movie.naver.com/'
            get_url = base_url + a['href']
            urls.append(get_url)
    
    return urls  

def insert_star(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    #content > div.article > div.mv_info_area > div.mv_info.character > h3 > a
    name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
    #content > div.article > div.mv_info_area > div.poster > img
    image_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
 #content > div.article > div.mv_info_area > div.mv_info.character > dl > dd:nth-child(4) > a:nth-child(1)
 #content > div.article > div.mv_info_area > div.mv_info.character > dl > dd:nth-child(4) > a:nth-child(1)
    recent = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

    doc = {
        'name': name,
        'image_url': image_url,
        'recent': recent,
        'like': 0,
        'url': url
    }

    db.mystars.insert_one(doc)
    print('완료!', name)

def insert_all():
    db.mystars.drop()
    urls = get_urls()
    for url in urls:
        insert_star(url)

insert_all()