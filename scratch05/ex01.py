"""
통계
많은 데이터를 다루는 학문. 데이터가 많을 때 그 데이터를 어떻게 볼 것이냐
중심이 어디있는가, 얼마만큼 퍼져있는가 (산포도)

i.e. 수능 점수
중심 경향성: 평균, 중앙값, 분위수, 최빈값
산포도: 분산(variance), 표준편차(standard deviation), 범위(range) # 범위는 평균과 상관 없고 나머지는 있어유
상관관계 (correlation): 공분산, 상관 계수

평균(average)
- 학생들의 점수가 어디를 중심으로 퍼져있는가
- 숫자 that represents 50만 of students
- total/n
- 평균의 약점: 이상치(outlier)에 약하다 (특정한 한두개의 값이 평균을 확 높이거나 낮출 수 있다)

- 중앙값 (median)
- 정렬을 시키고, 중앙 (위치적, 물리적) 에 있는 값을 갖는 것
- 이상치에 큰 영향을 받지 않는다
- 평균하고 맞지 않는 것도 있다

- 분위수 (Quantile) / 백분위수(percentile)
- quantile: divide the range into four
- percentile: divide the range into hundred

- 최빈값 (mode)
- most frequent number that represents a data set

- 산포도
- 평균/중앙값을 중심으로 얼마나 퍼져있는다
- how dispersed is the data

- 분산 (variance)
- get an average of a list of x
- i.e. x = [x1,x2,x3,...,xn]

- 표준편차 (standard deviation)
- 범위 (range)



"""
# from scratch04.ex01 import dot


# Average
def mean(x):
    """

    :param x: a list of n number of components (1-dim list)
    :return: average
    """
    sum = 0
    for x_i in range(len(x)):
        sum += x[x_i]
    return sum / len(x)


    # teacher's thought
    # return sum(x)/len(x)

    # thought 3 (prob: x_i)
    # sum = 0
    # if x_i in range(len(x)):
    #     sum += x_i
    # return sum/len(x)

    # thought 2
    # x = []
    # for x_i in range(len(x)):
    #     x.append(x_i)
    #     sum = 0
    #     for x_i in range(len(x)):
    #         sum += x_i
    # return sum/len(x)

    # thought 1 -> extended idea x.append[] list of numbers -> I tried this method and it did not work well, better to improve the thought1
    # sum = 0
    # for x_i in range(len(x)):
    #     sum += x_i
    # return sum/len(x)

# Median
def median(x):
    """
    list x 를 정렬 (sort 함수 사용) 했을 때 중앙에 있는 값을 찾아서 리턴
    n 이 홀수이면, 중앙값을 찾아서 리턴, n이 짝수이면, 중앙값에 있는 두 개 값의 평균을 리턴
    :param x: 원소 n개인 (1차원) 리스트
    :return: 중앙값
    """
    # teacher's solution
    n = len(x) # 리스트의 아이템 개수
    sorted_x = sorted(x) #데이터 크기 순으로 정렬(오름차순)
    mid_point = n//2 #리스트의 가운데 위치 (인덱스) # 몫을 구해주기 위한
    if n % 2: # if n % 2 ==1 이면이라고 주려고 했는데 파이썬은 1은 참으로 취급하니까 써주지 않아도 된다 #홀수일때
        median_value = sorted_x[mid_point]
    else: # 짝수인 경우 index + (index - 1) 0부터 시작해서 그려,,,
        median_value = (sorted_x[mid_point-1] + sorted_x[mid_point])/2
    return median_value

    # my thought
    # x = list.sort(x) # x.sort() 이건가? 헷갈린다 -> 이건 sorted 된 리스트를 호출할 때
    # 이게 아닌가 ㅎㅎ;;;
    # for x_i in x:
    #     if len(x) % 2 == 0: # 그런데 for 문 안주고 어떻게 인덱스를 계산?
    #                         # 인덱스 이것도 잘 못 줬다 (파이썬의 인덱스는 0부터 시작)
    #         return x[(x_i* 2 +1)/2]
    #     else:
    #         return x[x_i/2]

# Quantile
def quantile(x, p):
    """
    리스트 x의 p 분위에 속하는 값을 찾아서 리턴
    :param x: 원소 n개인 (1차원) 리스트
    :param p: percent (0~1.0 사이의 값)
    :return:
    """
    # sort 해서 위치를 찾아내면 된다
    n = len(x) #리스트의 아이템 개수
    p_index = int(n * p) #해당 퍼센트의 인덱스 - 소수점 버린다
    # 숫자에서 소숫점 버리기 할 때 int 를 사용하기도 한다
    sorted_x = sorted(x)
    return sorted(x)[p_index]

    # my_thought
    # min_n = x[0]
    # max_n = x[0]
    # for i in range(len(x)):
    #     min_n <= x[i]
    #     max_n >= x[i]
    # p = (max_n - min_n)/4
    # for i in range(len(x)):
    #     q = i in (p)
    # return q

