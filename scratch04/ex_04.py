"""
numpy의 행렬 관련 함수
"""
import numpy as np

# 행렬 A를 만들어 준다 (numpy를 사용할때는 numpy.ndarray 타입의 객체를 생성)
A = np.array([
    [1,2,3],
    [4,5,6]
])

B = np.array([
    [1,2],
    [3,4],
    [5,6]
])

print(A)
# Unlike the basic? list in Python, it prints in a more read-able format
print(B)
print(A.shape) #(2, 3) 이라고 하는 튜플을 리턴
print(B.shape) # (3,2) 이라고 하는 튜플을 리턴

# B.shape 을 풀어해쳐놓았다
nrows, ncols = B.shape
print(nrows, 'x', ncols)

# slicing: 원하는 행, 열의 원소들을 추출
# 기본 파이썬 연산자 에서는 list[row],[column], 하지만 numpy에서는 ndarray[row,column] - separated by a comma
print(A[0,0])
print(A[0,1])
print(A[1,2])

# row:col => this is called slicing
print(A[0,0:2]) # [1 2] -> 1,2,3 이 아니라 1,2의 리스트를 뽑아 주었다
                # 파이썬 스타일: 끝의 인덱스는 포함시켜주지 않아요! [0부터 1까지만 뽑아 주었어요]
# 파이썬의 기본 리스트에서는 A[1:2][0:3] 이런건 불가능했다
# ndarray 에서는 가능해요!
print(A[0:2, 0:2])
# slicing makes numpy handling data much easier!
print(A[:,0:2]) # 인덱스 0부터 1까지의 컬럼들로 이루어진 array
# 숫자 없이 colon 만 쓰면 0번행부터 마지막 까지 (마치 * 처럼...)
print(A[0,:]) #[1 2 3] # 인덱스 0번의 row의 원소들로 이루어진 array

# 항등행렬 (Identity Matrix)
identity_matrix = np.identity(3, dtype = int)
print(identity_matrix)
# In identity matrix, nrows = ncols (for always)
# so we should only give 1 n as a parameter
# if n = 3, numpy returns 3 * 3 automatically
# if we do not give dtype option, the default seems to be float (returns numbers like 1. 0. 0. (means 1.0 0.0 0.0))

# 전치 행렬 transpose Matrix
print(A.transpose())
# without having to give much, numpy does it for us!
print(B.transpose())

# 행렬 곱셈 n * m  m * k # the same must be the same
# returned value is n * k
# array 1 (n * m)
# array2 (m * k)
# the m values of both arrays must be the same
# the result = n * k
# one row of an array and one column of an array are multiplied and added
# numbers with the same indices - multiplied, and the products are added
# an expanded concept of dot product
print(A.dot(B))
print(B.dot(A))








