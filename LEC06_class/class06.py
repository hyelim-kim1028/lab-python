# November 13, 2019

from math import pi

class Circle:
    # field: 반지름(radius)
    # method:
    # pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        # if type(radius) != int or type(radius) != float:
        #     raise TypeError('radius는 반드시 숫자타입')
        if self.radius < 0: # < 가 들어간 코드에서 알아서 문자열은 에러가 발생한다!
            raise ValueError('반지름은 0 또는 양수') #이렇게 생각했는데 맞았다
        # 생각하지 못했던 디테일,,!
        # 원의 반지름이 숫자가 아니면 안된다 #오류를 발생시켜버린다
        # 원의 반지름은 마이너스가 되면 안된다 #오류를 발생시켜버린다
    def area(self):
        return pi * (self.radius ** 2) # 내가 3.14로 변수로 줘서 했을 때는 self. pi
    def perimeter(self):
        return 2 * pi * self.radius # 내가 3.14로 변수로 줘서 했을 때는 self. pi
    def __str__(self): #객체가 자기 자신일 때(?)
        return f'<radius = {self.radius}>' #print() 넣으면 안대여!!!!!!! ㅎㄷㄷ
    def __repr__(self): #representation #list 에서도 동작
                        # 출력할 때 사용되는 함수 # list, dict, set 에 들어가는 있는 클래스를 우리가 원하는 형식으로 볼 때  (i.e. Circles)
        return f'원({self.radius})'
    def __eq__(self,other):
       print('__eq__호출')
       return self.radius == other.radius # 등호 == 두개!! 매우 중요 (= 는 값저장)
    # def __ne__(self, other): # not equal
        # != 연산자를 사용하면 자동으로 호출되는 메소드
        # 예) return self.radius == other.radius 해버리면 equal 도 True, not equal 도 True 가 된다

# __eq__ 만 만들어두면 __ne__ 도 그냥 알아서 처리해 준다, 따로 만들어 주면 따로,,, 해주는거고 (정필요하면 두개 다 만들어도 되지만)
# 굳이굳이 둘 다 만들어줄 필요는 없다
# __eq__ 은 필수! __ne__ 은 선택!
# 둘 다 만들어줄 때 조심해야한다 하나가 트루면 다른건 폴스로 출력될 수 있도록 만들어줘야한다!!!!!! 꼭꼭!!!!!!
# __eq__ method 만 작성한 경우, != 연산자는 __eq__ 메소드를 호출한 후 그 결과값의 반대(not)을 사용
# __ne__ method 도 작성한 경우, != 연산자는 __ne__ 메소드의 리턴값을 사용
# == (not -> !=) , > (not -> <)

    def __gt__(self,other): #greater than
        #greater than: > 연산자를 사용하면 자동으로 호출되는 메소드
        print('__gt__호출')
        return self.radius > other.radius

    def __ge__(self,other):
        # greater than or equal to
        # >= 연산자를 사용하면 자동으로 호출되는 메소드
        print('__ge__호출')
        return self.__gt__(other) or self.__eq__(other)
            # 크거나                  #같으면

    # and others more...
    # __lt__: less than (<)
    # __le__: less than or equal to (<=)
    # 이런 크기 비교 연산자들은 왜 있는거지?

if __name__ == '__main__': #'__main__' 으로 실행할 때만 코드들이 실행하게 하겠다
    c1 = Circle(5) # porq no sale nada?
    print(c1)
    print('c1 area:',c1.area())
    print('c1 perimeter',c1.perimeter())
    print('c1 id:', id(c1))  # 생성된 객체의 주소값
                             #2158139095880

    c2 = Circle(5)
    print('c2 id:', id(c2)) #2158139111048
    print(c1 == c2) #c1.__eq__(c2) #True
    print(c1 != c2) #False # != > 이걸 했을 때도 _eq__ 호출 문구도 출력된다
                    # not c1.__eq__(c2)
    print(c1>c2)

    c3 = Circle(3)
    print(c3 == c1) #c3.__eq__(c1) #False
    print(c1>c3)
    print(c3>c1)

# 왜 __eq__ 가 중요할까?
# 우리가 만든 클래스를 리스트에 저장을 한다, sorting 하고싶다 -> 원이 같은지 다른지 비교해야 sorting 할 수 있다
# 그 기준을 우리가 마련해 줘야 크기 비교가 가능하다 (그럴 때 사용하는게 __eq__ modification)

# print (c3 >= c1) 이건 안된다,,, *-*! # not supported by Python
    #__ge__ 함수를 만들어 준 후에 괜찮아졌다!!
    print(c3 >= c1)
    print(c1 >= c3)
    print(c1 <= c3)
    print(c1 < c3)

# 우리가 만든 클래스들을 리스트 안에 넣을 수 있다
    circles = [
        Circle(10),
        Circle(7),
        Circle(100),
        Circle(50),
        Circle(0),
        Circle(50)
    ]

    print(circles)
    # <__main__.Circle object at 0x000002A1258EB708> * 5 ~*-*!
    # __repr__을 줬더니 [원(10), 원(7), 원(100), 원(50), 원(0)] 이렇게 출력되어 나와벌임 !
    # sorting 때문에 이렇게 해줬자나

    print(sorted(circles)) # default by 오름차순 ascending order 로 정리해줬다
    # __gt호출__ 이 왜 많이 나와있지? (파이썬이 큰지 작은지 비교를 해본거지)
    print(sorted(circles, reverse = True))
    # reverse = True -> descending order

# Circle(50) 을 하나 더 넣어줬는데, 그냥 --gt--로 끝내버렸어 --ge-- 은 안쓰고?!

# 문자열 비교
# 1 < 2, a < b, 가 < 나, a < 가 (사전순서, 영어보다는 한글보다 나중에 나와서 더 크다고 비교된다)

# class03으로 갔음