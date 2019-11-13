# November 11, 2019

"""
함수에서 return 의 의미
1) return 을 만나는 자리에서 함수를 종료하겠다 (end the function)
2) 함수를 호출한 곳에 값을 반환하겠다 (return a value)

yield: 반복문 안에서만 함수의 결과를 순차적으로 반환할 때 (https://stackabuse.com/understanding-pythons-yield-keyword/)
# keep the values and return the values within a 반복문
"""

# return 을 만나는 자리에서 함수를 종료하겠다
def test():
    x = 0
    while x < 4:
        return x # x = 0, 여기서 바로 함수를 끝내버림 -> 결론적으로 이미 함수가 반환을 끝냈기 때문에 x += 1 은 절대로 실행될 수 없는 코드가 됨
        x += 1 #절대로 실행되지 않는 문장

for i in range(4):
    print(test())
# 4번 호출을 해도, 증가가 되지 않고, 0을 4번 출력해준다


# yield 를 사용하는 함수
def four():
    x = 0
    while x < 4:
        yield x
        x += 1
# test 함수와 다른점은 1) 이름이 바뀐것 2) return 대신 yield 를 쓴 것
# 이 값들을 반복하면서 내부적으로 가지고 있는 값들이 언제 하나씩 밖으로 나가느냐: for 문 안에서,

print(four()) # return the address of a generator (???)
# generator is used within the for-loop

for x in four():
    print(x) # 0,1,2,3을 출력
# yield 는 generator 를 만들기 위해서 사용한다 -> generator 는 for..in.. 구문에서만 사용한다
# range 라고 하는 함수가 yield 를 이용해서 만들어진것

print(range(4))
# range 는 for 문 안에서 하나씩 값을 반환해주던 함수: 그래서 range 는 return 이 아니라 yield 를 사용하고 있었다
print(range(1,4))

# range를 흉내내서 만들어보기
def my_range(start = 0, end = 1):
    x = start
    while x < end:
        yield x
        x += 1

print(my_range())
# solo se vuevla: generator
# we have to use this function within a for-loop

for x in my_range(start = 1, end = 5):
    print(x)
# returns 1,2,3,4 # while x < end:

for x in my_range(end = 5):
    print(x)
# desde 0 a x < 5 (entonces, 0,1,2,3,4)

# 이런 유형의 아이들을 generator 이라고 하고
# 메모리를 더 효율적으로 사용하기 위해서
# yield 를 사용하면 값이 포문 안에서만 리턴이 되고, 메모리에 키핑되지 않는다
# 미리 한꺼번에 무언가를 만들어두지 않는다

