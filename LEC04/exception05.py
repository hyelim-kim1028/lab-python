# def user_input():
# #     """
# #     가위바위보 게임! 1,2,3 세가지 숫자 중 한가지를 선택하라고 안내한다
# #     사용자가 입력한 숫자를 return 한다
# #     :return: 1,2,3 중에 하나를 리턴
# #     # 사용자는 1,2,3 외에 숫자가 아니거나 숫자로 변환할 수 없는 문자를 입력하면 안내문 출력후에 다시 입력 받아야한다
# #     사용자가 1,2,3 이외의 숫자를 입력했을 때도 마찬가지로 1,2,3 숫자가 아니면 안됩니다 라는 안내문 출력 후에 다시 입력받음
# #     """
#     while True:
#         try:
#             n = int(input('1,2,3 중에 숫자 하나를 입력하세요>>'))
#             if n < 1 or n > 3:
#                 raise ValueError('Number in between 1 to 3')
#             print(n)
#             if n == 1 or n == 2 or n ==3: #n in (1,2,3) => tuple!
#                 break
#         except ValueError as e:
#             print(e.args)
# print('프로그램을 정상적으로 종료합니다')
# 진짜 리턴 문장이 없네,,, 그런데 되긴됐음 - 띠용 갑자기 안됨

# # teacher's version
def user_input2(): #return n value HERE
    while True:
        try:
            n = int(input('1,2,3 중에 숫자 하나를 입력하세요>>'))
            if n in (1,2,3):  # => tuple!
                return n # 여기서 함수가 끝나 버린다
                         # break 도 가능 -> while 문 끝나고 나온 시점에 print('') 하나 넣어줘야한다
            else:
                raise ValueError() #일부러 Raise 를 넣어서 사용자로 하여금 정확한 값만 입력하게 만드는 방법
        except ValueError:
            print('입력값은 반드시 1,2,3  중에 하나여야 합니다 ') # 여기 끝나면 다시 while 로 올라가야하는 while-loop
    # break 쓰면 여기다가 return n 이라고 해주어야함 (indent 는 While True 에 맞춰서!)

user = user_input2()
print('입력 값=', user)


# 입력값에 따라서 에러가 발생하고 안하는 경우에는 try - error 방법이 맞을 수도 있다

# chapter 3 review