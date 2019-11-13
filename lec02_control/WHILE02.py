#November 06, 2019
"""
while 문 연습 2
"""
#일부러 무한루프를 만들고 무한루프를 빠져나가는 걸 만들 때
while True:
    print('[1] 입력')
    print('[2] 수정')
    print('[3] 삭제')
    print('[0]종료')
    print('----------------')
    print('메뉴 선택 >>')
    menu = input()
    if menu == '0':
        break
print('프로그래 종료')

# while True 이라면 break 를 걸거나 조건식이 없는한 무한 루프 (이렇게하나 저렇게하나 참이니까)
# 가위바위보 모델 만들기
# while 0: 으로 주면 밑에 실행하지 않겠다 (선배의 선배코드 if(0) ... else... ^0^)

