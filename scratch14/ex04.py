import numpy as np

# numpy.c_ (column bind) 와 numpy_r (row bind)의 비교
a = np.array([1,2,3])
print(a)
b = np.array([4,5,6])
print(b, type(b), b.shape) # shape에서 1차원 array & 2차원 array에 따라 출력 방식이 다르다
                           # (row, column) : 2차원 array
                           # (원소개수, ): 1차원 array # not 행 개수!

c = np.c_[a,b]
print(c, type(c), c.shape)

d = np.r_[a,b]
print(c, type(d), d.shape)

e = np.array([[1,2,3],
              [4,5,6]])
f = np.array([[10, 20],
              [40, 50]])

print(np.c_[e, f]) # e와 f의 row 개수가 같아야 column 방향으로 붙일 수 있음
# print(np.r_[e, f]) # e와 f의 column 개수가 다르면 row 방향으로 붙일 수 없음
# 차원이 서로 안맞는다 (그래서 옆으로 붙이는 것은 안되는데, 밑으로 붙이는 것은 된다)

g = np.array([[100, 200, 300]])
# 컬럼의 갯수는 같지만, row의 갯수가 다르기때문에 column 방향 (오른쪽) 으로 붙일 수 없다
# 반대로 c_는 안되지만, r_은 된다
# print(np.c_[e, g])
print(np.r_[e,g]) # column의 갯수가 같아야 밑으로 붙일 수 있음

#error!
# when g = np.array([100, 200, 300]), there occurred an error for having different dimension of array
# ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)

# (2, 3) shape의 모든 원소가 1인 array를 생성해서 출력: A
print(np.ones((2,3), dtype = np.int))

# (2, 3) shape의 모든 원소가 0인 array를 생성해서 출력: B
print(np.zeros((2,3), dtype = np.int))

# (3, 2) shape의 원소는 1 ~ 6인 array를 생성해서 출력
print(np.arange(1, 7).reshape((3,2)))

# (3, 2) shape의 난수들로 이루어진 array를 생성해서 출력
print(np.random.random((3,2)))


# 항등행렬: (1 0) (a b) = a b
#             0 1   c d    c d
# 행렬에서 A dot B 와 B dot A 는 같지 않다. 하지만, 항등행렬은 항상 같은 결과를 준다.
# numpy에서 항등행렬을 만드는 함수를 찾아보아라
# 역행렬은 항등행렬과 반대되는 개념 (역수 -> 곱해서 1이되는것 => 3 * (1/3) = 1; 3의 역수는 1/3)

"""다음과 같은 결과가 나올 수 있도록 
numpy를 사용하지 않고 add(x, y), subtract(), multiply(), divide(), dot() 함수를 구현
|1 2| + |5 6|= |6  8 | 
|3 4|   |7 8|  |10 12|


|1 2| - |5 6|= |-4 -4| 
|3 4|   |7 8|  |-4 -4|

|1 2| * |5 6|= |5  12| 
|3 4|   |7 8|  |21 32|

|1 2| / |5 6|= |0.2   0.333| 
|3 4|   |7 8|  |0.428 0.5  |

|1 2| @ |5 6|= |19 22| 
|3 4|   |7 8|  |43 50|
위의 결과와 같은 결과를 주는 numpy 코드를 작성
"""

# numpy를 사용하지 않고 add(x, y), subtract(), multiply(), divide(), dot() 함수를 구현

array1 = np.arange(1,5).reshape((2,2))
array2 = np.arange(5,9).reshape((2,2))
# print(array1[0, 1])


# # 이렇게 만드니까 행끼리의 계산이 아닌 그냥 두 array를 물리적으로 붙여줌
# def add(x,y):
#     return x + y

def add(x,y):
    for n in range(len(x)):
        for m in range(len(y)):
           x[n,m] + y[n,m]
    return x + y

def subtract(x,y):
    for n in range(len(x)):
        for m in range(len(y)):
            x[n,m] - y[n,m]
    return x - y

