# 4. 데이터 시각화
# 데이터 시각화를 위해 matplotlib를 임포트하고 한글 깨짐 방지를 위한 코드를 추가

from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import seaborn as sns
import platform
import pandas as pd

# 그래프에서 한글 표기를 위한 글꼴 변경 (윈도우)

font_path = ''
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

data = pd.read_excel('./files/1_danawa_result2_6.xlsx', usecols=[0,1,2,3,5])
## 가격이 일시품절 된 데이터는 제외하고 보도록 한다.
mask = data['가격'].isin(['일시품절'])
data = data[~mask]

# 데이터가 없는 행은 삭제하기 위해 dropna 함수 사용
chart_data = data.dropna(axis = 0)
chart_data_sel = chart_data[:20]
a = len(chart_data_sel)
print(a)

# 총 71 개의 데이터
# 여기서 가격대 별 재생시간의 그래프를 그려보도록 한다.
# 가격과 재생시간의 최대값, 평균값 정리
max_price = chart_data_sel['가격'].max()
max_chargetime = chart_data_sel['충전시간'].max()
mean_price = chart_data_sel['가격'].mean()
mean_chargetime = chart_data_sel['충전시간'].mean()

plt.figure(figsize=(20,10))
plt.title("노이즈캔슬링 헤드폰 차트")
sns.scatterplot(x = '충전시간', y = '가격', hue = chart_data_sel['회사명'], data = chart_data_sel, legend = False)

plt.plot([0,max_chargetime],[mean_price,mean_price], 'r--', lw = 1)

plt.plot([mean_chargetime,mean_chargetime],[0,max_price], 'r--', lw = 1)

plt.show()

# 전체 데이터와 인기상위데이터를 비교한 결과, 가격이 낮을수록 충전시간이 적었고, 가격이 높을수록 충전시간이 길었다.
# 충전시간이 길다면 안 좋지 않을까 판단하고 분석을 했지만, 사실수록 가격이 비싸고 기능이 고급진것들이 충전시간이 긴게 아닌가 하는 생각이 든다.
# 노이즈캔슬링 헤드폰에 관심이 가 분석대상으로 삼았지만, 유무선여부와 노이즈캔슬링 기능의 정도, 노이즈캔슬링여부에 따라서 재생시간이 전부 달라지기때문에
# 단순 데이터 분석으로는 헤드폰의 성향을 제대로 분석하기 어려웠다. 물론 분석 결과가 명확한 주제에 대해서 분석하는 것도 좋지만, 이런 까다로운 주제에 대해 분석하는것도 공부가 될 수 있다.
