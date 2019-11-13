# if-clause
"""
Python if-statement

if 조건식:
    조건식이 참일 때 실행할 문장
# Indentation is a must and one of the most important factors when using an if-statement

if 조건식:
    참일 때 실행 할 문장
else
    거짓일 때 실행할 문장

if 조건식1:
    조건식1이 참일 때 실행할 문장
elif 조건식2:
    조건식2이 참일 때 실행할 문장
...
else:
    모든 조건식들이 거짓일 때 실행할 문장
"""

# EXAMPLE
# 숫자를 입력받아서 양수일 경우에만 출력하는 문장
num = int(input('>>> 정수를 입력하세요'))
if num > 0:
    print(f'num = {num}')
else:
    print('0 or Negative number')

#if-elif-else
    score = 85
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    else:
        print('F')
    print('End the Program')

# INDENTATION is VERY IMPORTANT in Python
#if, elif, else 안에서도 다른 if 구문을 사용할 수 있음
if num % 2 == 0: #짝수이면
    if num % 4 == 0:
        print('Multiplier of 4')
    else:
        print('even number not a multiplier of 4')
else:
    #홀수이면
    print('odd number')
print('End the Program ')
# if 문안에 참일 때 할일이 없어서 에러가 나는 것
# 아무일도 안하겠다 라고 할 때 쓰는 키워드: pass



























