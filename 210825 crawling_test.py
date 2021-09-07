#-*- coding: utf-8 -*-
# https://hyun-am-coding.tistory.com/entry/%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-DB%EC%97%90-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0?category=778333
# 데이터 크롤링해서 DB에 저장하기 프로젝트 - 간단 테스트 버전

# 필요한 모듈 임포트
import MySQLdb

#mysql의 계정의 특정 데이타베이스에 접속해서 연결 객체(conn) 생성
conn = MySQLdb.connect(
    user="crawl_usr",
    passwd="Test001",
    host="localhost",
    db="crawl_data",
    charset="utf8"
)

# Step3 - 커서(cursor) 객체 생성
# 커서는 SQL문을 실행하거나, 결과를 돌려받는 통로이다.
# 객체명 = 연결객체(conn).cursor()
print(type(conn))
cursor = conn.cursor()
print(type(cursor))

# Step4 - sql 명령을 실행
# database crawl_data 의 books 테이블을 생성, 컬럼 생성.
"""
# 커서(cursor)객체.execute(sql명령문)
cursor.execute("CREATE TABLE books (title text, url text)")
"""

# 테이블에 값을 넣어보기.
"""
bookname = "We will start python"
url_name = "www.wikibook.co.kr"
cursor.execute(f"INSERT INTO books VALUES(\"{bookname}\",\"{url_name}\")")
"""

# 실행할 때마다 다른 값이 나오지 않게 테이블을 제거해두기
cursor.execute("DROP TABLE IF EXISTS books")

# 테이블 생성하기
cursor.execute("CREATE TABLE books (title text, url text)")

# 데이터 저장하기

bookname = '처음 시작하는 파이썬'
url_name = "www.wikibook.co.kr"
cursor.execute(f"INSERT INTO books VALUES(\"{bookname}\",\"{url_name}\")")

# 커밋하기
conn.commit()

# 연결 종료하기
conn.close()
