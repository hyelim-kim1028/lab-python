"""
mpg.csv 파일을 읽어서, 경사 하강법을 사용한 선형 회귀식을 찾음
cty = slope * displ + intercept
# intercept: 절편
# intersect: 교차
"""
import os
import random
import matplotlib.pyplot as plt

from scratch04.ex01 import vector_mean
from scratch08.ex03 import gradient_step
from scratch08.ex04 import minibatches, linear_gradient

print(os.getcwd()) # 이거랑 R에서 작업해줘야 에러가 나지 않는다!

with open('mpg.csv', encoding = 'UTF-8') as f:
     # with - as (read,write) 구문 파일을 열고 close를 자동으로 해주는 구문
     f.readline() # 첫번째 라인을 읽고 버림 (아무데도 저장하지 않는다) - 컬럼 이름들 remove
     # 한 줄씩 읽어서 그 줄의 앞 뒤 공백들 (줄바꿈, \n)을 제거하고, ',' 로 문자열을 분리해서 만든 리스트를 df에 저장
     df = [line.strip().split(sep = ',') for line in f]

# df = [line for line in f]
# ['"1","audi","a4",1.8,1999,4,"auto(l5)","f",18,29,"p","compact"\n', '"2","audi","a4",1.8,1999,4,"manual(m5)","f",21,29,"p","compact"\n', '"3","audi","a4",2,2008,4,"manual(m6)","f",20,31,"p","compact"\n'
# 자세보면 ' ' 작은 따옴표가 가장 바깥에 있고, \n 줄 바꿈 해줌 ->
# 하지만 우리는 컬럼별로 문자열을 짤라야하고, 쉼표로 짜름

# df = [line.split(sep = ',') for line in f]
# [['"1"', '"audi"', '"a4"', '1.8', '1999', '4', '"auto(l5)"', '"f"', '18', '29', '"p"', '"compact"\n'], ['"2"', '"audi"', '"a4"', '1.8', '1999', '4', '"manual(m5)"', '"f"', '21', '29', '"p"', '"compact"\n'], ['"3"', '"audi"', '"a4"', '2', '2008', '4', '"manual(m6)"', '"f"', '20', '31', '"p"', '"compact"\n'], ['"4"', '"audi"', '"a4"', '2', '2008', '4', '"auto(av)"', '"f"', '21', '30', '"p"', '"compact"\n'], ['"5"', '"audi"', '"a4"', '2.8', '1999', '6', '"auto(l5)"', '"f"', '16', '26', '"p"', '"compact"\n']]
# ['"1"', '"audi"', '"a4"', '1.8', '1999', '4', '"auto(l5)"', '"f"', '18', '29', '"p"', '"compact"\n'] 이렇게가 1개인 리스트로 만들어줌

# df = [line.strip().split(sep = ',') for line in f]
# 모든 줄의 끝에는 줄바꿈 \n이 들어가 있음 => not from the original data so it must be removed
# [['"1"', '"audi"', '"a4"', '1.8', '1999', '4', '"auto(l5)"', '"f"', '18', '29', '"p"', '"compact"'], ['"2"', '"audi"', '"a4"', '1.8', '1999', '4', '"manual(m5)"', '"f"', '21', '29', '"p"', '"compact"'],
# 줄바꿈 대행 문자 (\n)이 들어가지 않았다

#  df = [line.strip().split(sep = ',') for line in f]
# 문제 2: '"1"' length = 1 인 1에서  length = 3 인 "1" 으로 인식해버렸다
# 처음에 csv파일에서 문자열로 구분하기 위한 "" 이 데이터 그 자체로 들어가버렸다
# 예를들어 separator = ','로 두면 텍스트 마이닝에서 데이터에 ',' 가 들어가 버리면 하나의 데이터가 되는 것과 같다
# [['"1"', '"audi"', '"a4"', '1.8', '1999', '4', '"auto(l5)"', '"f"', '18', '29', '"p"', '"compact"'], ['"2"', '"audi"', '"a4"', '1.8', '1999', '4', '"manual(m5)"', '"f"', '21', '29', '"p"', '"compact"'],

print(df[0:5]) # 데이터 프레임 확인
# 배기량(displ)과 시내 연비(cty)만 추출 - 데이터 타입: 숫자
displ = [float(row[2]) for row in df]
cty = [float(row[7]) for row in df]
displ_cty = [(d,c) for d,c in zip(displ, cty)]
print(displ_cty[0:5])
# [(1.8, 18.0), (1.8, 21.0), (2.0, 20.0), (2.0, 21.0), (2.8, 16.0)]

