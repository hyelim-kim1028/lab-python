"""
# 파이썬 2.x & 3.x 공통으로 함수를 선언하는 방법
함수 정의:
    def 함수이름(파라미터 선언):
        함수 기능 (body)

# 3.x로 들어와서 파라미터에 힌트(i.e. data type)를 주는게 가능해졌다
def 함수이름(파라미터: 타입, 파라미터2: 타입, ...) -> 리턴타입 :
    함수 기능(body)

"""

# 뺄셈 함수
def subtract(x: int,y: int) -> int:
    return x - y

result = subtract(1,2)
print(result)

# 파이썬은 함수를 호출할 때 함수의 파라미터 타입과 리턴 타입을 검사하지 않는다,
# 힌트를 아무리 준다고 해서 반드시 int만 넣어야한다는 아니다.
# 해당 데이터 타입이 아니더라도 제대로 작동한다 (힌트를 주는 목적일 뿐)

result = subtract(1.1,0.9)
print(result)


def my_sum(numbers: list) -> float:
    """
    숫자들(int, float)이 저장된 list를 전달 받아서,
    모든 원소들의 합을 리턴하는 함수
    :param numbers: list of numbers (숫자들이 저장된 리스트)
    :return: sum of elements in the list (리스트의 모든 원소들의 합)
    """
    # return
    result = 0
    for element in numbers:
        result =+ element
    return result #not print() but return result

result = my_sum([1,2,3,4,5,6])
print(result)
print(my_sum([1,10,100]))

# 평균을 계산하는 함수
#뭔가 이상하다
def my_mean(numbers: list) -> float:
    """
    숫자들을 저장하는 리스트를 전달받아서 ,
    모든 원소들의 평균을 계산해서 리턴하겠다
    :param numbers: list of numbers (숫자들을 저장한 리스트)
    :return: 리스트의 모든 원소들의 평균
    """
    return my_sum(numbers)/len(numbers)

result = my_mean([1,2,3,4,5])
print(result)

print(my_mean([1,10,100]))


















