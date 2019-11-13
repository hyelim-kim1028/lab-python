"""
파이썬에서 함수는 1급 객체 (first-class object) 이라고 불리운다
-> first-class object means 함수를 변수에 저장할 수 있다
-> 함수가 모든 object의 특징을 갖는다
-> 매개변수(parameter) : 함수 선언할 때 함수 header 에 있는 변수
-> 매게 변수에 함수를 전달할 수 있음
-> 함수가 다른 함수를 리턴할 수도 있음
-> 함수 내부에서 다른 함수를 정의할 수도 있음
"""

def twice(x):
    return 2 * x

result = twice(100) #함수 호출 -> 함수의 리턴값을 변수에 저장
print(result) #함수의 리턴값을 출력

double = twice
# line 14 and 17 are different. We call invocation when we do function(value) like in line 14, however,
# in line 17, we saved the function in a variable (함수 자체를 변수에 저장)
print(double) #function의 이름 + 주소를 준다 (함수를 저장)

result = double(11)
print(result)
# Now, double and twice became exactly the same functions;
# when we invoke the function double, we are actually invoking the function twice

# 함수를 매게변수제 저장
def plus(x,y):    # To be used with the operator function below
    return x + y

def minus(x,y):
    return x - y

def calculate(x, y, operator):
    return operator(x,y) # 이건 뭘까욤
            # 모두 다 파라미터인데 왜 이렇게 온거지??
            # 어떤 이름 뒤에 괄호를 써주고, fn(...) 이면 함수 호출
            # 함수를 주고 (값을 줘라) 라는 의미?

# Guardabamos la funcion en el parameter de operator y creamos una funcion que se vuelva operator(x,y)

result = calculate(1,2,plus) # la funcion se llama plus esta guardada en el parameter 'operator'
print(result)
# Returned value: 3 -> x = 1, y = 2, operator = plus
# operator = plus goes in the same logic as how we put twice = double
# operator(1,2) is the same as plus(1,2)


# voy a estudiar la relacion de sud america y corea + los articulos (los issues sociales)

result = calculate(1,2,minus)
print(result)
# es possible por 함수 자체를 변수에 저장할 수 있다는 특징 때문에

def decorate(func):
    print('decorate 함수 내부: ', func.__name__)
    # decorate 함수 내부에서 wrapper_function 함수를 정의한다
    def wrapper_function(*args):
        print('다음 함수를 실행:', func.__name__)
        # 선 두개 입니당,,, ^0^
        return func(*args) #func 를 decorate 함수의 파라미터
    # decorate 함수에서 다른 함수(wrapper_function)를(을) 리턴
    return wrapper_function # returned a function (함수 이름 자체)

wrapper1 = decorate(print)
wrapper1 = ('a','b','c')

# 구별해야할것: 함수 호출 vs 함수를 변수에 저장 (sin parentesis)
# 함수를 호출할 때 준 값을 argument 라고 한다

# Como expresa las funciones (f(x)):
# f(x) = ax + b  # los dos son mismos
# f: x -> ax + b # 람다 (lamda) 표기법
# 람다표기법을 잘 활용하면 코드를 더 간단히 작성할 수 있다 (간단히에 대한 단어 찾아보기)







































