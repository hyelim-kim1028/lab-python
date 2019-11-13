"""
error, exception: 프로그램 실행 중에 발생할 수 있는 오류
- exception 은 예외 (프로그램 실행 중 비정상적인 발생 -> 오류)

프로그램 실행중에 오류가 발생하면 해결 방법:
1) 오류가 발생한 코드 위치를 찾아서 오류가 발생하지 않도록 수정
2) 오류가 발생하더라도, 오류를 무시하고 프로그램이 실행될 수 있도록 프로그램을 작성
    -> try 구문
"""

# Different types of errors
print(1)

# TYpical Error 1: nameerror: 변수나 함수등의 없는 이름을 사용하려고 할 때 ( ~ not defined)
#pritn(1)

n = int('1')
# n = int(input('정수 입력: '))
        # when we run this code: the number received will be deemed as 'character string' for Python
    # Por eso, debe poner int/float
    # int(): 문자열 -> 정수, float(): 문자열 -> 실수
    # 사용자가 키보드로 입력한 값들은 regardless of its type, they are all regarded as character strings

n = int('123')
print(n)

# PERO, n = int('123.') se occura un error: ValueError: invalid literal for int() with base 10: '123.'
# . 때문에 10 진수로 변환할 수 없다
# 코딩을 잘 하려면 에러 메시지 보는 연습을 잘 해야한다

numbers = [1,2,3]
#print(numbers[3])
# IndexError: list index out of range
# Index [0,(n-1)] -> numbers의 인덱스는 0,1,2 니까, 3은 out of range 가 맞다
# oracle 이나 R은 인덱스가 1 부터 시작하지만, 다른 언어들 C, java와 같은 아이들은 0부터 시작

#print('123' + 456)
# TypeError: can only concatenate str (not "int") to str
# '123' is a character, 456 is a number type; different types cannot be added

"""
n = 100 
x = input()
하면 x 의 값은 character 이 되고, 그냥 
n + x해버리면 그것도 type error 이 되어버린다 
"""

print(123 / 0)
# ZeroDivisionError: division by zero
# 수학에서 0으로 나눌 수 없다 -> mathematically wrong

# 이것말고도 여러가지 다른 에러들이 발생할 수 있다. 발생 했을 때 가서 고친다 혹은 에러가 발생하더라도 실행될 수 있도록 한다