from collections import Counter

# def mode(x):
#     """
#     리스트에서 가장 자주 나타나는 값(최빈값) 을 리턴
#     최빈값이 여러개인경우, 최빈값들의 리스트를 리턴
#
#     :param x: 원소가 n개인 1차원 리스트
#     :return: 최빈값들의 리스트를 리턴
#     """
#     # 최빈값이 1개만 올 수도 있고, 여러개가 올 수 도 있다.
#     # 최빈값을 모두 찾아야한다 (1개 이상이라도)
#     for i in x.elements():
#         print(i, end = " ")
#     print()


def mode(x):
    counts = Counter(x) #Counter() 는 counter 라는 클래스를 만들어주는 생성자 # Counter() 객체 생성
    # print(counts)   # dictionary (number:frequency)
    # print(counts.keys(), counts.values()) # keys = data set, values = frequency of the keys
    # print(counts.items()) # dict_items([(2, 2), (3, 2), (4, 3), (6, 3), (100, 1)]) - key 와 value 의 튜플로된 리스트를 반환
    # 빈도수의 최댓값 찾기!
    max_count = max(counts.values()) # 빈도수의 최댓값
    # keys of the values
    freq = [] # 최빈값들을 저장할 리스트
    return [val for val, cnt in counts.items()
            if cnt == max_count] # 얘만 쓰던가 (144), 아니면 이 밑에(145~149)를 쓰던가 둘 중 한개
    # for val, cnt in counts.items():
    #     if cnt == max_count: # if the requency of a value is the same as its maximum,
    #         freq.append(val) # save it in the list
    #         # cnt 가 maximum cnt 와 같을 때 values will be appended to the freq list
    # return freq

    # https://www.daleseo.com/python-collections-counter/
    # max_count = -1
    # for x_i in counts:
    #     if counts[x_i] > max_count:
    #         max_count = counts[x_i]
    #         max_i = x_i
    #     return max_i, max_count


def data_range(x):
    """

    :param x:원소가 n개인 (1차원) 리스트
    :return: 리시트의 최댓값 - 리스트의 최솟값
    """
    sorted_x = sorted(x)
    min_n = sorted_x[0]
    max_n = sorted_x[len(x)-1]
    return max_n - min_n
    # the same as:
    # sorted_x[len(x) - 1] - sorted_x[0]
    # or
    # return max(x) - min(x)

def de_mean(x):
    """
    편차들의 리스트
    :param x:
    :return: 편차(deviation)들의 리스트
    """
    mu = mean(x) #평균
    return [x_i - mu for x_i in x]

def variance(x):
    """
    sum += (x[i] - mean) ** 2
    return sum/(len(x)-1)
    :param x: 원소가 n개인 1차원 리스트
    :return: 분산을 계산해서 리턴
    """
    sum = 0
    for x_i in de_mean(x):
        sum += (x_i) ** 2 #de_mean 은 어떻게 사용할까 -> list라서 사용이 힘들어,,,
        # how about I give: sum += (x[i] - sum/len(x)) **2 and do not say anything about mean? is it still valid?
        # we defined the xi-mu above
    return sum / (len(x) - 1)

# teacher's solution1
#     n = len(x) # number of elements
#     x_bar = mean(x) # x_bar = avg
#     return sum([x_i - x_bar] ** 2 for x_i in x) / (n-1)

# teacher's solution 2'
#     n = len(x)
#     deviations = de_mean(x) #편차들의 리스트 -> 여기서 하나만 꺼내면 (x_i - mu) 이다
#     return sum([x ** 2 for d in deviations])/(n-1)

# 이젠 list comprehension 으로!!! 만들어주기

# teacher's solution 3
# using the dot function we made before
# def variance2(x):
#     print('dot사용')
#     n = len(x)
#     deviations = de_mean(x)
#     return dot(deviations, deviations) /(n-1)

from math import sqrt

def standard_deviation(x):
    """

    :param x: 원소가 n개인 1차원 리스트
    :return: 표준편차
    """
    return sqrt(variance(x))

# 상관관계: 두개의 변수에 대한 관계

def covariance(x, y):
    """
    covariance = sum((x_i - x_bar)(y_i - y_bar)) / (n-1)
    :param x: 원소가 n개인 1차원 리스트
    :param y: 원소가 n개인 1차원 리스트
    :return: 공분산
    """
