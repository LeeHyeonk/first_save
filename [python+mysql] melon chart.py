# 크롤링한 값 DB에 저장하기 - 멜론 사이트 탑 100 데이터 크롤링, 데이터 베이스.

# win + r -> cmd -> mysql -u root -p 를 통해 mysql 접속

import MySQLdb      # Mysql에서 DB를 사용할때 필요한 모듈
import requests     # HTTP 호출하는 프로그램을 작성할때 가장 많이 쓰임.
from bs4 import BeautifulSoup

# GET: 서버로 부터 데이터를 취득
# POST: 서버에 데이터를 추가, 작성 등
# PUT: 서버의 데이터를 갱신, 작성 등
# DELETE: 서버의 데이터를 삭제

# -----------------------------------(웹크롤링)-----------------------------------------
if __name__ == "__main__":
    RANK = 100      # 멜론 차트 순위가 1 ~ 100위까지 있음.

    header = {  # 해당 브라우저에 접속하기 위해 Header를 만들어 주어야 한다.
                # User-Agent 를 설정해주어야 크롤링이 차단당하지 않는다.
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    # 가져오려는 데이터의 링크를 GET으로 가져와서 req에 저장
    req = requests.get('https://www.melon.com/chart/week/index.htm', headers=header)
    # 가져오려는 데이터 페이지의 html 소스 가져오기
    html = req.text
    # BeautifulSoup으로 html 소스를 python객체로 변환 (html소스코드, 어떤 parser을 이용할지)
    parse = BeautifulSoup(html, 'html.parser')

    # -----------------------------------(데이터)-----------------------------------------

    # find_all() / select() 를 사용하면 특정 조건을 만족하는 전체 데이터를 얻을 수 있다.
    # find_all(name:태그이름, 딕셔너리 형식의 값)

    # 노래 제목의 정보는 div 태그의 ellipsis rank01 클래스 안에 있다.
    titles = parse.find_all("div", {"class": "ellipsis rank01"})

    # 가수의 정보는 div 태그의 ellipsis rank02 클래스 안에 있다.
    singers = parse.find_all("div", {"class": "ellipsis rank02"})
    # 데이터만 저장할 real_title과 real_singer 리스트를 생성.
    real_title = []
    real_singer = []
    # 가져온 titles에서 a태그의 텍스트 값을 가져와서 real_ 리스트에 for문으로 저장
    for i in titles:
        real_title.append(i.find('a').text)
    for t in singers:
        real_singer.append(t.find('a').text)
        # real_singer.append(t.find('span', {"class": "checkEllipsis}).text"}))
    # 제목과 가수를 매칭시켜서 items 리스트에 넣는다. - items 안에 item 객체들이 있음.
items = [item for item in zip(real_title, real_singer)]

print(items)

# -----------------------------------(DB 저장)-----------------------------------------
# 데이터를 DB에 저장
# DB에 연결시킬 객체 생성
conn = MySQLdb.connect(
    user="crawl_usr",
    passwd='Test001',
    host="localhost",
    db="crawl_data",
    charset="utf8"
)
print(conn)

# sql커서 생성
cursor = conn.cursor()
print(cursor)

# 실행할때마다 다른 값이 나오지 않도록 테이블 제거하기
cursor.execute("DROP TABLE IF EXISTS melon")

# 테이블 생성하기
cursor.execute("CREATE TABLE melon (`rank` int, title text, url text)")
i = 1

# 데이터 저장하기
# melon 테이블에 값 rank, item[0] = title, item[1] = singer을 넣는다.
for item in items:
    cursor.execute(
        f"INSERT INTO melon VALUES({i}, \"{item[0]}\", \"{item[1]}\")")
    i += 1

# 커밋하기
conn.commit()

# 연결 종료하기
conn.close()
