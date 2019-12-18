"""
상속(inheritance)
- 조/부모님으로부터 물려받는 것
- 파이썬에서도 부모클래스, 자식클래스가 있다 (부모 클래스로부터 물려받는 것)
- 데이터/필드와 메소드를 물려 받는다
- 처음엔 코드 재활용때문에 생긴 컨셉
- 파이썬에서는 어떻게 해야 상속 받을 수 있을까?

- 정리: 부모 클래스로부터 데이터(filed)와 기능(method)를 물려 받아서 자식 클래스에서 사용할 수 있도록 하는 개념
- 부모클래스: parent (부모), super (상위), base (기본) class
- 자식클래스: child (자식), sub (하위), derived (유도) class

# 예:
shape 이라는 부모클래스를 갖는 사각형, 원 등의 자식클래스를 생성해보자
"""
# 상속을 잘못하면 코드 재사용에 문제가 있을수도 있다

class Shape:
    # 모든 도형은 시작점이 있어야 만들 수 있지 않을까?
    def __init__(self, x = 0, y = 0):
        print('Shape__init__호출')
        self.x = x
        self.y = y

    def __repr__(self):
        # 출력문을 만들어 줄 때 사용하는 함수이고, 문자열을 리턴해준다
        return f'Shape(x = {self.x}, y = {self.y})' # shape 클래스에 있는 repr 이 차일드 클래스에 __init__ 을 만들고 에러가 났다

    def move(self, dx, dy): #이동시킨다
        self.x += dx
        self.y += dy
    # 중심, 시작점을 옮기면 도형자체가 옮겨갈 수 있다

# 색칠을 하는 동작/기능은 같지만 방법은 도형마다 조금씩 다르지 않을까?
    # 사각형에서는 w*h 만큼, 원에서는 pir**2 만큼 색칠하고,,, area (면적)을 알아야 색칠할 수 있어야한다
    # each child class would have its own area to be colored/ filled
    # en todos modos, we have to know their area first
    def area(self):
        """
        # shape 객체는 넒이를 계산할 수 없다
        # shape의 sub 타입들인 rectangle, circle 객체가 각자의 방식으로 넒이를 계산 해야됨
        :return:
        """
        #pass  # is the same as return none
        raise NotImplementedError('반드시 override 하세요 (Haz el override)')
    # 메소드는 있지만 그냥 넘어가야한다 -> 문법적으로는 오류가 없다
    # area 라고 하는 것을 이용해서 다른 메소드를 만든다 -> draw
    def draw(self):
        """
        넒이를 계산하는 area() 메소드를 사용해서 도형 내부를
        그려주는 메소드 (not dealing with graphics but we are trying to understand the concepts on how drawing functions work)
        :return: None
        """
        print(f'drawing {self.area()}...*-*!')
    # there should be a value in self.area (the developer deems as there is a area of a shape given)
    # Method invocation: 호출이 끝나면 메소드가 리턴해주는 값이 자리로 온다
    # For now our area() is not working

class Rectangle(Shape):
    # 파이썬에서 상속을 받을 때 () 괄호 안에다 super class 의 이름을 적어준다
    # class Child(Parent)
    # 이런 문법은 언어마다 조금씩 다르다 (C##  child_class :: Parent class / java ch extends pa)
    # 기본은 차일드 클래스 이름을 써주고, 옆에다 페어런트 클래스의 이름을 써준다

 # child class 에서 __init__ 함수를 작성하지 않은 경우에는 파이썬 interpretor 가 parent class 의 __init__ 메소드를 호출해서 부모 객체를 자동으로 생성합니다
    # 그런데, 개발자가 child class 에서 __init__ 메소드를 정의한 경우에는
    # Python interpretor 가 parent 클래스의 __init__ 메소드를 자동으로 호출하지 않는다
    # 그렇기 때문에 child class 에서 parent class 의 __init__ 메소드를 명시적으로 호출해야한다
    def __init__(self, w = 0, h = 0, x = 0, y=0): #__init__ 함수를 만들어주고 에러가 생겼다
        print('Rectangle.__init__ 호출')
        # How to invoke the parent class in child class: (부모클래스의 __init__호출)
        super().__init__(x, y) #super() 의 클래스가 __init__의 첫번째 파라미터로 들어간다
                              # super(). 이 self 의 주소라서 self 를 넣어주지 않는 것
        # Since super() has default numbers, it might not be an obligatory process to give parameters to the super class
        # However, we can give it under child class as well (also include x,y as the parameters in the child class/ line 46)
        self.w = w
        self.h = h

#override: 부모 클래스로부터 상속받은 메소드를 자식 클래스에서 재정의하는 것
    def __repr__(self):
        return f'사각형(가로 = {self.w}, 세로 = {self.h}, 시작점x = {self.x}, 시작점y = {self.y})'
        # rectangle class에서는 위의 __repr__은 없어지고 얘만 남는다
        # this process is called 'override' (부모로부터 상속받은 메소드를 자식 클래스에서 제정의 하는 것)
        # 상속이 없으면 오버라이드도 없으요 *.~ (vs overloading: 파라미터가 다른 경우, 그러면 같은 이름으로 메소드를 여러개 만들 수 있다 -> not under the concept of inheritance - 파이썬에는 없는 개념)
        # rect1: 사각형(가로 = 3, 세로 = 4, 시작점x = 1, 시작점y = 1)
        # 사각형(가로 = 3, 세로 = 4, 시작점x = 0, 시작점y = -1)

