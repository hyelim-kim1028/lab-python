'''
1. 1부터 n까지의 숫자들의 합을 리턴하는 함수를 만들어라
    - n 만 알면 계산할 수 있다. 파라미터를 하나만 선언해라, 그 하나만 받으면 1~n까지로 ...
    -  다양한 방법을 생각해보자 (for, while, for 어쩌구 [] 하는거, function 도 사용해보고싶다)
2. 1부터 n까지 숫자들의 제곱의 합을 리턴하는 함수
    - 1**2 + 2**2 + .... + n**2
3. 숫자들의 리스트를 전달 받아서 최댓값/최솟값을 찾아서 리턴하는 함수
    - 파라미터가 1개, 리스트에서 최댓값을 찾아서 리턴해주면 된다
4. 숫자들의 리스트를 전달받아서 최댓값/최솟값의 인덱스를 리턴하는 함수
5. 숫자들의 리스트를 전달받아서 중앙값(median)을 리턴하는 함수 [6,3,2,4,1,5]
    - sorting 했을 때 가운데에 있는 값 (크기 순서대로 세워서 가운데에 있는 값 찾기)
'''

# n(n+1)/2  - 1 부터 100까지 더하는 공식

# def n_sum(x: float) -> float:
#     '''
#     summation of all elements from 1 to x
#     :param x:
#     :return:
#     '''
#     result = 0
#     for i in x: #range(x) 에서도 작동을 할까?
#         result += i
#     return result
#
# print(n_sum([1,2,3]))



# teacher's solution
def sum_to_n(n: int) -> float:
    return n * (n + 1) / 2

result = sum_to_n(9)
print(result)

def sum_to_n2(n: int) -> int:
    _sum = 0
    for x in range(1, n + 1):
        _sum += x
    return _sum

result = sum_to_n2(9)
print(result)

def sum_to_n3(n: int) -> int:
    numbers = [x for x in range(1, n + 1)]
    print(numbers)
    return sum(numbers)

result = sum_to_n3(9)
print(result)

# 셋 중 가장 안좋은 방법은 세번째 방법이다 (리스트 만들기 반복문 + 연산 반복문).
# 두번쨰도 n의 크기만큼 연산을 해줘야하기 때문에 두번째로 성능이 안 좋음


# 1부터 n까지 숫자들의 제곱의 합을 리턴하는 함수

# def my_squared(x: float) -> float:
#     '''
#     summation of squared elements from 1 to x
#     :param x:
#     :return:
#     '''
#     result = 0
#     for i in x: #range(x) 에서도 작동을 할까?
#         result += i**2
#     return result
#
# print(my_squared([1,2]))

# teacher's solution
# Formula for the summation of squared numbers = n(n+1)(2n+1)



# 3. 숫자들의 리스트를 전달 받아서 최댓값을 찾아서 리턴하는 함수
# def my_max(x: list): #how do you give a list as a parameter?
#     '''
#     Finding max value from the list of x
#     :param x:
#     :return:
#     '''
#     x_max = x[0]
#     for i in range(len(x)):
#         if x[i] > x_max:
#             x_max = x[i]
#     return x_max
#
# print(my_max([6,3,2,4,1,5]))

# 4. 숫자들의 리스트를 전달받아서 최댓값/최솟값의 인덱스를 리턴하는 함수
# def i_max(x: list):
#     '''
#     Finding index of a max value from the list of x
#     :param x:
#     :return:
#     '''
#     x_max = x[0]
#     for i in range(len(x)):
#         if x[i] > x_max:
#             x_max = x[i]
#     return x.index(x_max) # index 라는 함수를 사용해서 풀었다
# print(i_max([0,15,97,8]))


# values = list.sort 하면 null이 되어버림 (주의주의)
# sorted 는 저장해야하지만 sort는 하면 안된다

# 이 경우는 늘 순서를 유지해주어야한다. 최댓값을 찾고, 그리고 인덱스를 찾아야한다






# 5. 숫자들의 리스트를 전달받아서 중앙값(median)을 리턴하는 함수 [6,3,2,4,1,5]
def my_median(x: list):
    '''
    Get the median of a list of x
    :param x:
    :return:
    '''
    x_sorted = sorted(x)

    i_med = (x.index(len(x_sorted)) - 1)/2
    return i_med

# print(my_median([17,14,13,15,16]))

