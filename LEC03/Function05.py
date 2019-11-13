# # 가변 길이 인수 (Variable-length argument)
# # 함수를 호출할 때 전달하는 argument의 갯수가 가변적으로 변할 수 있을 때 사용하는 방식
# # 파라미터 앞에 *을 붙임
# # print함수는 대표적으로 가변 길이 인수
# # print(‘a’) 이나 print(‘a’,’b’,’c’,’d’) 이라고해서 모두 파라미터를 따라가지 않는다
#
# print('a')
# print('a','b','c','d', sep = ':')

# 파라미터를 설정할 때 * 가 있다는 것은 개수와 상관이 없다 라는 의미

#가변 길이 인수 만들어보기

# def fn_vararg(varargs):
#     print(varargs)
#
# fn_vararg(1) #실행이 잘 된다
# fn_vararg(1,2) #TypeError: fn_vararg() takes 1 positional argument but 2 were given

# Pero cuando ponemos * en el parameter, no le importa cuantas variables que pongamos
# def fn_vararg(*varargs):
#     print(varargs)
#
# fn_vararg(1,2)

# def fn_vararg(*varargs):
#     print(varargs)
#     for arg in varargs:
#         # 여기에 사용할 때는 * 없이 사용해야 튜플로 취급되지 않아 언팩 가능
#         print(arg)

# fn_vararg(1,2,3)
# 그리고 리스트나 튜플에서 원소를 하나씩 꺼내고 싶으면 for .. in .. 구문을 사용하면 된다
# 묶여있던 것들이 하나씩 unpacked 되는 것

# 하나 만들어봅시당

# def summation(*args):
#     """
#     임의의 갯수의 숫자들을 전달받아서 그 숫자들의 총합을 리턴하는 함수 작성
#     :param args: integer
#     :return:
#     """
#     result = 0
#     for number in args:
#         result += number
#     return result

# print(summation())
# # 에러는 생기지 않고, 초기화된 값 0 이 리턴이 된다
# print(summation(1,2,3,4,5,6))

# def fn_vararg2(a, *b):
#     print(f'a = {a}')
#     print(f'b = {b}')

# fn_vararg2()
# TypeError: fn_vararg2() missing 1 required positional argument: 'a'
# a 라는 argument 가 있는데 기본값이 없으니까 반드시 값을 주어야한다
# fn_vararg2(1)
# b는 가변길이라서 값을 줘도되고, 안줘도 되고, 많이 줘도 된다 그래서 에러없이 실행

# fn_vararg2() # a값을 전달하지 않으면 에러 발생
# fn_vararg2(1) #b는 가변길이 파라미터이므로 인수를 전달하지 않아도 됨

# def fn_vargars3(*a,b):
#     print(f'a = {a}')
#     print(f'b = {b}')

# fn_vargars3()
# TypeError: fn_vargars3() missing 1 required keyword-only argument: 'b'
# *a 는 가변길이 파라미터이므로 줘도 되고 안줘도 되는 값이지만
# b 는 keyword-only argument 가 missing 이라고 했다
# 왜 이럴까? *a 는 가변길이니까 몇개가 올지 컴퓨터도 예상하지 못 하고, 그러니까 반드시 b를 명시하고 값을 줘야한다

# fn_vargars3(1,2)
# 이 아이도 에러가 난다: TypeError: fn_vargars3() missing 1 required keyword-only argument: 'b'

# fn_vargars3(1, b = 2)
# 가변길이 파라미터 뒤에 선언된 파라미터에 값을 전달할 때는 keyword 방식으로만 값(argument) 를 전달할 수 있음
import operator


def calculator(*values, operator):
    """
    operator가 + 인 경우에는 values들에 합계를 return 하고
    operator가 * 인 경우에는 values들의 곱을 return 하는 함수
    operator가 위 두 경우가 아니면 None 을 리턴

    :param values: int
    :param operator: int
    :return: return the total summation or product of values
    """
    result = None # 다른 operator 가 오면 None 을 출력
    if operator == '+':
        result = 0
        for x in values:
            result += x
       # return result
    elif operator == '*':
        result = 1
        for x in values:
         result *= x
        #return result
# 왜 에러가 나지: indentation error: function 은 """ 에 맞춰서 식을 써주세요

    return result


result = calculator(1,2,3,4,5, operator = '+')
print(result)
result = calculator(1,2,3,4,5, operator = '*')
print(result)
result = calculator(1,2,3,4,5, operator = '-')
print(result)


# idea1
# s = 0
# values = values[0]
# while operator == '+':
#     s += values
#     p = 1
#     while operator == '*':
#         p = p * values
# return s, p

#idea2
# for i in values:
#     if operator == '+':
#         result += i
#     if operator == '*': #if -> elif
#         result = result * i
# return result

# 자주 써보면 익숙해진다. 자주하면 기억할 수 있다. dont get frustrated
# just follow what we did in class
# And we do it repeatedly, there come a time of aha-moment