def multiply(x,y):
    for n in range(len(x)):
        for m in range(len(y)):
            x[n,m] * y[n,m]
    return x * y


def divide(x,y):
    for n in range(len(x)):
        for m in range(len(y)):
            x[n,m] * y[n,m]
    return x/y

# my_solution
# def dot(x,y):
#     dot_sum = 0
#     for s in range(len(x)):
#         dot_sum += multiply[s]
#         for n in range(len(x)):
#             for m in range(len(y)):
#                 multiply = x[n, m] * y[n, m]
#     return dot_sum
#
# print(f'dot_sum = {dot(array1,array2)}')

# teacher's solution
# 앞에 있는 행렬의 컬럼 갯수와 뒤에있는 행렬의 열의 갯수가 같아야 dot product이 가능하다
# def my_dot(A, B):
#     """ 두 행렬 A와 B의 dot 연산 결과를 리턴
#         dot_ik = sum[a_ij * b_jk] """
#     print('A.shape =',A.shape) # tuple 형태로 되어 있어서 shape함수 사용이 가능했다
#     print('B.shape =',B.shape)
#     if A.shape[1] != B.shape[0]:
#         raise ValueError('A의 column과 B의 row 개수는 같아야 함!')
#     n_row = A.shape[0]     # dot 결과 행렬의 row 개수
#     n_col = B.shape[1]     # dot 결과 행렬의 column 개수
#     # dot product의 결과는 첫번째 행렬의 row 갯수과 nrow가 되고, 두번째 행렬의 column개수가 column 개수가 된다
#     temp = A.shape[1] # 각 원소들끼리 곱한 결과를 더하는 회수 # 앞의 행렬의 컬럼 갯수 = 뒤의 행렬의 row 개수
#     numbers = [] #결과값들을 저장할 리스트
#     for i in range(n_row): # A행렬의 row 개수만큼 반복
#         for k in range(n_col): #B 행렬의 column 개수만큼 반복
#             n = 0
#             for j in range(temp):
#                 # dot 결과 행렬의 [i, k]번째 원소의 값을 계산
#                 n += A[i, j] * B[j, k]
#             numbers.append(n) #[i, j] 번째 원소를 리스트에 추가
#     # 결과를 (i, k) 모양의 행렬로 변환해서 리턴
#     return np.array(numbers).reshape(n_row, n_col)


# Method B
def my_dot(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError('A의 column과 B의 row 개수는 같아야 함!')
    n_row = A.shape[0]
    n_col = B.shape[1]
    temp = A.shape[1]
    result = np.zeros((n_row, n_col)) # 변수 하나에 row와 column을 줘야하기 때문에 tuple로 묶는다; 원소들은 모두 0으로 채워진다
    for i in range(n_row):
        for k in range(n_col):
            n = 0
            for j in range(temp):
                n += A[i, j] * B[j, k]
            result[i,k] = n
    return result




A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(my_dot(A, B))
print(A @ B) # numpy array에서 @을 사용하면 dot을 해준다

"""
항등 행렬(Indentity matrix): 대각선의 원소는 1이고, 나머지 원소는 0인 정사각행렬 
    A @ I = I @ A = A를 만족 # numpy.identity(n, dtype = None)  
역행렬(Inverse matrix): A @ A- = A- @ A = I를 만족하는 행렬 # numpy.linalg.inv()
전치 행렬(Transpose matrix): 행렬의 row와 column을 서로 바꾼 행렬 array1.transpose() 
# 함수를 찾아서 행렬을 넣어보기 
"""
# identity matrix
print(np.identity(2))
id1 = np.identity(2)
print(array1 * id1)

# Inverse Matrix
print(np.linalg.inv(array1))
inverse1 = np.linalg.inv(array1)
# print(dot(array1, inverse1)) # 움? 왜 None 이지

# Transpose Matrix
print(array1.transpose())
