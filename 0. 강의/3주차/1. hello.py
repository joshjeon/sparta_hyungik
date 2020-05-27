print("hellow world!")  #javascript의 console(log) 와 같은 


def is_adult(age):
	if age > 20:
		print('성인입니다')    # 조건이 참이면 성인입니다를 출력
	else:
		print('청소년이에요')  # 조건이 거짓이면 청소년이에요를 출력

is_adult(15)
# 무엇이 출력될까요?

fruits = ['사과','배','감','귤']

for fruit in fruits:
	print(fruit)

# 사과, 배, 감, 귤 하나씩 꺼내어 찍힙니다.

######################################

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
	if fruit == '사과':
		count += 1

print(count)    # 결과는 2

#########################

def count_fruits(name):
	count = 0
	for fruit in fruits:
		if fruit == name:
			count += 1
	return count

subak_count = count_fruits('수박')
print(subak_count) #수박의 갯수

gam_count = count_fruits('감')
print(gam_count) #감의 갯수

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
print(rjson['RealtimeCityAir']['row'][0]['NO2'])
