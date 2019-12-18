"""
Boston HOuse
"""
from sklearn import linear_model
from sklearn.datasets import load_boston
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

# 보스턴 집값 데이터 세트 로딩
from sklearn.preprocessing import StandardScaler

boston = load_boston()

# 데이터 탐색 - 그래프
X = boston.data
y = boston.target
print(X[:5])
print(X.shape, y.shape) #(506,13) (506,)
features = boston.feature_names #변수 이름들
print(features)
print('X[0] =',X[0]) #첫번째 행 -> 데이터 프레임 확인 # 전처리 필요? 아닌듯
print('y[0] =', y[0])

# 특성들을 스케일링 (표준화)
# scaler = StandardScaler()
# X_scaler = scaler.transform(X)

X_transpose = [column for column in zip(*X)]
print('X_transpose[0] =', X_transpose[0])

# 데이터 확인 차 그래프 그려보기
fig, ax = plt.subplots(3,5)
for row in range(3):
    for col in range(5):
        axis = ax[row, col]
        idx = 3 * row + col
        if idx > 15:
            break
        x = X[:, idx]
        axis.scatter(x,y)
        axis.set_title(features[idx])
# plt.show()

# 시도해보고 싶은 세트들: CRIM, RM, AGE, DIS

# 학습 세트/ 검증 세트 나눔

# CRIM
crim = X[:, np.newaxis, 0]
print('crim =', crim[:5])
print('crim.shape =', crim.shape)

crim_train = crim[:-56]
crim_test = crim[-56:]
y_train = y[:-56]
y_test = y[-56:]

# RM
rm = X[:, np.newaxis, 5]
print('rm =', rm[:5])
print('rm.shape = ', rm.shape)

rm_train = rm[:-56]
rm_test = rm[-56:]

# AGE
age = X[:, np.newaxis, 6]
print('age =', age[:5])
print('age.shape =', age.shape)

age_train = age[:-56]
age_test = age[-56:]

# 단순 선형 회귀
# CRIM
regr_crim = linear_model.LinearRegression()
regr_crim.fit(crim_train, y_train) # training set 을 학습 시킨다
print('CRIM_coefficients:',regr_crim.coef_)

#rm
regr_rm = linear_model.LinearRegression()
regr_rm.fit(rm_train, y_train) # trainining set 을 학습 시킨다
print('RM_coefficients:', regr_rm.coef_)

#age
regr_age = linear_model.LinearRegression()
regr_age.fit(age_train, y_train)
print('AGE_coefficients:', regr_age.coef_)

# 다중 선형 회귀
lin_reg = LinearRegression()
lin_reg.fit(X,y)
print('inctercept =', lin_reg.intercept_)
print('coefficient =', lin_reg.coef_)

# selected items
# multiple = X[:, np.newaxis, [0,5,6,7]]
# no need to include np.newaxis because it is already a 다차원 array
multiple = X[:, [0,5,6,7]]
print(multiple) # 이 표? 자체는 만들어 졌는데


lin_multiple = LinearRegression()
lin_multiple.fit(multiple, y) #여기서부터 문제 (정규화?)
print('intercept =', lin_multiple.intercept_)
print('coefficient =', lin_multiple.coef_)


# 검증 세트를 사용해서 예측

#CRIM
crim_pred = regr_crim.predict(crim_test)
print(crim_pred)

#RM
rm_pred = regr_rm.predict(rm_test)
print(rm_pred)

#age
age_pred = regr_age.predict(age_test)
print(age_pred)

# 예측한 그래프를 그려보기
# 절편, x에 대한 기울기 등등

#CRIM
plt.scatter(crim_test,y_test)
plt.scatter(crim_test,crim_pred)
plt.title('CRIM')
plt.show()

#RM
plt.scatter(rm_test, y_test)
plt.scatter(rm_test, rm_pred)
plt.title('RM')
plt.show()

# AGE
plt.scatter(age_test, y_test)
plt.scatter(age_test, age_pred)
plt.title('AGE')
plt.show()


# Linear Regression를 활용해서 Mean Square Error & R2-score 계산

#CRIM
crim_mse = mean_squared_error(crim_test, crim_pred)
print(crim_mse)

crim_r2 = r2_score(crim_test, crim_pred)
print(crim_r2)

#RM
rm_mse = mean_squared_error(rm_test, rm_pred)
print(rm_mse)
rm_r2 = r2_score(rm_test, rm_pred)
print(rm_r2)

#AGE
age_mse = mean_squared_error(age_test, age_pred)
print(age_mse)
age_r2 = r2_score(age_test, age_pred)
print(age_r2)

#so far, age was the most appropriate of all