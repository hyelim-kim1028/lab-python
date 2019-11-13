#반복문 연습 3
# 1 + 2 + 3 + ... 100 = ?

#Using while
# n = 1
# sum = 0
# while n <= 100:
#      sum = sum + n
#      n += 1
# print(sum)

total, n = 0, 1 #이렇게 변수를 선언할 수도 있다
while n <= 100:
    total += n
    n += 1
print(total)

#Using For: My answer/ Wrong
# total = 0 #shadow built-in name 'sum' (sum 이라는 함수가 있다) # 이제는 썸이라는 함수는 사용할 수 없다 (shift + F6)
# for i in range(1, 101):
#     total = total + total[i] #sum += x
    # if i > 101:
    #     break
# print(total)

# shift + F6: refactor/rename 이라는 기능
# 변수 이름을 바꿔주겠다! 라는 것
# 바꾸고싶은 기능에다 커서를 누르고 shift + F6 그러면 모든 sum이 내가 지정한 이름 (total)로 바뀐다

# Teacher's solution
# total = 0
# for x in range(1,101):
#     total += x
# print(f'sum = {total}') # Indent here means to show all the calculated numbers

#Method 2
# n=100
# print((n*(n+1))/2)

#Method 3: List comprehension
# numbers = [x for x in range(1,101)]
# print(sum(numbers))

# Question 2: 1 + 2 + 3+ ... + x <= 100

#Using while
# n = 1
# sum = 0
# while n:
#     sum = sum + n
#     n += 1
#     if sum == 100:
#         break
# print(f'{sum},{n}')

total = 0
x = 1
while True:
    total += x
    print(f'x = {x}, sum = {total}')
    if total > 100:
        break
    x +=1

# total, x = 0,1
# while total <= 100:
#     total += x
#     print(f'x = {x}, sum = {total}')
#     x+=1

#Using for

# sum = 0
# for i in range(1,101):
#     sum = sum + sum[i]