# 모든 클래스에는 오브젝트라는 조상이 있다
# 사실 class Shape(): 는 class Shape(object): 이다 -> 하지만 object 는 생략한다!

    def area(self):
        return self.w * self.h #override 해줌
        # 이 area 를 가지고 그림을 그린다


class Circle(Shape):
    # 새로운 클래스 써클은, sub class of a superclass Shape
    def __init__(self, r, x, y):
        print('Circle._init_호출')
        # when sub class has __init__, it has to invoke that of super class as well because or else the fields from the super class won't be initiated
        # super().__init__(x, y) # 이렇게 쓸 때는 self 를 안 쓰고, 아래처럼 쓸 때에는 self를 쓰지 않으면 안된다 (꼭 써야한다)
        Shape.__init__(self, x, y) #self 가 이전에는 회색처리가 되어서 쓰지 말아라 라고 되어있었는데, 여기서는 검정색으로 찐!!하게 보여줌 (써라..)
        # super().__init__(x, y) is the same as Shape.__init__(self, x, y)
        # sub class 만 갖는 field 를 초기화
        self.r = r # r for radius
        # no need to define arguments of super class again

    def __repr__(self):
        return f'동그라미(반지름 = {self.r}, x = {self.x}, y = {self.y})'

    def area(self):
        return 3.14159 * self.r ** 2
    # without the def area, occurs an error:  raise NotImplementedError('반드시 override 하세요 (Haz el override)')


if __name__ == '__main__':
        # The code above this is not a must, however, if we dont do it the returned values will appear in other Python files
        shape1 = Shape()  # since there are default values, even though there is no values given to Shape() function, it returns something
        print(shape1)
        # returns Shape(x = 0, y = 0)
        shape1.move(1, 2)
        print(shape1)

        # rect1 = Rectangle(3, 4)  # __init__ 도 안 만든 상태
        # 생성자의 이름은 class 이름과 같다 rect1 = Rectangle() 에서 에러가 났다
        # w,h 의 값을 주지 않아서
        # __init__ 을 만든 상태에서 -> 여기서 3,4 라는 값은 준다
        rect1 = Rectangle(w = 3, h = 4, x = 1, y = 1)
        print('rect1 타입:',type(rect1)) #__init__ 만들고 난 후에 여기까지는 잘 실행되다가 62번에서 에러가 났따

        # rect1 을 출력하는데 문자 타입으로 출력해야하니까 parent class 가 있는 __repr__로 올라갔다.
        # __rectagle__ 의 init 이 실행되었다는것은 찍혔는데, Shape 의 init 은 안 찍혔다
        # 이유는 child class 의 init 이 생기는 순간, 부모 크랠스의 init 은 자동으로 생성되지 않는다
        # 그래서 init 이 없었을 떄는 부모 클래스가 자동으로 생성되었는데, 이제는 아니라서,,, -> 그러면 부모 클래스의 x,y 가 만들어 지지 않는다
        # AttributeError: 'Rectangle' object has no attribute 'x'
        # 부모 클래스의 x가 refer to 할 때가 없는 것 (물려받지 못 했으니까) -> 부모클래스의 __init__ 이 호출되지 않았으니까

        print('rect1:',rect1)  # 3개의 줄이 더 출력 됐다 (__repr__ 의 parent 를 상속받아서 생성하지 않았지만 이미 만들어져있어요)
                      # 이런 것들이 코드의 재사용성을 높이는 것
                        # override 한 후에는 __repr__ 메소드가 변경되어 출력되요
        rect1.move(-1,-2) #i.e. move function -> 부모로 부터 물려받은 함수들 (부모에게서 상속받은 move메소드가 호출되요)
        print(rect1)

        circle1 = Circle(r = 10, x = 0, y = 0)
        print(circle1)
        print('circle1 type:',type(circle1))

        # 다중 상속 - 부모가 둘 이상인 것
        # 다중 상속을 받을 때에는 괄호 안에 class Circle(Shape, Drawingutil): 이런식으로 하면 Circle은 Shape, Drawingutil 에게서 상속 받는것
        # 그러면 super().__init__(x,y) 형식은 사용할 수 없다
        # so in multiple inheritance, we have to indicate as:
        # super().__init__(x, y)
        # Drawingutil().__init__(x,y)
        # 만약 두 부모에게 상속을 받을 때, 이름이 같은 메소드가 같은게 있다면 -> override 의 문제가 생긴다 (둘 중에 무엇을 남길 것인가?)
        # 다중상속의 양면성
        # 파이썬은 다중상속은 허용은 하지만 문제가 많다

        rect1.draw()
        # draw 는 Shape class 만 가지고 있다
        circle1.draw()
        # these functions before giving area functions to children class returns <drawing None...*-*!>
        # 각각의 자식 클래스 (rectangle & cirlce) override area()















