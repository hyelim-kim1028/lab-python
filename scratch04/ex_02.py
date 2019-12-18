"""
numpy package 를 사용한 vector 연산
"""
import math

import numpy as np

print('numpy version: ', np.__version__)

# 두 백터의 덧셈
v = [1,2] # type: class list
print(type(v))
print('v =', v)

w = [2,3]
print('w =',w)

z = [3,4]
print('z =',z)
print (v + w)
# + 연산자는 extend 함수와 비슷한 기능
# + 연산자는 v 나 w를 변경하지 않고, 새로운 리스트를 리턴
# v.extend(w) 함수는 v를 변경함

print(v + w + z) # list는 + 연산을 사용할 수 있음
# 같은 letters 가 있어도 모두 다 중복 출력한다

# print(w - z)
# list 는  - 연산을 사용할 수 없음!
# subtraction not allowed with strings

v.extend(w) #the same as v + w
print(v)

# v.extend(w,z) #TypeError: extend() takes exactly one argument (2 given)
# print(v)

# v + w 는 v 변하지 않고, w 도 변하지 않고 아예 새로운 리스트를 변환해준다
# 하지만 v.extend(w) 는 v 가 아예 바뀐다 v = [1,2,2,3] 로 바뀌어버리는 것

# numpy 패키지의 ndarray 타입을 사용
# n-dimensional array(n차원 배열)
v = np.array([1,2]) #1차원 배열
print('type:', type(v))
print(v)
# (x1,y1) 2 차원 백터
# 여기서의 차원은 배열안에 배열이 있느냐, 없느냐
print('dimension: ', v.ndim)
print('shape: ', v.shape) #(2,) # 배열의 원소의 갯수를 반환해준다

v2 = np.array([
    [1,2],
    [3,4]
])
print('v2 type:',type(v2))
print('v2 dimension:',v2.ndim) # 2차원
# 배열: 여러개의 원소들을 하나로 저장한 것
# 파이썬에서는 이걸 list 라고 부르고, numpy에서는 array 라고 부른다고 생각해도 되지만, 기능이 조금 다르다
# dimension - 배열안에 배열을 갖느냐

v3 = np.array([
    1,
    [1,2],
    [3,4]
])
print('v3 type:',type(v3))
print('v3 dimension:',v3.ndim) # 1차원

# 2차원이 되려면 array가 가지고 있는 모든 원소가 다 2차원이 되어야한다
v4 = np.array([
    [1,5],
    [1,2],
    [3,4]
])
print('v4 type:',type(v4))
print('v4 dimension:',v4.ndim) # 2차원
print('v4 shape: ', v4.shape)

# shape()
# 1차원 ndarray인 경우 shape은 (원소 개수,)
# 2차원 ndarray인 경우 shape은 (행의 갯수, 컬럼의 갯수)

# ndarray 는 원소들 다음에 ',' 가 없고, 줄이 바뀌어져서 출력되어있다
v = np.array([
    [1,2],
    [3,4],
    [5,6]
])
print(v)

# 이렇게하면 ',' 를 원소들 다음에 넣어줘야하고, 같은 줄에 출력해준다
l = [
    [1,2],
    [3,4],
    [5,6]
]
print(l)

# ndarray 타입을 사용한 벡터 연산
# v = np.array([1,2])
# w = np.array([3,4,5]) #ValueError: operands could not be broadcast together with shapes (2,) (3,)
# different in len. doesn't work

v = np.array([1,2,3])
w = np.array([3,4,5])
vector_add = v + w
print('vector add = ', vector_add)
# added by column and returned an array of the sum
vector_sub = v - w
print('vector subtract = ',vector_sub)

vectors = np.array([
    [1,2],
    [3,4],
    [5,6]
])
# 2차원 array 가 된다
np_sum = np.sum(vectors) # 2차원 배열의 모든 원소들의 합
print('np_sum =', np_sum) #np_sum = 10
# np.sum 이 모든 원소를 다 더해주었다
# numpy 의 기본은 array


# axis = 0: 2차원 배열의 각 컬럼들의 합으로 이루어진 배열
np_sum_by_col = np.sum(vectors, axis = 0)
# sum(a, axis=None, dtype=None, out=None, keepdims=np._NoValue, initial=np._NoValue, where=np._NoValue)`
# a for array
print('np_sum_by_col =', np_sum_by_col) #np_sum_by_col = [4 6]
# axis = 0 이 컬럼 방향
# 아래로 아래로 계산해서 [4,6] 을 반환해준 것 # 이거하고 [5,6] 추가해줌

# axis = 1: 2차원 배열의 각 행(row)들의 합으로 이루어진 배열
np_sum_by_row = np.sum(vectors, axis = 1)
print('np_sum_by_row =', np_sum_by_row)
# axis = by row / 행 방향으로 더한다
# 행의 갯수만큼 출력해준다

# 컬럼, 행별로 평균 계산하기
np_mean = np.mean(vectors)
print('np_mean =', np_mean)
np_mean0 = np.mean(vectors, axis = 0)
print('np_mean0_by_column =', np_mean0) #np_mean0 = [3. 4.] -> 3.0, 4.0 이라는 뜻
np_mean1 = np.mean(vectors, axis = 1)
print('np_mean1_by_row =', np_mean1) # np_mean1 = [1.5 3.5 5.5] -> 1.5, 3.5, 5.5

v = [1,2,3]
scalar_mul = 3 * v
print('scalar_multiplication = ', scalar_mul) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# 리스트를 3번 반복해서 출력해주었다
# np.array 로 바꿔주지 않아서 이렇게 출력된 것

v = np.array([1,2,3])
scalar_mul = 3 * v
print('scalar mulitplication_np.array =', scalar_mul) #[3 6 9]
scalar_div = v/3
print('scalar division =', scalar_div)
# [0.33333333 0.66666667 1.        ]
scalar_div = 3/v
print('scalar division =', scalar_div)
# 원소의 갯수만큼 반복해준다
# numpy.array 에서는 // 이나 % 도 가능하다

# dot product
v = np.array([1,2])
w = np.array([3,4])
print('dot = ', v.dot(w)) # 11 -> (1 * 3) + (2 * 4)

# numpy 를 이용해서 vector 의 크기를 비교하는 함수 만들기
def norm(v):
    return math.sqrt(v.dot(v))
# 빨간줄 alt + enter

v = np.array([1,1]) #sqrt(2)
print('norm =', norm(v))

# numpy를 이용한 두 벡터 사이의 거리

def dist(v,w):
    # return math.sqrt(vector_sub(v,w)**2)
    return math.sqrt((v-w).dot(v-w))
                    # 우와ㅏㅏ 그냥 앞뒤로 v-w 줘서 제곱해줌;;ㅎㄷ
      # return norm(v-w)

v = np.array([1,2])
w = np.array([3,4])
print('distance =', dist(v,w))





























