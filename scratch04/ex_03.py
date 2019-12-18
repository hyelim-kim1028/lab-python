"""
2차원 리스트(파이썬 기본 타입) 를 이용한 행렬
행렬(Matrix): 행과 열로 이루어진 데이터들
행렬에는 차원(shape) 이 있다 (shape 은 행 * 열로 나타낸다)
"""

def shape(matrix):
    """
    행렬의 행과 열의 개수를 tuple 형태로 리턴
    :param m: 행렬
              (행의 갯수가 n개이고 열의 갯수가 m개인 2차원 리스트)
    :return: (n, m) # tuple♡
    """
    # teacher's solution
    nrows = len(matrix) # 행의 개수
    ncols = len(matrix[0]) #열의 개수
    return nrows, ncols

    # my_thought
    # for row in matrix:
    #     for column in matrix:
    #         count = count(matrix[row,column])
    #         matrix[row] = ''
    #         matrix[column] = ''
    # return count

def get_row(matrix, index):
    """
    주어진 행렬(matrix) 에서 index에 해당하는 row를 리턴
    :param matrix: n * m 행렬
    :param index: 행 번호
    :return: vector (원소가 m개인 리스트)
    """
    nrow = len(matrix),(matrix[index])
    # nrow = matrix[index] - this is the correct one
    return nrow

def get_column(matrix, index):
    """
     주어진 행렬에서 index에 해당하는 column을 리턴
    :param matrix: n * m 행렬
    :param index: 행 인덱스
    :return: 벡터(원소 n개인 1차원 리스트)
    """
    # teacher's solution
    result = []
    for x in matrix:
        result.append(x[index])
    return result
    # return [x[index] for x in matrix]
    # matrix A 에서 x 를 꺼내면 [1,2,3] 단위로 꺼내지고, 거기서 원하는 x[index] 인덱스만 뽑아내기

    # my thought
    # ncol = []
    # for index in matrix:
    #     matrix.append(matrix[index])
    # return ncol

def make_matrix(nrows, ncols, fn):
    """
    함수 fn의 리턴값들로 이루어진 nrows * ncols 행렬을 생성
    :param nrows: 행의 개수
    :param ncols: 열의 개수
    :param fn: 함수 (fn (nrows, ncols) = 리턴값 in number) => 이렇게 생긴 함수는 아무거나 넣어도 되는 함수,,,
    :return: nrows * ncols 행렬 만들기
    """
    # mat = [] #빈 리스트 생성 -> 2차원 리스트
    # for i in range(nrows): # row 만들기 (행의 개수만큼 반복)
    #     rowlist = [] # create an empty list -> 행렬에 추가될 행. 1 차원 리스트
    #     for j in range(ncols): # col 만들기 (열의 개수만큼 반복)
    #         rowlist.append(fn(i,j)) #[]  아니고 () # row에 아이템을 추가 # the same as creating a row
    #         # isn't it logical to give () not [] when we are giving the name of a function?! Que tonteria huhuuh
    #     mat.append(rowlist) #matrix에 row 를 append
    # return mat
    return[[fn(i,j) for j in range(ncols)] for i in range(nrows)]


    # my thoughts
    # 오마쥬 from https://stackoverflow.com/questions/40120892/creating-a-matrix-in-python-without-numpy
    # pseudo code (프로그램이 어떻게 흘러가는지만 보여주는 코드) / 의사(유사)코드
    # mat = []
    # for i in range(nrows): # row 만들기
    #     rowlist = []
    #     for j in range(ncols): # col 만들기
    #         rowlist.append(fn[nrows, ncols]) #여기다가 뭘 넣어줘야할 지를 모르겠다 예예
    #     mat.append(rowlist)
    # return mat

    # 오마쥬: https://www.dreamincode.net/forums/topic/413327-creating-nxm-matrix-without-numpy/
    # return [([fn] for row in range(len(nrows))) for column in range(len(ncols))]


# 항등행렬 (Identity Matrix)
# https://kr.mathworks.com/help/matlab/ref/eye.html?lang=en

def identity(x,y):
    # result = 0
    #     # if x == y:
    #     #     result = 1
    #     # else:
    #     #     reult = 0
    # 삼항연산자 (항이 3개다!)
    # result = 1 if x == y else 0 #elif not allowed!
    # # 1           2        3
    # return result
# In Java, we can put it this way: 변수 = if 조건 ? 값 (조건이 참일 때) : 값
    # to put it simplier
    return 1 if x == y else 0
# In lambda expression we can put it:
identity_matrix = make_matrix(3,3,lambda x,y: 1 if x == y else 0)
print('identity_matrix =',identity_matrix)
# when we have x,y we return 1 value (this is lambda!)