# 미니배치가 가장 일반적으로 적용될 수 있음 (ex04, lines 101-107) 그래서 그 걸 함수 함수로 만듬
def mini_batch_gd(dataset,
                  epochs, # 몇번 반복할 것인가
                  learning_rates = 0.001, # 어떤 비율 만큼씩 이동시킬 것 인가 # in terms of returned value, 0.001 > 0.01 (the prior one was better than the other)
                  batch_size = 1, # 기본값 1, 점 1개에 대해서 센터값 다시 계산하고 반복 (스토케스틱이 기본값이다)
                  shuffle = True):  # 셔플 -> 에포크를 다시 줄 때마다 계산 할 것인지 여부
   dataset = dataset.copy() # 원본 데이터를 복사해서 사용
   # AUNQUE LO MEZCLAMOS, LOS DATOS DE ORIGINAL VERSION SE QUEDA
   # 찾으려고하는 직선의 기울기와 절편의 초깃값
   theta = [random.randint(-10,10),
            random.randint(-10,10)]
   print('theta 초깃값:', theta)
   for epoch in range(epochs): # epoch 회수만큼 반복
        if shuffle:
            random.shuffle(dataset) # 무작위로 순서를 섞음
        mini_batch = minibatches(dataset, batch_size, shuffle) # dataset (that has the values of x & y)
        for batch in mini_batch: # 미니 배치 크기만큼 반복
            # 미니 배치 안의 점들에 대해서 gradient 들을 계산
            gradients = [linear_gradient(x,y,theta)
                         for x, y in batch]
            # gradient 들의 평균을 계산
            gradient = vector_mean(gradients)
            # gradient를 사용해서 파라미터 theta 변경
            theta = gradient_step(theta, gradient, -learning_rates) # 최솟값을 찾는 것이기 때문에 learning rates 에 마이너스 값을 줬다
   return theta

# stochastic 경사 하강법
print("===== Stochastic Gradient Descent ======")
theta_stochastic = mini_batch_gd(displ_cty, epochs = 200, shuffle= False) #어짜피 stochastic 은 모든 원소를 한번씩 다 하는 거기때문에
print(theta_stochastic)
# returned value: 최깃값에 상관없이 비슷한 값으로 최저값을 찾아간다

print("===== batch gradient descent =====") # 하나씩 뽑아서 gradient 계산하고 theta 변경, 반복
theta_batch = mini_batch_gd(displ_cty, epochs = 5000, batch_size= len(displ_cty), learning_rates = 0.01, shuffle = True)
# batch = gradient 평균을 계산할 때, 몇개의 gradient 를 가지고 할까? 전체집합
# 그래서 batch_size 에 전체집합 (dipl_cty) 만큼 길이로해서 계산
print(theta_batch)
# 200번해서는 잘 안나옴

# Machine Learning 에서 전체 데이터 세트를 훈련 세트와 검증 세트로 나누어준다. 그리고 훈련 세트로 훈련 시켜주면서 제일 잘 찾는거를 찾으려고
# 지금 하는 것: 모든걸 트레이닝 세트에 놓고 맞춰가는 가정을 해보는 것

# mini batch gradient descent
print('===== mini batch gradient descent =====')
theta_mini = mini_batch_gd(displ_cty,
                           epochs = 1000,
                           learning_rates= 0.01,
                           batch_size= 32,
                           shuffle = True)
print(theta_mini)
# learning rate 0.001 -> 0.01  에서 0.01 이 성능이 더 좋았다

def linear_regression(x, theta):
    slope, intercept = theta
    return slope * x + intercept # y = ax + b

# 산점도 그래프
plt.scatter(displ, cty) # 대략적인 linear line 이 그려진다

# 라인 그래프
ys_stochastic = [linear_regression(x, theta_stochastic)
                 for x in displ] # 이거 그려주려고 linear regression 함수 만든것
plt.plot(displ, ys_stochastic, color = 'red',
         label = 'Stochastic GD')

ys_batch = [linear_regression(x, theta_batch)
            for x in displ]
plt.plot(displ, ys_batch, color = 'green', label = 'Batch GD')

ys_mini = [linear_regression(x, theta_mini)
           for x in displ]
plt.plot(displ, ys_mini, color = 'yellow', label = 'Mini GD')

plt.xlabel('displacement(cc)')
plt.ylabel('efficiency(mpg)')
plt.title('Fuel Efficiency (연비) vs Displacement(배기량)')
plt.legend()
plt.show()









