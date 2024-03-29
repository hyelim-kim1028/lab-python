# 직사각형 만들기
class rectangle:
    """
    직사각형 클래스

    """
    def __init__(self,width = 0 ,height = 0): #parameters ; 에러를 막기위해 디폴트값 주기
        # Normally in programming,  __init__ (10+ parameters, mostly default items, to be fixed for optimization)
        self.width = width
        self.height = height

    #method
    def info(self):
        print(f'Rectangle(w={self.width}, h = {self.height})')

    #면적을 계산하는 함수
    def area(self):
        # 여기서 다시 width 랑 height 를 선언해주지 않아도 된다 (모두 self에 들어있음)
        return self.width * self.height

# == 연산자를 사용했을 때 자동으로 호출되는 메소드
    def __eq__(self, other): #eq as equal
        return self.width == other.width and\
               self.height == other.height

    # method 중에 __ 로 시작하고, 끝나는 모든 클래스가 가지고 있는 매소드들이 있다 se llaman 'predefined'

# 객체의 내용을 프린트 할 때 자동으로 호출되는 메소드
    def __str__(self): #string (문자열)
        # return f'<{__name__}.rectangle object at {self}>' #__name__ = 모듈이름
        # return f'<{__name__}.직사각형_객체_주소 object at {self}>' #RecursionError: maximum recursion depth exceeded while calling a Python object
        # return f'<{__name__}. 직사각형 객체 주소>'
    # 주소값을 개발자가 마음대로 사용할 수 없게 해놔서 이럼 ㅜㅠ 엉엉엉
    # 출력의 형태를 우리가 원하는대로 할 수 있다
        return f'<직사각형 가로 = {self.width}, 세로 = {self.height}>'


if __name__ == '__main__':
    rect2 = rectangle()
    # Error: TypeError: __init__() missing 2 required positional arguments: 'width' and 'height'
    # missing arguments
    # argument (__init__) 에 default 값을 주면 비어져있어도 에러가 나지않는다
    # argument 를 아무것도 전달하지 않으면 모든 parameter는 기본값(default argument)를 사용하게 됨
    rect1 = rectangle(3,2) #arguments
    print(type(rect1))
    print(id(rect1))
    rect1.info()
    #print(rect.info()) => null 을 출력
    # info 안 에서는 출력이 되고, print에 넣으면 info 라는 함수는 사실상 다르게 반환하는 값이 없으므로 => NULL

    rect3 = rectangle(1) # positional argument: width = 1, height = 0 (height from default argument)
    rect3.info()

    rect4 = rectangle(height=4) # Invoked using keyword argument
    rect4.info()

    rect5 = rectangle(2,3) # called using positional argument
    rect5.info()

    rect6 = rectangle(width = 2, height=3) #invoked using keyword arguments
    rect6.info()

# rect 5 and 6 are the same rectangles; 메모리에 똑같은 값이 있지만 재사용하지 않고 새로 만든다
# 모양은 똑같이 생겼지만 다른 변수로써 다른 주소값을 갖는다
print(id(rect5)) #2159641968456 => 10진수
print(id(rect6)) #2159641972872
# they have different id serials
# 숫자나 문자열은 재사용하지만 그 외에 다른 모든 클래스들은 생성자를 호출할 때 마다 다른 주소에다가 다른 객체를 만들어 낸다
# 지금 드는 생각은 이건 숫자잖아? 이지만 이건 엄연히 내가 새로 만든 rectangle 이라는 객체
print(rect5 == rect6) #False # after __eq__  value as True
# rect5 와 6은 다른 사각형이라고 반환하다
# 두 개의 객체의 rect 5 &rect6 의 주소를 비교하기 때문에 (값 X, 주소 O)
# obj1 == obj2 comparison method (== 연산자의 동작 방식):
# obj1.__eq__(obj2)
# == 연산자는 클래스의 __eq__함수를 호출

# 기본적으로 == 는 두 객체의 주소값을 비교하게 되어있다, 그래서 모양이 같더라도 다르다고 리턴해 준 것
# 만약에 우리가 두개의 객체가 다른 주소에 있는 것은 신경쓰지 않고 모양이 같으냐, 다르냐만 보고서, 같다 라고 얘기하고 싶으면 함수를 만들면 된다
# def __eq__
print(rect5.__eq__(rect6)) #True

# 개발자가 만들지 않아도 모든 클래스에는 __eq__ 가 있다. 하지만 개발자가 클래스를 정의할 때 __eq__ 메소드를 정의하지 않아도
# 모든 클래스는 __eq__메소드를 가지고 있음
# 기본 __eq__메소드는 개체들의 주소값 (id)를 비교함
# 개발자가 __eq__ 메소드를 다른 방식으로 작성하면 == 연산자는 개발자의 의도대로 True/False 를 리턴하게 됨
# 위에 우리가 함수를 정의한것 처럼

# Area 함수 프린트해보기
print('rect5 넓이:', rect5.area())
print('rect6 넒이:', rect6.area())

print(rect5)
#<__main__.rectangle object at 0x0000025EF9157548>
# __str__을 바꿔준 다음에 프린트물이 <직사각형 가로 = 2, 세로 = 3> 이렇게 출력된다 OhohoH
# 어떤 객체를 출력하려고 하면 모듈이름(__main__). 클래스이름(rectangle) 오브젝트이다 at 0x0000025EF9157548 (주소) => 알파벳이 있는 16진수
# 숫자와 문자를 제외한 다른 클래스는 이렇게 출력해주기로 약속했다 !^0^!
# 이런 <__main__.rectangle object at 0x0000025EF9157548> 걸 만들어주는게 __str__ 메소드
print(id(rect5)) #2159641968456 => 10진수
# 둘은 사실 같은 숫자 ~ ^.~* (windows 계산기 -> 메뉴 -> 프로그래머용 계산기)

