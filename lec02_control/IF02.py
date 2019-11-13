"""
Python 에서 참과 거짓을 판별할 때
1) 숫자 타입인 경우 0 은 F 취급을 한다, 0 이외의 숫자는 True 취급을 한다
2) 숫자 이외의 타입인 경우, 비어있는 값('',"",[], {}, (), ... ) 은 FALSE 취급한다. 나머지는 트루취급한다


"""
# 1) 숫자 타입인 경우 0 은 F 취급을 한다, 0 이외의 숫자는 True 취급을 한다
n = 2
if n % 2:
    print('Odd number')
else:
    print('even number')
# 언어에 따라 조금씩 룰이 다르다 (1번의 rule을 인정하기도 하고 안하기도 하다)
# 2로 나누어서 나머지가 있으면 0 이외의 다른 값이 오기 때문에 (1) TRUE, 하지만 나누어서 나머지가 없으면 0 으로써 False
# 1 은 True 0은 False

# 2) 숫자 이외의 타입인 경우, 비어있는 값('',"",[], {}, (), ... ) 은 FALSE 취급한다. 나머지는 트루취급한다
my_list = [] #비어 있는 리스트 (empty list)
if my_list:
    print(my_list)
else:
    my_list.append('Python')
    print(my_list)
# when the list is Empty, we consider it as False and therefore the conditional statement immediately return the value from else-statement
# But when the comment is done for the second time, it no longer returns FALSE because the code had alread added 'python'
# using append function

# in 연산자
# ~ 안에 있으면
# 변수 in 리스트/ 튜플/ dictionary 등등..

languages = ['PL/SQL','R']
if 'Python' in languages:
    pass #아무일도 하지 않고 지나감
else:
    languages.append('Python')
print(languages)
# print(languages) is not a part of else-clause, it's outside of it

# not 구문
lang = ['python','pl/sql','r']
if 'Python' not in lang:
    lang.append('Python')
print(lang)

# 위 두 코드는 같은 코드이다
# not을 사용해서 없으면~ 을 표현해줌
# 파이썬은 대소문자를 구분한다

























