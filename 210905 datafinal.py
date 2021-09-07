# 3. 데이터 분석

# 데이터 전처리 완료된것을 분석한다. -> 단순 표로만 출력

import pandas as pd
import numpy
import re

# row 생략 없이 출력
pd.set_option('display.max_rows', None)
# col 생략 없이 출력
pd.set_option('display.max_columns', None)

# 재생시간은 다양한 옵션을 사용함에 따라 달라지므로 분석을 하기에 적합하지 않다.
# 따라서 재생시간을 제외한 나머지 열만 불러오도록 한다.
data = pd.read_excel('./files/1_danawa_result2_6.xlsx', usecols=[0,1,2,3,5])

# 1. 가격순 정렬 - 내림차순
## 가격이 일시품절 된 데이터는 제외하고 보도록 한다.
print('------------가격 순 정렬----------------')
mask = data['가격'].isin(['일시품절'])
data = data[~mask]

print(data['가격'])

top_list1 = data.sort_values(['가격'], ascending=False)
print(top_list1.head())


print('------------충전시간 정렬----------------')
# 충전시간 기준 정렬 - 내림차순
## 충전시간이 NaN 인 값은 제외한다
mask = data['가격'].isin([None])
data = data[~mask]
top_list2 = data.sort_values(['충전시간'], ascending=False)
print(top_list2.head())

print('------------충전시간 + 가격 정렬----------------')
top_list3 = data.sort_values(['충전시간','가격'], ascending=False)
print(top_list3.head())

print('------------평균값 정리----------------')
price_mean = 0
charge_mean = 0
try : price_mean = data['가격'].mean()
except : print('오류발생')

try : charge_mean = data['충전시간'].mean()
except : print('오류발생')

print('가격 평균값 : ', round(price_mean,2), '원')
print('충전시간 평균값 :', round(charge_mean,2), '시간')

#가성비 좋은 제품은 가격과 충전시간이 적은것으로 설정해본다.
print('------------가성비 좋은 제품 탐색----------------')

condition_data = data[
    (data['가격'] <= price_mean)
    &
    (data['충전시간'] <= price_mean)
]
print(condition_data)

# 데이터 시각화