#Fibonacci sequence
# f[0] = 0
# f[1] = 1
# f[n] = f[n-1] + f[n-2], n >= 2

#MY SOLUTION
# f = []
# f.append(0)
# f.append(1)
# for i in range(2,20):
#      f[i] = f[i-1] + f[i-2] # 이렇게 할 수 없다 > 인덱스가 생성되어 있지 않으니까 (index error: out of range)
#      f.append(f[i])
# print(f)


#TEACHER'S SOLUTION
#피보나치 수열 원소 20개짜리 리스트를 생성
f = [0,1]
for n in range(2,20):
    f.append(f[n-1] + f[n-2])
    #for n in range(0,18)
    # f.append(f[n+1] + f[n])
print(f)

# Prime number (1과 자기 자신만으로 나누어지는 정수?)
# 2 부터 10까지의 정수들 중에서 소수를 찾아서 출력

# p = [1,2,3,4,5,6,7,8,9,10]
# for p in range(1,11):
#     if p == p:
#         print(1*p)
#     elif p // 2 > 1:
#         continue
#     elif p // 3 > 1:
#         continue
#     else:
#         print(1*p)
# print(p)

# 생각의 전환: 나머지가 있어야 정수가 아니다

# for p in range(1,11):
#     print(p)

# 이 부분 노트 정리 잘 하기

# teacher's solution
for n in range(2,11):
    isPrime = True
    for divider in range(2,n): # 자기 자신보다 하나 낮은 숫자까지 비교해서 나눠보면 되니까 자기 자신까지 (보통 파이썬은 그래요)
        if n % divider == 0:
            print(f'{n} = {divider} x {n/divider}')
            isPrime = False
            break
    if isPrime:
        print(f'{n}은 소수!')

# for/while 반복문과 else 가 함께 사용되는 경우:
# 반복문이 break 또는 continue를 만나지 않고 범위 전체를 반복했을 때
# else 블록이 실행이 된다
# 반복문 중간에 break 또는 continue를 만나면 else 는 실행이 되지 않는다

for i in range(5):
    if i == 5:
        break
    print(i,end=' ')
else:
    print('모든 반복을 끝냄')

print()

# i == 3을 만나서 break 를 만났을 때는 else 는 실행이 되지 않았고, i == 5 로 바꾸어서 break 를 안 만났을 떄에는 else 까지 나왔다

for i in range(5):
    if i == 3:
        continue
    print(i,end=' ')
else:
    print('모든 반복을 끝냄')
# 3만 빠지고, else 포함한 나머지 전체 출력
print()

# for - else 구문을 사용한 소수 찾기
for n in range(2, 11):
    for divider in range(2, n):
        if n % divider == 0:
            break
    else: # break 를 만나지 않았을 때 실행된다 # break 를 만났으면 약수를 찾았으므로 소수가 아니다 #그러므로, 약수가 없다는 것은 소수라는 의미
        print(f'{n}은 소수')

