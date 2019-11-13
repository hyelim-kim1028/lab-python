"""
재귀 함수(recursive function)
- 내용은 어려운데 코드는 쉽다,,,^^
"""
# 재귀 함수를 잘 알면 코드를 간단하게 줄일 수 있다.
# factorial!
# n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! * n
# (n-1)! * n 이 재귀이다, factorial 을 계산하려고 했는데 그 속에서 또 들어가는 것 -> 재귀

# 막간 연습: factorial 을 for 문으로 만들어 보기
# 0! =1  ( int > 0 에는 n! = 1 x 2 x 3 x ... x (n-1) x n 으로 약속한다)

def factorial1(n:int) -> int:
    result = 1 # 0! =1
    for x in range(1,n+1): # 0을 곱하면 안되니까 1부터로 해준다
        # 굳이 if n > 0은 안줘도 된다 ( 0 = n, n + 1 =1 이니까)  (음수 안된다는 주석으로 넣어줘도 된다)
        result *= x # result = result * n
    return result

for x in range(6):
    print(f'{x}! = {factorial1(x)}')

def factorial2(n: int) -> int:
    if n == 0:
        return 1
    elif n > 0:
        return factorial2(n-1) * n

print("============")
for x in range(6):
    print(f'{x}! = {factorial2(x)}')

# 내가 나를 또 부른다고 해서 재귀함수라고 한다
# 하지만 잘못 사용할 경우 위험위험 (끊임 없이 계속 들어가면 -> infinite loop)
# EX) stack overflow (임시로 저장되는 값들이 지워지지 않고 계속 쌓이는 것 OS가 준 값들이 한계치를 넘으면 메모리가 터져벌임...^^)
# 그래서 재귀함수에는 꼭 나올 수 있는 구멍이 있어야함 (like a white-whole)
# def factorial2(n: int) -> int:
#         return factorial2(n-1) * n

# 1 ~ n 까지 더하기 하는 것 등 모두 재귀함수 사용가능 # 만들어 보기
def rec_sum(n:int) -> int:
    if n == 0:
        return 0
    elif n > 0:
        return rec_sum(n-1) + n

print("============")
for n in range(6):
    print(f'sum = {rec_sum(n)}')


# 재귀 함수를 사용한 하노이 탑
#

def hanoi_tower(n: int, start, target, aux) -> int:
    """
    재귀 함수를 사용해서 하노이 탑 문제 해결 방법 출력
    :param n: 옮길 원반의 갯수 ( n > 0인 양의 정수)
    :param start: 시작하는 기둥 (원반들이 있는 출발 기둥 번호)
    :param target: 타겟 기둥 (원반들을 모두 옮겨 놓을 타겟 기둥 번호)
    :param aux: 보조 기둥 (원반들을 옮길 때 보조 기둥으로 사용할 기둥의 번호)
    :return: None
    """
    if n == 1:
        # 1 -> 3: 끝
        print(f'{start} -> {target} ')
        return # 함수를 종료하겠다라는 뜻, 리턴값을 구지구지 안줘도 된다,
               # 또한 재귀함수의 특성상 들어가고 들어가고 들어가다가 n == 1이 되는 시점이 오면 함수를 종료시켜줘야함 아니면 계속 돌아가는 것
    if n > 0:
        #(n-1)개의 원반을 보조 기둥(aux)
        # (n-1)개의 원반을 target을 보조 기둥으로 사용해서 aux 기둥으로 모두 옮김
        hanoi_tower(n - 1, start, aux, target)
                            # 우리는 지금 n - 1개를 aux 자리에 모두 옮겨두고 싶으니까, target 파라미터에 aux 를 둔 것
        print(f'{start} -> {target}')
        # 이제 aux 가 start 가 되고, target에 옮겨 놓기 위해서 start 가 aux 가 된다
        # aux 기둥에 남아있는 (n-1)개의 원반을 start 기둥을 보조 기둥으로 사용해서 target 으로 옮김
        hanoi_tower(n-1, aux, target, start)

# 원반 한개짜리 하노이 탑
hanoi_tower(n = 1, start = 1, target =3 , aux = 2)
# n = 1 인 경우, print(f'{start} -> {target}') 만 주면 끝난다

for n in range(1,5):
    print('하노이 타워')
    hanoi_tower(n, start = 1, target = 3, aux = 2)
    print('=======================')


    #  응 또 삽질
    # when disc = n
    # do I make it a list of three tuples? [(),(),()] -> 그럼 가변길이 인수로 만들어야하나...?
        # Disc 1 to n
        # pegs A (start), B(auxiliary) , C(target)
        # Disc 1, 2, 3 in A [(1,2,3),(),()]
        # Disc 1 to C [((n-1),n),(),(1)]
        # Disc(n - 1) to B [(n),((n-1)),(1)]
        # Disc 1 to B [(n),((n-1),1),()]
        # Disc n to C [(),((n-1),1),(n)]
        # Disc 1 to A [(1),((n-1)),(n)]
        # Disc(n - 1) to C  [(1),(),(n,(n-1))]
        # Disc 1 to C [(),(),(n,(n-1),1)]
    # if n == 1:
    #     return A to C [(),(),(1)]
    # if n > 1:





# Tried to find 2**n - 1 as a recursive formula and failed
#     if n == 0:
#         return 0
#     elif n > 0:
#          return tower_of_hanoi(2**((n-1)*n)) - 1
#
# for n in range(5):
#     print(f'tower_of_hanoi = tower_of_hanoi(n)')
























