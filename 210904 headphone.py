# 1. 데이터 수집

# 다나와 페이지에서 어떤  "노이즈캔슬링 헤드폰" 에 대한 선호도를 분석하도록 한다.
# [데이터분석 실무 with 파이썬] 책을 참고하여 작성하였다.
# 데이터 수집을 위해 웹크롤링을 이용할것이며, 이번 크롤링에서는 selenium과 크롬드라이버를 이용해볼것이다.
# pip install selenium - selenium 설치
# 크롬드라이버는 별도의 설치가 필요함. https://sites.google.com/a/chromium.org/chromedriver/downloads 에서 사용중인 크롬의 버전에 맞는 드라이버를 설치해온다.
# 설치한 exe파일의 경로 C:\Users\flgus\Desktop\python project\danawa

import time
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_ 크롬 연결 *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
from selenium import webdriver
# browser에 크롬드라이버를 저장하였다. 이 browser을 통해 크롬 브라우저를 조작할 수 있다.
# 크롤링 할 페이지의 링크를 크롬드라이버가 잡으면 크롬 브라우저가 뜬다. (OK)
browser = webdriver.Chrome('C:/Users/flgus/Desktop/python project/danawa/chromedriver.exe')
url = "http://prod.danawa.com/list/?cate=12337356&src=adwords&kw=GA0252303&gclid=Cj0KCQjwssyJBhDXARIsAK98ITQnxx5Q90R-QBHs2zM9v5ydWohIFCHmneQl4GyJxAUCQBVCWaUeIOEaAjGtEALw_wcB"
browser.get(url)

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_ 상품정보 잡기 *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

# 웹페이지에서 상품정보 가져오기
"""
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
prod_items = soup.select('div.main_prodlist > ul.product_list > li.prod_item.prod_layer ')
"""
# 마지막 31번째 값은 랜덤값으로 들어가있기 때문에 제거해준다.
"""
del prod_items[-1]
title = prod_items[0].select('p.prod_name > a')[0].text.strip()
# strip()함수를 이용하여 양쪽 공백을 제거하였다.
# print(title)
# 스펙리스트도 가져온다.
spec_list = prod_items[0].select('div.spec_list')[0].text.strip()
# print(spec_list)
# 가격정보 가져온다.
price = prod_items[0].select('p.price_sect > a > strong')[0].text.strip()
# print(price)
"""
"""
prod_data = []
for prod_item in prod_items:
    try:    # 제목
        title = prod_item.select('p.prod_name > a')[0].text.strip()
    except:
        title = ''
    try:    # 스펙목록
        spec_list = prod_item.select('div.spec_list')[0].text.strip()
    except:
        spec_list = ''
    try:    # 가격정보
        price = prod_item.select('p.price_sect > a > strong')[0].text.strip()
    except:
        price = 0
    prod_data.append([title, spec_list, price])

print(len(prod_data))
print(prod_data)
"""
# 위의 소스를 함수로 구현하면
def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        try:  # 제목
            title = prod_item.select('p.prod_name > a')[0].text.strip()
        except:
            title = ''
        try:  # 스펙목록
            spec_list = prod_item.select('div.spec_list')[0].text.strip()
        except:
            spec_list = ''
        try:  # 가격정보
            price = prod_item.select('p.price_sect > a > strong')[0].text.strip()
        except:
            price = 0
        prod_data.append([title, spec_list, price])
    return prod_data

# 여러 페이지에 걸친 검색 크롤링
total_page = 5
prod_data_total = []

for page in range(1, total_page + 1):
    # 1. 검색 페이지 이동.
    # 여러 페이지를 수집하기 위해 버튼을 누른다
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    prod_items = soup.select('div.main_prodlist > ul.product_list > li.prod_item.prod_layer ')
    del prod_items[-1]
    prod_item_list = get_prod_items(prod_items)

    prod_data_total = prod_data_total + prod_item_list
    print(prod_item_list)
    print(page, '----------')

    try:
        page_buttons = browser.find_elements_by_css_selector(
            '#productListArea > div.prod_num_nav > div > div > *')
        page_buttons[page].click()
        time.sleep(3)

    except:
        # print(prod_data_total)
        print('완료되었습니다.')

data = pd.DataFrame(prod_data_total)
data.columns = ['상품명', '스펙 목록','가격']
data.to_excel('./files/1_danawa_crawling_result.xlsx', index = False)



