"""
람다 표현식(lambda expression)
함수의 이름을 명시하지 않고 (함수의 이름 없이) 함수의 매개변수 선언과 리턴 값으로만 표현하는 방법
Lamda[p1,p2, ... ]: 식 (expression)
    # parameters
"""
# This is how to declare a function using lambda expression
multiplication = lambda x, y: x * y
result = multiplication(11,11)
print(result)

# lambda 표현식을 다르게는 이름이 없는 함수라고도한다.
# 이름이 없는 함수는 부를 수 없기 때문에 변수에 저장 한다
# 보통 함수의 매게변수를 주는 용도로 람다를 많이 사용한다

division = lambda x, y: x/y
result = division(1,2)
print(result)

# 람다 표현식은 주로 함수의 매게변수로 함수를 전달할 때 많이 사용함
# 다른 함수의 파라미터에 함수를 전달할 때 함수를 따로 만들지 않고, 바로 람다를 쓰는 그런 방식을 많이 쓴다

def calc(x,y,op):
    return op(x,y)

result = calc(1,2, lambda x,y: x+y)
                # 이렇게 하면 다른 함수를 굳이 주지 않아도 더하는 함수가 만들어 진다
print(result)

result = calc(1,2, lambda x,y: x/y)
print(result)

# lambda 표현식을 사용한 함수 예
def my_filter(values, func):
    """
    리스트의 원소들 중에서 필터링 조건을 만족하는 원소들만으로 이루어진
    새로운 리스트를 생성해서 리턴하는 함수
    필터링 조건: function 안에 넣어보고 T 면 리스트에 추가, F 면 리스트에 추가하지 않겠다
    :param values: list (any kind of)
    :param func: function that returns either True or False
    :return: 필터링된 새로운 리스트
    """
    result = [] # create an empty list
    for item in values: # 파라미터에 전달된 리스트에서 리스트의 모든 원소들에 대해서 반복
        if func(item) : # 필터링 조건 함수 func 의 리턴값을 검사
            result.append(item) #조건이 참인 경우에만 리스트에 추가
    return result

numbers = [1,-2,3,-4,5,6,7,8]
# combination of positive/negative numbers
positive = my_filter(numbers, lambda x: x > 0) # positive = func
# 1 parameter, returns boolean type data
print(positive)
# 양수들만 찾아서 출력

even = my_filter(numbers, lambda x: x % 2 == 0)
print(even)

# 람다 표현식은 여러 모듈에서 계속해서 쓰는 함수가 아니라, 간단한 함수 이면서 한번만 쓰고 끝낼 그런 함수
# 장점: 변수에 함수를 저장할 수 있게 해주는 것
# 함수가 들어갈 자리에 이름이 없는 함수 표현식 람다 표현식을 사용한 것이다!

languages = ['python','r','pl/sql','java','c/c++']
more_than_5 = my_filter(languages, lambda x: len(x) > 5)
print(more_than_5)

# my_filter 함수 list comprehension 으로 1줄로 써보기

def my_filter2(values, func):
    return [x for x in values if func(x)]
# values 에서 하나씩 꺼내서 리스트를 만들겠다
# func(x) 에서 참을 만족하는 값들만 리스트로 만들겠다

print(my_filter2(numbers, lambda x: x>0))
                        #this is the func(x) in this formula

def my_mapper(values, func):
    """
    리스트의 아이템들을 함수의 파라미터에 전달해서,
    리스트의 아이템을 키, 함수의 리턴값을 벨류로 하는 딕셔너리를 리턴한다
    Give the items in a list to the parameters of a function,
    return a dictionary with the items in the list as key, and Create a dictionary
    :param values: list
    :param func: function with one parameter
    :return: dict
    """
    result = {} #create an empty dictionary
    for item in values: #all elements of list values iterate (리스트 values 의 모든 원소들에 대해서 반복)
        # dict의 키는 item, dict의 값(value)는 함수 func의 리턴 값
        result[item] = func(item)
    return result

result = my_mapper(languages, lambda x: len(x))
# len(x) = 아이템의 length 를 리턴하겠다
print(result)
# 중괄호안에 key:value 의 pairs 로 이루어진 dict 이 완성을 return 해주었다

def my_mapper2(values,func):
    return {x:func(x) for x in values} # list 인 values 에서 하나씩 꺼내면서 그게 key 값이 되고,
                                       # returned value from func will be the value(v) => func(k)
                                       # whichever letter would come, it won't affect the function but be coherent
print(my_mapper2(languages, lambda x: len(x)))






















