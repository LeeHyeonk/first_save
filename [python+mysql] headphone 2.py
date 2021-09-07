# 2. 데이터 전처리

# 데이터 수집이 된 파일을 토대로 데이터 전처리를 하자.
# 1. 회사명과 제품명 분리
# 2. 스펙목록에서 필요한 스펙으로 분류하고 단위를 통합. -> 카테고리, 재생시간, 충전시간

import pandas as pd
import re
# *-*-*-*-*-*-*-*- 크롤링 결과 가져오기 *-*-*-*-*-*-*-*-*-*-

datas = pd.read_excel('./files/1_danawa_crawling_result.xlsx')
datas.info()
datas.head()


# *-*-*-*-*-*-*-*- 1. 상품명에서 브랜드와 모델명 분류하기 *-*-*-*-*-*-*-*-*-*-
a = datas['상품명'][:10]
print(a)

company_list = []
product_list = []

for title in datas['상품명']:
    # 첫번째 공백에 대해서만 제목을 분리한다. 분리한 변수를 title_info에 저장
    title_info = title.split(' ', 1)
    company_name = title_info[0]
    product_name = title_info[1]

    company_list.append(company_name)
    product_list.append(product_name)

print('데이터의 갯수 : ', len(datas))
print('브랜드의 갯수 : ', len(company_list))
print(company_list[:5])
print('제품명의 갯수', len(product_list))
print(product_list[:5])

# *-*-*-*-*-*-*-*- 2. 스펙목록에서 데이터 추출하기 *-*-*-*-*-*-*-*-*-*-

a = datas['스펙 목록'][0]
print(a)
# ' / ' 좌우 공백과 슬래쉬를 기준으로 양쪽을 split 한다. 이 데이터는 리스트로 잘 정제된다.
print(datas['스펙 목록'][0].split(' / '))
spec_list = datas['스펙 목록'][0].split(' / ')
print(spec_list)

categoty =  spec_list[0]
print(categoty)

category_list = []
playtime_list = []
chargetime_list = []

"""
for spec in spec_list:
    if '재생시간' in spec:
        v1 = spec
    elif '충전시간' in spec:
        v2 = spec
print(v1)
print(v2)
vv1 = v1.split(' ')[1].strip()
if '(' in vv1:
    vv1 = vv1.split('(')[0]
vv2 = v2.split(' ')[1].strip()
print(vv1)
print(vv2)
"""


for spec_data in datas['스펙 목록']:
    # 카테고리 / 기준으로 분류하기 : 스펙 목록 을 / 기준으로 나누어서 spec_list에 저장한다.
    spec_list = spec_data.split(' / ')
    # print(spec_list)
    # 카테고리 추출하기 : list의 첫번째 요소를 category에 저장
    category = spec_list[0]
    category_list.append(category)

    # 재생시간 추출하기
    ## 재생시간과 충전시간 정보가 없는 제품을 위해 변수 생성
    playtime_value = None
    chargetime_value = None

    for spec in spec_list:
        if '재생시간' in spec:
            playtime_value = spec.split(': ')[1].strip()
            #if '(' in playtime_value:
            #    playtime_value = playtime_value.split('(')[0]
        if '충전시간' in spec:
            chargetime_value = spec.split(': ')[1].strip()
            if '약' in spec:
                chargetime_value = re.sub('약','',chargetime_value)
            if '시간' in spec:
                chargetime_value = re.sub('시간','',chargetime_value)
            if '이상' in spec:
                chargetime_value = re.sub('이상','',chargetime_value)
            if '~' in chargetime_value:
                text = chargetime_value.split('~')
                t1 = int(text[0])
                t2 = int(text[1])
                t = (t1 + t2) / 2
                chargetime_value = t
            try : chargetime_value = float(chargetime_value)
            except : print('변환 중 오류')
            #if '(' in chargetime_value:
            #    chargetime_value = chargetime_value.split('(')[0]

    playtime_list.append(playtime_value)
    chargetime_list.append(chargetime_value)


print("카테고리 ", len(category_list), category_list[0:10])
print("재생시간 ", len(playtime_list), playtime_list[0:10])
print("충전시간 ", len(chargetime_list), chargetime_list[0:10])

# *-*-*-*-*-*-*-*- 3. 가격을 숫자데이터로만 남기기 *-*-*-*-*-*-*-*-*-*-
p = []
for price in datas['가격']:
    if price != '일시품절':
        price = re.sub(',','',price)
        price = int(price)
    p.append(price)


datas['가격'] = p


pd_data = pd.DataFrame()
pd_data['카테고리'] = category_list
pd_data['회사명'] = company_list
pd_data['제품'] = product_list
pd_data['가격'] = datas['가격']
pd_data['재생시간'] = playtime_list
pd_data['충전시간'] = chargetime_list
pd_data.head()

pd_data.to_excel('./files/1_danawa_result2_6.xlsx', index=False)
