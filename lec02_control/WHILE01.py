#
'''
while 반복문:
[초기식]
while 조건식:
    조건식이 참인 동안에 실행할 문장
    [조건을 변경할 수 있는 식]
# 대괄호 안의 아이들은 없어도 됩니다
'''

#1 ~ 10 옆으로 출력
# n = 1
# while n <= 10:
#     print(n, end= ' ')
# print()
# 이렇게하면 무한대로 생성한다
# for 과 while 은 다르다

n = 1
while n <= 10:
    print(n, end= ' ')
    n += 1 # n = n + 1
print()
# 자주하는 실수1: n = 1 처럼 첫번째 값 안주는 경우: 이러면 식을 시작할 수 없어요

# while 문을 활용하여 구구단 출력해보기
n = 1
while n < 10:
    print(f'2 X {n} = {2 * n}')
    n += 1
print()

# while문을 활용하여 2~9단까지 구구단 출력해보기

dan = 2
while dan <= 9: #or dan < 10
    n = 1 #이게 위에 있을 때는 2단만 출력됬는데, 밑으로 내리니까 바로 문제 해결됨 (왜일까요)
          # 다음에 단이 들어올 때 (2->3 so on) 에 1부터 다시 시작
    while n < 10:
        print(f'{dan} X {n} = {dan * n}')
        n += 1 #n 이 빠져나오고 dan 으로 토스된다
    dan += 1
    print('---------------')
print()

dan = 2
while dan < 10:
    n = 1
    while n < 10:
        print(f'{dan} X {n} = {dan * n}')
        if dan == n:
            break
        n += 1 #어디에다 넣느냐가 매우 중요하다
    dan += 1
    print('---------------')
print()

