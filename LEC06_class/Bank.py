"""
LEC06_class\class07.py 파일에서 작성한 Account 클래스를 사용해서 은행 어플리케이션 만들어보기
1) 본인확인 - 이름, 주민번호, 핸드폰번호, 이메일주소
2) 거래내역조회 - 통장 (account), 입/출금 시간정보 , 비고
3) 예금, 적금 , 출금
4) 대출
5) 신용 조회
6) 전계좌조회 - customer class + account class 를 이어주는 무엇인가가 있어야한다
7) 자동이체
8) 이상 출/입금 관리
# 어떤 데이터가 있어야할까 => 클래스 설계

#우리가 할 것
1) 거래내역 조회
2) 입금, 출금, 이체
"""

from LEC06_class.class07 import Account
    #파일이름.모듈이름          #클래스이름

# we have to consider the GUI (graphic user interface)

print("Banking Application")
# 여러 게좌들을 관리하기 위한 dict를 선언
# dict 의 key = accountno, value = Account 객체 자체

accounts = {} # create an empty dictionary

while True: #계속 다시 첫 화면 메뉴로 돌아가는 무한루프
    # Main Menu (첫 화면 메뉴)
    print('[0] 종료')
    print('[1] 계좌 개설')
    print('[2] 입금')
    print('[3] 출금')
    print('[4] 계좌 이체')
    print('[5] 계좌 정보 출력')
    print('----------------------')
    print('>> 선택')
    menu = input()
    # 무한루프를 멈추는 라인을 넣어준다
    # 종료되는 조건 => print('[0] 종료')
    if menu == '0':
        break
    elif menu == '1': # 새로운 계좌 개설 선택
        print('----신규 계좌 개설 화면------')
        # print('계좌번호 입력>>')
        account_no = int(input('계좌번호 입력>>'))
        money = int(input('잔액 입력>>'))
        accounts[account_no] = Account(account_no, money)
        # print(accounts) # 이게 없어서 출력이 안된거였다
        # dict 의 key = accountno => accounts[account_no], value = Account 객체 자체 Account(account_no, money)
        # 겹치는 account_no는 없다
    elif menu == '2':
        print('---입금 화면---')
        account_no = int(input('입금할 계좌 번호>>'))
        money = int(input('입금 금액>>'))
        accounts[account_no].deposit(money)
    elif menu == '3':
        print('---출금화면---')
        account_no = int(input('출금할 계좌 번호>>'))
        money = int(input('출금 금액>>'))
        accounts[account_no].withdrawal(money)
    elif menu == '4': #이체: 계좌번호 두개 입력
        print('---이체화면---')
        from_acc = int(input('내 계좌번호 입력>>'))
        to_acc = int(input('상대방 계좌 번호 입력>>'))
        money = int(input('이체할 금액'))
        accounts[from_acc].transfer(accounts[to_acc],money)

        # what I thought was correct:
        # account_no = int(input('이체할 계좌 번호>>'))
        # money = int(input('이체할 금액>>'))
        # accounts[account_no].withdrawal(money)
        # accounts[account_no].deposit(money)
    elif menu == '5':
        print('---계좌 조회 화면---')
        accout_no = int(input('조회할 계좌번호를 입력하세요>>'))
        print(accounts[account_no])

print('Banking App Finished')





