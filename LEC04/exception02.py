"""
try 구문:
try:
    실행할 문장들 (indentation *****)
except 에러 종류 [as 별명]
    에러가 발생했을 때 실행할 문장들
[except 다른 에러: 코드] - 필수 아님
else:
    에러 없이 try 블록 안의 모든 문장이 정상적으로 실행됐을 때 실행할 코드
    - else 구문도 필수 아님
    - 아니면 그냥 try 구문 마지막에 넣어도 괜찮지 않은가?
finally:
    에러 발생 여부와 상관없이 반드시 실행할 문장들을 작성
    - 필수 아니라서 있어도 되고 없어도 된다ㅏㅏ
# 구냥 첫번째 except 이후로는 다 그냥 필수도 아니고 있어도 되고 없어도 되고 둥가둥가 예예

# when there was no error: try -> else -> finally
# when there was an error: try -> except -> finally  (skipped error because there was an error/ else is only for when there was no error at all)
"""

# try:
#     numbers = [1,2,3]
#     for i, v in enumerate(numbers):
#         # enumerate안에 리스트와 같이 주면: index 와 values 를 같이 준다
#         print(i, ':',v)
# SyntaxError: unexpected EOF while parsing -> grammatical error
# because there was no 'try' in this structure
# Hay que tener un 'except' por lo menos en try
# try:
#     numbers = [1,2,3]
#     for i, v in enumerate(numbers):
#             # enumerate안에 리스트와 같이 주면: index 와 values 를 같이 준다
#         print(i, ':',v)
# except IndexError:
#     print('인덱스 에러 발생')
# else:
#     print('try의 모든 내용을 정상적으로 실행')
# finally:
#     print('finally  BLOCK')
# try -> else -> finally 이 수순을 밞는 코드가 탄생

try:
    numbers = [1,2,3]
    for i in range(1,4):
        print(i, ':', numbers[i]) # IndexError: list index out of range
except ValueError: # 원래 Index Error
    print('인덱스 에러 발생')
else:
    print('try의 모든 내용을 정상적으로 실행')
finally:
    print('finally  BLOCK')
# try -> else -> finally 이 수순을 밞는 코드가 탄생
# finally BLOCK 은 실행이 되는데 에러가 나왔다
# 이렇게하면 비정상적으로 종료되는것을 방지: 끝까지 다른 일들을 할 수 있도록 해준 것

# 모든 에러가 아니라 우리가 잡고 싶은 에러만,,,
# If we dont specify which type of error we are facing, the system wont be able to catch any and the code cannot capture any neither

try:
    numbers = [1,2,3]
    for i in range(1,4):
        print(i, ':', numbers[i]) # IndexError: list index out of range
except ValueError: # 원래 Index Error
    print('값 에러 처리')
except IndexError:
    print('Index Error')
else:
    print('try의 모든 내용을 정상적으로 실행')
finally:
    print('finally  BLOCK')
# 정상 종료,,,?
# 좋은 방법은 아니다