"""
전치행렬(transpose) 
https://m.blog.naver.com/PostView.nhn?blogId=qbxlvnf11&logNo=221402190993&categoryNo=67&proxyReferer=https%3A%2F%2Fwww.google.com%2F
# intercambio entre los row y las columnas 
"""

# def transpose(matrix):
"""
   주어진 행렬에서 행과 열을 뒤바꾼 행렬 (전치 행렬)
   :param matrix: n * m 행렬
   :return: m * n 행렬 (n = 행, m = 열)
   """
    # teacher's solution 1
    # nrows, ncols = shape(matrix)
    # t = make_matrix(ncols, nrows, lambda x,y: matrix[y][x])
    #                                         # 순서를 바꿔줘야 뒤바뀐 행렬을 찾을 수 있을테니!
    # return t

    # teacher's solution2
    # but what if we do not have any function at hand?
# def transpose(matrix):
#     nrows = len(matrix)  # 원본 행렬의 행이 개수
#     ncols = len(matrix[0])  # 원본 행렬의 열의 개수

        # t = []  # 전치 행렬을 위한 비어있는 리스트
        # for j in range(ncols):  # 원본 행렬의 열 개수 만큼 반복
        #     # 원본 행렬에서 j 번째 컬럼을 꺼낸 후 전치 행렬의 행(row)로 추가
        #     t.append(get_column(matrix, j))  # append 자체가 행을 추가하는 것 처럼 (가로로 나오니까)
        # return t
    # 왜 안되지 # returned transpose = None

    # we can write list comprehension for lines 138-142
    # return [get_column(matrix, j) for j in range(ncols)]
    # This did not work 2222 (indentation error!!)

# teacher's solution 3
# def transpose(matrix):
#         nrows = len(matrix)
#         ncols = len(matrix[0])
#         t = []
#         for j in range(ncols):
#             t_row = [] # 전치 행렬의 행이 될 리스트
#             for i in range(nrows):
#                 t_row.append(matrix[i][j])
#                 # row의 갯수만큼 원소들을 꺼내서 col로  append
#                 # 그래서 matrix [행번호] [열번호] 를 꺼내서 넣어야한다
#             t.append(t_row)
#         return t
          # to write it like a list comprehension lines 154~
def transpose(matrix):
        nrows = len(matrix)
        ncols = len(matrix[0])
        return [[[matrix[i][j]] for i in range(nrows)] for j in range(ncols)]
                                                        # 원본 행렬의 col 만큼


    # my thoughts
    # n = len(matrix)
    # m = len(matrix[0])
    # matrix = m * n
    # return[[(m,n) for n in range(len(matrix))] for m in range(len(matrix[0]))]
    # return[[(n,m) for m in len(matrix))] for n in len(matrix[0])]

# column 을 뽑아서 row로 가져다 넣으면 된다 (and vice-versa)
# 우리가 만든 function을 써서 만들어보기!

def transpose(matrix):
    print('unpakcing 연산자 *를 사용한 transpose')
    t = []
    for col in zip(*matrix):
        t.append(col) #to be returned in list format: t.append(list(col))
    return t

# *matrix 니까 matrix 의 행들을 튜플 형태로 리턴 되고, 거기서 각 튜플의 인덱스들을 빼서 append 시켜주니까 col 처럼 완성
# 그래서 이번에는 리스트안에 리스트가 들어간 형태가 아니라 튜플이 들어간 형태로 리턴되었다

if __name__ == '__main__': # 이걸 해줘야 다른데서 안나오니까
    # 2 * 3 행렬
    A = [
        [1,2,3],
        [4,5,6]
    ]

    # 3*2 행렬(row = 3, column = 2)
    B = [
        [1,2],
        [3,4],
        [5,6]
    ]

    print(A)
    print(B)

print('shape A =',shape(A))
print('shape B =',shape(B))
print('get row = ',get_row(A,0))
print('get column =', get_column(A,1))
print('get matrix =', make_matrix(2,2,lambda i,j: i * j))
# or we could just give the name of a function in the place of lambda
print('get Identity Matrix =', make_matrix(4,4,identity))
print('transpose =', transpose(A))
print('transpose =', transpose(B))

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
for x,y,z in zip(a,b,c):
    print(x,y,z)

# unpacking 연산자: *
print('A =', A)
# A = [[1, 2, 3], [4, 5, 6]]
# 2개의 원소를 갖는 1개의 리스트
print('*A =', *A)
# A = [1, 2, 3] [4, 5, 6]
# unpacking!의 결과

print('B =',B)
print('*B =', *B)
# B = [1, 2] [3, 4] [5, 6] # 3개의 원소만 뽑아 줬고, 튜플처럼 생각해주면 된다
# 언패킹된 아이를 zip안에 넣으면 zip 이 argument 3개를 갖는 것과 같다













