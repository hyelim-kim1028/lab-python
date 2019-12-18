# method 만들기 연습
# 은행계좌 ^0^


class Account:
    min_balance = 0
    """
    은행 계좌 클래스
    field: 계좌번호, 잔고/액
    # 은행계좌가 가져야할 데이터들
    method: 입금 (deposit), 출금 (withdrawal), 이체(transfer)
    """
    def __init__(self, accountno, balance):
        self.accountno = accountno
        # 숫자타입만 들어올 수 있도록, 아니면 에러가 나게끔 만들 수 있다
        self.balance = balance
        # idea 2
        # try:
        #     temp = balance + 1
        # except Exception:
        #     raise TypeError
        # unique to Python
        # temp = balance + 1 에서 balance 에 문자가 들어오면 (temp는 쓰이지도 않는 변수임) 에러가 어짜피 발생하니까 그렇게 보내버리기 ^^
        # duck typing : 꽥꽥 거리면 오리고, 꽦꽦거리지 않으면 오리가 아니다 ( 1을 더할 수 있으면 숫자고 아니면 숫자가 아니다)

        # idea 1
        # #타입을 체크하는 function 이 있다
        # if not isinstance(balance, int) and \
        #    not isinstance(balance, float):
        #    raise TypeError('')
        #         # returns boolean type
        #    # \문장 안 끝났다라는 표시

    def __repr__(self):
        return f'Account(account no: {self.accountno}, balance: {self.balance})'

    def deposit(self, amount):  # amount 라는 파라미터: 얼마를!
        # idea 1
        # self.salary = (1 + pct) * self.salary  # this formula is the same as: self.salary *= 1+pct
        # return self.salary
        # if self.accountno: # 내가 하고 싶은 말: if self.accountno = True 라면 # 이게 맞는 걸까
        #     # 이걸 어떻게 주지
        #     self.balance += amount
        #     return self.balance

        # idea2
        # if amount > 0:
        #     self.balance += amount
        #     print(f'Accountno = {self.accountno}, Remaining Balance = {self.balance}')
        # else:
        #     print('Deposit impossible below $0')
        #
        # fixed
        if amount <= 0:
            raise ValueError('Deposit impossible below $0')
        self.balance += amount
        print(f'Accountno = {self.accountno}, Remaining Balance = {self.balance}')

        # idea 2
        # if amount < 0:
        #     raise ValueError('Deposit impossible below $0')
        # self.balance += amount
        # print(f'Accountno = {self.accountno}, Remaining Balance = {self.balance}')

    def withdrawal(self,amount):
        # if self.accountno:
        #     self.balance -= amount
        #     return self.balance
        # # elif self.balance <= self.min_balance:
        # #     print('No remaining balance')
        # if self.balance > 0:
        #     self. balance -= amount
        #     print(f'Accountno = {self.accountno}, Remaining Balance = {self.balance}')
        # elif self.balance <= 0:
        #     raise ValueError('No remaining balance')
        # else:
        #     print('Amount too big to be withdrawn')
        # return self.balance

        # fixed
        if amount < 0:
            raise ValueError('Not logical withdrawal')
        elif self.balance < amount:
            raise ValueError('Amount too big to be withdrawn')
        self.balance -= amount
        print(f'Accountno = {self.accountno}, Remaining Balance = {self.balance}')

        # teacher's solution (money is an equaivalent to my amount)
        # if money < 0:
        #     raise ...
        # elif self.balance < money:
        #     raise ...
        # self.balance -= amount
        # print


    def transfer(self,other,amount):
        """
        계좌 이체 기능. 내 계좌에서 금액을 출금해서 상대방 계좌에 입금한다
        :param other: 이체할 상대방 계좌 (Account 클래스 객체)
        :param amount: 이체할 금액
        :return: None
        """
        self.withdrawal(amount)  # 내 계좌에서 출금
        other.deposit(amount)  # 상대방 계좌에서 입금

        # if other.accountno:
        #     # 내가 하고 싶은 것: 다른 accountno 에 입금 시키는것 -> 내가한 것 그냥 accountno 을 amount 만큼 증가 (un cambio en accountno)
        #     other.balance += amount
        #     print(f'Accountno = {other.accountno}, Remaining Balance = {other.balance}')
        # else:
        #     print ("Fraud detected")




if __name__ == '__main__':
   #  account1 = Account(1234, 1000) #Account() = 생성자
   #  # __str__ 은 문자 단독만, __repr__ 은 리스트나 튜플도 가능
   #  print(account1)
   #  # before __repr__: <__main__.Account object at 0x000002214D6561C8>
   #  # after __repr__: Account(account no: 1234, balance: 1000)
   #  account1.deposit(100)
   #  # account1.deposit(0)
   # # print(account1.withdrawal(1500))
   #
   #  account2 = Account(5678,500)
   #  account3 = Account(7890,100)
   #  print(account1.transfer(account2, 100))
   #  print(account1.transfer(account3,100))

     account1 = Account(123, 1000)
     print(account1)
     account1.deposit(500)
     account2 = Account(789, 100)
     account1.transfer(account2,500) # 두 줄이 출력되었다
     print(account1)
     print(account2)