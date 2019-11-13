#November 06, 2019
# for - in 구문 연습
# 구구단 2단부터 9단까지 출력

# for dan in range(2,10):
#     for n in range(1,10):
#         print(f'{dan} X {n} = {dan * n}')
#     print('-------------')

#구구단을 출력하는데 2*2, 3*3 까지,,, 이런식으로 출력
 # for dan in range(2,10):
 #     for n in range(1,10):
 #         if dan >= n:
 #             print(f'{dan} X {n} = {dan * n}')
 #     print('-------------')

#Method2
# for dan in range(2,10):
#     for n in range(1,dan + 1):
#             print(f'{dan} X {n} = {dan * n}')
#     print('-------------')

# Method3
for dan in range(2,10):
     for n in range(1,10):
         print(f'{dan} X {n} = {dan * n}')
         if dan == n:
            break   #break 가 포함된 가장 가까운 반복문을 종료하겠다
     print('-------------')

# continue: 결과를 다시 실행하러 올라가는?
for i in range(1,10):
    if i == 5:
        continue
    print(i, end = ' ')
    # 5가 빠져있다, 왜지?
    # 계속하겠다, continue에서 시작하는 지점으로 돌아간다
    # for문 안쪽에 다른 것들은 실행을 하지 않고, 5 는 건너고 다음 숫자들 부터 실행