# x, y have the same number of values

    #     n = len(x) # number of elements
    #     x_bar = mean(x) # x_bar = avg
    #     return sum([x_i - x_bar] ** 2 for x_i in x) / (n-1)

    # n = len(x)
    # x_bar = mean(x)
    # y_bar = mean(y)
    # return sum([((x_i - x_bar) * (y_i - y_bar)) for x_i, y_i in zip(x,y)])/(n-1)

# teacher's solution1
    x_bar = mean(x) # average of the list x
    y_bar = mean(y) # average of the list y
    x_deviations = [x_i - x_bar for x_i in x] #편차들의 리스트
    y_deviations = [y_i - y_bar for y_i in y]
    sum_of_deviations = 0
    for xd, yd in zip(x_deviations, y_deviations):
        sum_of_deviations += xd * yd # where there is no sum_of_deviations = 0, sum_of_deviations += xd * yd occurs an error
                                    # because sum_of_deviations has not yet been defined
    return sum_of_deviations / (len(x) - 1)
    # can also do this:
    # x_bar = mean(x)  # average of the list x
    # y_bar = mean(y)  # average of the list y
    # # x_deviations = [x_i - x_bar for x_i in x]
    # # y_deviations = [y_i - y_bar for y_i in y]
    # sum_of_deviations = 0
    # for xd, yd in zip(x, y):
    #     sum_of_deviations += (xd - x_bar)(yd - y_bar)
    # if we skip * in (xd - x_bar)* (yd - y_bar), then it occurs an error, se dice " 'float' object is not callable"
    # not callable = sth is not a function (call-able : to call/invoke a function, we cannot call a function) wow solo ahora me daba cuenta del origen de la palabra!!
    # return sum_of_deviations / (len(x) - 1)
    # si el code esta escrito asi: (xd - x_bar)(yd - y_bar), la programa piensa el primera formula es una funcion => por eso se occura el error de funcion

# teacher's solution2 - not using for-statement
# must invoke the function from the other python file before running
#     x_bar = mean(x)
#     y_bar = mean(y)
#     x_deviations = [x_i - x_bar for x_i in x]
#     y_deviations = [y_i - y_bar for y_i in y]
#     sum_of_deviations = dot(x_deviations,y_deviations)
#     return sum_of_deviations/(len(x)-1)


def correlaton(x,y):
    """
    상관계수 (correlation)
    Corr = Cov(x,y) / (SD(x) * SD(y))

    :param x: 원소 n개인 (1차원) 리스트
    :param y: 원소 n개인 (1차원) 리스트
    :return: 상관 계수
    """
    sd_x = standard_deviation(x)
    sd_y = standard_deviation(y)
    if sd_x != 0 and sd_y != 0:
        corr = covariance(x,y)/((standard_deviation(x)) * (standard_deviation(y)))
    else:
        corr = 0
    return corr
# return covariance(x,y)/((standard_deviation(x)) * (standard_deviation(y)))
# 만 사용하는 것은 살짝 위험한 코드 (porque a veces, 표준편차 = 0, 0 이 되면 ,, 흠)
# 모든 데이터가 다 같으면 표준편차가 0 이고, 분모가 0 이면 에러 발생
# 둘중에 하나라도 0 이 있으면 에러를 리턴하거나 0을 리턴해주는 코드로 짜도 좋을 것 같다
# 그래서 if-else 코드로 바꿔주었다

# 상관관계: 기울기가 급할수록? more scant , 상관관계가 높다, 기울기가 완만할수록 상관관계가 낮다


if __name__ == '__main__':
    data = [2,2,3,3,4,4,4,6,6,6,100]
    data2 = [10,2,5,3,4,1,4,0,6,1,7]
    print('mean =', mean(data))
    print('median =', median(data))
    print('1st quantile =', quantile(data, 0.25)) #1사분위 값
    # these quantiles return the indices
    print('3rd quantile =', quantile(data,0.75)) #3사분위
    print('mode = ', mode(data))
    print('range =', data_range(data))
    print('variance =', variance(data))
    # print('variance2 =', variance2(data))
    print('sd =', standard_deviation(data))
    print('covar =', covariance(x = data, y = data2))
    print('correlation =', correlaton(x = data, y = data2))

    x = [-3,-2,-1,0,1,2,3]
    y = [3,2,1,0,1,2,3]
    # y = /x/
    print(correlaton(x,y))
    # 0에 수렴 (상관관계가 읎다,,,^^;;)
    # 한쪽만 보면 양수로 완벽한 상관관계, 다른 한쪽은 음으로 완벽 -> 으앙 그러니까 이도저도 아닌게지
    















