"""
try - except 구문 활용
"""

# n = int(input('정수를 입력하세요>>'))
# print('n =', n)
# when n = 99 > no error, n = 99. > error (value error)
# 이것은 우리가 고친다고 고쳐지는 에러가 아니다
# 이럴 때 try 구문을 사용해 준다

try:
    n = int(input('정수를 입력하세요>>'))
    print('n =', n)
except ValueError:
    print('입력값은 정수여야 합니다!')
# when n = 99 > no error, n = 99. > 입력값은 정수여야 합니다!
# 아니면 아래 코드를 아예 그냥 사용하지 못 하는데, 이렇게 하면 사용할 수 있다

# 사용자가 정수를 입력할 때 까지 무한 루프로 에러 메시지를 발생하려면?
while True:
    try:
        n = int(input('정수를 입력하세요>>'))
        print('n =', n)
        break #반복문 끝내준다
    except ValueError:
        print('입력값은 정수여야 합니다!')

print('프로그램 정상 종료...')

# while True ~ except 까지 하나의 함수로 만들어서 응용할 수도 있다

# 일부러 에러를 발생시킬 수도 있다 (나이를 입력하세요 -> 마이너스는 없고, 숫자가 아닌 것도 없고,,,)
# 나이에 마이너스등 말도 안되는 값이 들어가 있어서 일부러 에러를 발생시킬 때: raise


