"""
선형대수(linear algebra)
"""
# 각 성분별로 더하기를 리턴해주는 함수

def add(v,w):
    """
    주어진 두개의 벡터에서 성분별로 더하기를 해서, 새로운 n 차원 벡터를 리턴해주세요
    :param v: n차원 vector (성분이 모두 n개인 벡터) 
    :param w: n차원 vector (차원이 같아야지만 더하기가 가능하다) 
    :return: 각 성분별로 더하기 결과를 갖는 벡터 
    """
    # thought 1
    # for i in v:
    #     for n in w:
    #         if count(i) = count(n): # how to put
    #             v[i] + w[n]
    #     return v + w

    #thought2
    # zip 사용하는 것 같기도 for l,f,m in zip(labels, friends, minutes):
    #     for i,n in zip(v,w):
    #         print (i + n) # 여기를 고쳐주면 될 듯
    # how to make them is a list format

    # teacher's solution
    if len(v) != len(w):
        raise ValueError('v and w must have the same length')
    return [v_i + w_i for v_i, w_i in zip(v,w)]
    # v = [v1,v2, ... , vi]
    # w = [w1,w2 ... wi]
    # add = [v1 + w1, v2 + w2 ... vi + wi]

    # teacher's solution 2
    # if not using list comprehension
    # result = []
    # for i in range(len(v)):
    #     result.append(v[i] + w[i])
    #  return result # indentation aligned with for-statement

def subtract(v,w):
        """
        주어진 두 개의 n차원 백터에서 성분별로 뺄셈을 수행
        :param v: n차원 벡터
        :param w: n 차원 벡터
        :return: n 차원 벡터
        """
        # my_method
        # for i,n in zip(v,w):
        #     print(i-n)

        #teacher's solution1
        if len(v) != len(w):
            raise ValueError('v and w must have the same length')
        return [v_i - w_i for v_i, w_i in zip(v, w)]

        # Teacher's solution2
                # result = []
                # for i in range(len(v)):
        # depends on the len(v)/ if len(v) < len(i); len(v) 까지만 계산하고 다 버려버림/ if len(v) > len(i) 면 incur an index error
                #     result.append(v[i] + w[i])
                # return result

def vector_sum(vectors):
    """
    모든 벡테들에서 각 성분별 더하기를 수행
    vector_sum([v,w,x,y])
    vector_sum([1,2],[3,4],[5,6]) = [ 1+3+5 = 9, 2 + 4 + 6 = 12] = [9,12]
    :param vectors: n 차원 벡터들의 리스트 (2 차원 리스트) -> 벡터 안에 벡테가 들어가,,,
    :return: n 차원 벡터
    """
    # teacher's thoughts
    num_of_elements = len(vectors[0])
    for vector in vectors[1:]: #slicing [1:] -> 1번부터 마지막 까지
        if num_of_elements != len(vector):
            raise ValueError('모든 백터는 길이가 같아야함.')

    # result = [0 for _ in range(num_of_elements)] #num_of_elements 만큼 0을 채워 넣겠다 [0,0,0...]
    # for i in range(num_of_elements):
    #     for vector in vectors:
    #         result[i] += vector[i]
    # return result

    # using function
    result = vectors[0] # first row
    for vector in vectors[1:]:
        result = add(result, vector)
    return result

    # my thoughts
    # for 구문에 [v_i - w_i for v_i, w_i in zip(v, w)] 을 넣어서 계속 합해주기 x[i] + x[i+1]
    # for i,n in zip(v, w):
    #      v += v[i]
    #      w += w[n]
    # return (v,w)
# algo en este sentido
# using add function we made above

# sum = 0
#     for v in vectors:
#             vectors[v] # change of vector value (of v index?)
#             for i in vectors: #change of index value
#                 sum += vectors[i]

    #  A - double loop
    # sum = 0
    # for v in vectors:
    #     for i in vectors: #change of index value
    #         sum += vectors[i]
    #     vectors[v]  # change of vector value (of v index?)

    # B - add function
    #     if len(v) != len(w):
    #         raise ValueError('v and w must have the same length')
    #     return [v_i + w_i for v_i, w_i in zip(v,w)]
    #     return [sum += vectors_i for vecotrs_i in zip(vectors)]
    # I feel sick


def scalar_multiply(c, vector):
    """
    c * [x1,x2,x3...] = [c*x2, c* x2 ...]

    :param c: 숫자(스칼라, scalar)
    :param vector: n차원 vector (n개의 아이템을 갖는 1차원 리스트)
    :return: n-dimension vector
    """
    # my thought - mas o menos
    # sc_multi = []
    # for i in vector:
    #     vector.append(c * vector[i]) #sc_multi.append(c * i)
    # return sc_multi

# teacher's solution
    result = []
    for item in vector: # vector from the parameter
        result.append(c*item)
    return result

# teacher's solution2
#     return [c * i for i in vector]


def dot(v,w):
    """
    [v1,v2,v3...] @ [w1,w2,w3...] = v1 * w1 + v2* w2 + v3 * w3 ...
    :param v: n-dimensional vector
    :param w: n-dimensional vector
    :return: scalar
    """
    # my thoughts # muy parecidos22222 (has hecho muy bien! estoy mucha contenta)
    # sum = 0
    # for i in zip(v,w):
    #     sum += v[i] * w[i]
    # return sum

    # teacher's solution1
    if len(v) != len(w):
        raise ValueError('El tamano/largo (length) de los vectores deben ser mismos!')
    sum = 0
    for v_i, w_i in zip(v,w):
        sum += v_i * w_i
    return sum

