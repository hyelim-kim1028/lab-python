def test(x, y):
    print(f'x = {x}, y = {y}')
    return x + y, x - y

# 함수 호출
#  test()
# Error: test() missing 2 required positional arguments: 'x' and 'y'
# 실행 중에 type error 발생
# 파이썬은 함수의 파라미터 타입은 검사하지 않지만, 파라미터 갯수는 검사합니다
# 파라미터를 줘야하는만큼 주지 않으면 에러가 발생
# positional argument: 함수를 호출할 때 전달하는 값(arguments)들이 함수 정의에 선언된 파라미터 순서대로 전달되는 방식

# plus, minus = test(1,2)
# plus,minus = test(1)

# positional argument : 함수를 호출할 때 전달하는 값(argument)들이 함수 정의에 선언된 파라미터 순서대로 전달되는 방식
# keyword argument: 함수를 호출할 때, argument를 파라미터 = 값 형식으로 전달하는 방식

plus, minus = test(x=10, y=20)
print(minus)
plus, minus = test(y=10, x=20)
print(minus)

# keyword argument를 사용하면 함수가 정의된 파라미터 순서와 상관 없이 argument를 전달할 수 있다.



# default argument: 함수를 정의할 때 파라미터의 기본값을 설정하는 것
# 문자열에서 사용할 수 있는 산칙연산 +,*
# + : 두 문자열을 이어 붙여준다, * : * number 만큼 repeat
def show_msg(msg: str, times: int = 1) -> None:
    print(msg * times)

show_msg('졸리세요?', 5)
show_msg('네... 많이 졸려요~~')
# 에러가 나지 않는다, 문자열 1번만 하고 끝남

# hay values en cada parameter que se puede usar la funcion vacia
def show_msg(msg: str = 'hello', times: int = 1) -> None:
    print(msg * times)
show_msg()

# default argument 주의 사항:
def test2( x = 1, y):
    return x + y
# 에러가 난다: default 파라미터는 뒤쪽에 놔주어야해요
# dafault argument 를 갖는 파라미터는 반드시 default argument를 갖지 않는 파라미터들이 선언된 뒤에 선언해야 함

# test2(1,2)
# logically, if we put test2(1), somebody might think that 1 would automatically be the value of y which does not have a default value
# However, for the logical process, we give default arguments after non-default ones





















