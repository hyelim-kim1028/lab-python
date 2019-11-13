"""
클래스 사용 예
"""
s = 'hello' #객체를 생성한다
print(s.capitalize()) # 생성된 객체의 변수이름을 가지고 함수를 사용할 수 있다
# m for method
#  s 가 가지고 있는 함수를 호출을 했더니 출력이 함수를 거쳐서 됨
# 여기에서는 문자열을 저장하고 조작하는 기능들을 가지고 있는 대상을 만들고 싶은데, 그 대상이 str 이라는 클래스 이고,
# str 클래스는 문자열들을 저장하고 조작할 수 있다. 이 기능들을 method 라고 일컫는다

print(s.upper())
# upper -> changed all the letters into uppercase letters

# s의 클래스 타입 확인
print(type(s))

print(s.find('l'))
# returns the index of a specific letter

# 이런 클래스를 만드는 것을 공부하겠다


# volvimos a class01
# volvimos a intro despues de linea 145 en class01

s2 = 'python'
print(type(s2))
print(s2.capitalize())
# give the function capitalize the address of s2
print(s2.capitalize())
print(s2.upper())
print(s2.find('l'))
# there is no letter such as 'l' and Python returned -1
# Python returning a negative number as its index means that it was not able to find any
# hello 와 python 은 class 는 같은데 객체가 다르다 = 우리의 시각으로 보자면 같은 모델의 컴퓨터이지만 둘은 다르다
# 기능은 같다, 같은 설계도와 사양으로 만들어진 객체들이지만, 고로, 동작원리는 같지만 데이터가 무엇이냐에 따라 결과는 다르다

# volvimos a class01


































































