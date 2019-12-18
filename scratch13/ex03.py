"""
변수가 1개밖에 없을 때: 단순 선형 회귀
y = b + a1 * x1
변수가 여러개 일 때: 다중 선형 회귀
y = b + a1 * x1 + a2 * x2 + ...
다중 선형 회귀에서도 마찬가지로, y-절편과 a1,a2...들의 기울기가 중요하다
"""
import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(1216)
X1 = np.random.rand(100, 1)
print('X1 = ',X1[:5])
X2 = np.random.rand(100, 1) # 100X1
print('X2 = ',X2[:5])
# 숫자들이 0부터 1까지 존재한다

y = 3 + 4 * X1 + 5 * X2 + np.random.randn(100, 1) # y -> target (찾고자 하는 값)
print('y = ',y[:5])
X = np.c_[X1, X2] #combine columns x1 and x2 #data
print('X =',X[:5]) # returns a list of lists; a set of [x1,x2]

lin_reg = LinearRegression() # LinearRegression 객체 생성
# 학습데이터를 줘서 훈련시키기 -> 정답주기
lin_reg.fit(X,y) #model fitting, 학습
# X 와 y라고하는 데이터와 정답을 줘서 개수들을 찾아낼 수 있게 끔 훈련
print('절편(intercept) = ', lin_reg.intercept_)
print('계수(coefficeints) = ', lin_reg.coef_)
# 절편 & 계수 = 우리가 찾은 선형관계식

# 행렬로 계산해도 똑같은 값이 나와요 (연습해보기)

# 예측 데이터를

# 변수가 많아진다고 해서 예측률이 올라가지 않는다, 데이터 바이 데이터이기 때문에 해 봐야 안다
# 얼마든지 확장시켜 나갈 수 있어욤!

# 선형회귀에서 비선형회구로 넘어갈 수 있다!!!
# 선형회귀: 모두 1차항으로 이루어져있다
# 때로는 2차나 3차식인 경우에 만족하는 점을 쉽게 찾는 경우가 있을 수 도 있다
# 후자와 같은 경우가 비선형회귀 -> Linear regression으로 할 수 있다





