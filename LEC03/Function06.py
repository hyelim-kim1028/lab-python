"""
variable-length (가변길이) keyword argument
함수 정의할 때 파라미터 이름 앞에 **를 사용
함수 내부에서는 이 argument 를 dict 처럼 취급한다
"""

def test(**kargs):
    print(kargs)

test()
test(name = '오쌤', age = 16)
# argument 를 키워드를 붙여서 넣으면 the function deem these as pairs
# there is no defined paramters, we can just give any and python receives it in a dict format

# dict 를 for … in … 구문에다 넣어주면 key words 만 뽑아준다
def test(**kargs):
    print(kargs)
    for key in kargs:
        print(key)
test(name = '오쌤', age = 16)





























