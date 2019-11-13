"""
class 작성 및 테스트 연습
"""
from math import sqrt

class point:
    """
    2-dimension (x-y) 평면 상의 점 1개를 저장할 수 있는 클래스
    """
    def __init__(self,x,y): # 여기다 4개 선언하는건 그냥 에바 참치였다^0^
        self.x = x
        self.y = y
        # self.x2 = x2
        # self.y2 = y2
    def print_point(self):
        """
        포인트 객체가 가지고 있는 점의 좌표를 (x,y) 형식으로 출력하는 메소드
        :return: none
        """
        point1 = print(f'({self.x},{self.y})')
        #point2 = print(f'{self.x2},{self.y2}')
    def distance(self,other):
        """
        # my_first guess: give other as a list or a tuple
        두 점 사이의 거리를 계산해서 리턴하는 함수
        :param other: 다른 점/ point 객체 (other points)
        :return:
        """
        # np.sqrt((self.x2-self.x)**2 - (self.y2-self.y)**2)
        return sqrt((self.x - other.x)**2 + (self.x - other.x)**2)
            #sqrt was imported (from math import sqrt)

if __name__ == '__main__':
    pt1 = point(3,4)
    pt1.print_point()

    pt2 = point(2,3)
    pt2.print_point()

    print(pt1.distance(pt2))
        # pt1 becomes self and pt2 becomes an other(it was inserted as a part of an argument/a parameter)
