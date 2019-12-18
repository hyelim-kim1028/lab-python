"""
변수들간의 상호관계를 알고 싶은 때: 다시 for문을 돌려서 컬럼을 만들어 주는데
            -> 그 방법을 쉽게 만들어주는 것이 seaborn 이라는 패키지
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston

boston = load_boston()
X = boston['data'] #boston.data
y = boston['target'] #boston.target
features = boston['feature_names'] #boston.feature_names

# numpy.ndarray 타입을 pandas의 dataframe으로 변환
boston_df = pd.DataFrame(X, columns = features)
# 데이터 프레임에 컬럼 추가
boston_df['Price'] = y

print(boston_df.head())
print(boston_df.shape)
print(boston_df.describe())

columns = ['LSTAT', 'INDUS', 'NOX','RM','Price']
subset_df = boston_df[columns]
print(subset_df.head())
sns.pairplot(subset_df)
plt.show()
# 전체 데이터에 대한 동향을 보기 좋은 seaborn 패키지

# 전체 데이터 프레임에 관한 plot (14X14)
# sns.pairplot(boston_df)
# plt.show()

# 상관 행렬(correlation matrix): 상관 계수들로 이루어진 행렬
corr_matrix = subset_df.corr().round(2)
print(f'correlation matrix: {corr_matrix}')
# heatmap: 상관 계수(correlation coefficient)를 색깔로 표시해서 반/비례관계를 보여줌


cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr_matrix, annot=True, cmap = cmap)
plt.show()
# 공분산 = 1 이라서 대각선은 모두 1
# LSTAT & Price 는 진한 색깔로 (-0.76) 이니까, 반비례하다
# RM & Price 는 연한 색깔로 (0.6) 이니까, 비례하다 => ex05의 결과와 일치함
# 상관관계가 인관관계는 아니다 (반드시 원인과 결과는 아니다) -> 그냥 반/비례하는 경향을 보이는 것일 뿐

# 왜 heatmap이라고 이름을 붙였을까:
# 적외선 카메라로 촬영하면 열이 많은 부분이 더 진한 색깔로 표시되는 것과 비슷한 컨셉으로 이렇게 이름을 지음





