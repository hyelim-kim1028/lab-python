# p.230 # 13,14,15

# 13.
# for j in range(1,8): #7 rows
#     for j in range(1,j): #7 stars
#         print('T',end = ' ')
#         if j > 8:
#             break
#     print()

strT = 1
row = 1
while row < 8:
    strT += 1
    while row == strT:
        print('T', end =' ')
    row += 1
print()


#14
# 앞에 패드를 주고 마지막에 j = j 만 T 를 출력
# for j in range(1,8): #7 rows
#      for j in range(1,8): #7 stars
#         print(end = ' ')
#      for j in range(1,8):
#          print('T', end = ' ')
#      print()

#the correct one
# for i in range(0, 7):
#     for j in range(0, 6 - i):
#         print(' ', end='')
#     for k in range(0, i + 1):
#         print('T', end='')
#     print()
# print()

#15. 13번과 14번을 while loop으로 풀기