def vector_mean(vectors):
    """
    주어진 백터들의 리스트에서 각 항목별 평균으로 이루어진 백터
    :param vectors: list of n-dimensional vectors
    (길이가 n인 1차원 리스트를 아이템으로 갖는 2 차원 리스트)
    :return: n차원 백터(길이가 n인 1차원 리스트)
    """

# my thoughts
    # num_of_elements = len(vectors[0])
    # for vector in vectors[1:]:
    #     if num_of_elements != len(vector)
    #         raise ValueError('No puede ser!')
    #
    # result = vectors[0]
    # for vector in vectors[1:]:
    #     result = add(result, vector)
    # return result

    # for vector in vectors:
    #     vector_sum()/len(vector)
    # return result

#    vector_sum * scalar_multiply(vector ** -1)

# teacher's solution
    length = len(vectors)
    return scalar_multiply(1/length, vector_sum(vectors))

def sum_of_squares(vector):
    """
    vector = [x1,x2, ... xn]
    n 차원 벡터일 때, x1의 제곱 + x2의 제곱 + ... + xn의 제곱을 리턴
    square root ( x1의 제곱 + x2의 제곱 + ... + xn의 제곱)
    :param vector: n차원 벡터(길이가 n인 1차원 리스트)
    :return: 숫자
    """
    # sum = 0
    #     # for x_i in vector:
    #     #     sum += x_i**2 # tambien se puede escribir asi: x_i * x_i => v_i * w_i -> dot product
    #     # return sum

    # if x_i * x_i => v_i * w_i -> dot product, then:
    return dot(vector,vector)

import math

def magnitude(vector):
    """
    vector 의 크기를 리턴하는 함수 - math.sqrt(sum_of_squares)
    """
    return math.sqrt(sum_of_squares(vector))

# 만능키 alt + n

# 두 백터 사이의 거리

def squared_distance(v,w):
    """
    (v1 - w1) **2 + (v2 - w1) ** 2 + .... + (vn - wn)**2
    :param v: n차원 벡터(길이가 n인 1차원 리스트)
    :param w: n차원 벡터(길이가 n인 1차원 리스트)
    :return: 숫자
    """
    sum = 0
    for v_i,w_i in zip(v,w):
        sum += (v_i - w_i) **2
    return sum

    # return sum_of_squares(subtract(v,w))
    # what I did originally: sum_of_squares(v_i - w_i)

def distance(v,w):
    """
    두 벡터 v 와 w 사이의 거리를 리턴 - sqrt(squared_distance)
    :param v:
    :param w:
    :return:
    """
    return math.sqrt(squared_distance(v,w))






if __name__ == '__main__':
    # how I tested
    a = add([1,2,3],[4,5,6])
    print('add =',a)
    b = subtract([1,2,3],[1,2,3])
    print('subtract =',b)

    # how teacher tested
    v = [1,2]
    w = [3,4]
    result = add(v,w)
    print('add2 =',result)
    result = subtract(v,w)
    print('subtract2 =', result)



# 정상적인 경우만 테스트하지말고 에러가 날 것 같은 경우도 해보자

# w,v 의 순서 반대로 준 경우 가능
    result = add(w,v)
    print('add test = ',result)

# 하지만 different len of v & w -> also possible
    v = [1, 2, 3]
    w = [3, 4]
    result = add(v, w)
    print('add test = ',result)



# zip 이라는 함수가 (v,w) 중에서 작은 갯수 만큼만 뽑아낸다 => 많은건 그냥 버려버림
    #    if len(v) != len(w):
    #             raise ValueError('v and w must have the same length')
    # 이 문구를 지워주면 zip 이라는 함수가 자동으로 더 짦은 걸로 해주는 걸 볼 수 있다
# 그래서 if ... raise error 구문을 넣어주었다
    v = [1, 2, 3]
    w = [3, 4]
    result = subtract(v, w)
    print('subtract test =', result)

    vectors = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    result = vector_sum(vectors)
    print('vector_sum =', result)

    print("test scalar_multiply")
    v = [1,3,5]
    sm = scalar_multiply(2,v)
    print('scalar multiply =', sm)

    print("test Dot Product")
    v = [2,3]
    unit_x = [1,0] #x-axis 단위 백터 (어떤 방향으로 크기가 1인)
    unit_y = [0,1] #y-axis 단위 백터
    dot1 = dot(v, unit_x)
    print('dot1 = ', dot1)
    dot2 = dot(v, unit_y)
    print('dot2 =', dot2)

    print("vector mean")
    vectors = [
        [1,2]
        [3,4]
        [5,6]
    ]
    vm = vector_mean(vectors)
    print('vector mean =', vm)

    v = [3,4]
    ss = sum_of_squares(v)
    print('sum of squares =', ss)

    norm = magnitude(v) #In linear algebra, norm referes to the result of magnitude
    print('magnitude =', norm)

    v = [1,2]
    w = [3,4]
    sqd = squared_distance(v,w)
    print('squared distance =', sqd)
    dist = distance(v,w)
    print('distance =', dist)
















