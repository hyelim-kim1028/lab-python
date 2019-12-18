"""
gradient descent 연습
"""


def g(x):
    """ y = (1/3)x**3 - x """
    return x**3 / 3 - x

def difference_quotient(f, x, h):
    """ 함수 f의 도함수의 근사값 """
    return (f(x + h) - f(x)) / h

def move(x, direction, step = -0.1):
    """x 좌표를 새로운 x로 이동.
        direction: 접선의 기울기
       step > 0 인 경우는 접선과 같은 방향으로 이동 -> 최솟값 찾기
       step < 0 인 경우는 접선과 반대 방향으로 이동 -> 최댓값 찾기 """
    return x + step * direction


if __name__ == '__main__':

    random.seed(1128)
    init_x = random.randint(-10, 10)  # 시작 값
    print(f'init_x = {init_x}')
    tolerance = 0.0000001
    # 두 x좌표 사이의 거리가 tolerance 이하이면 반복문 종료
    count = 0
    while True:  # 반복
        count += 1
        # x좌표에서의 접선의 기울기를 계산
        gradient = difference_quotient(f, init_x, h=0.001)
        # 찾은 기울기를 사용해서 x좌표를 이동
        next_x = move(init_x, gradient, step=-0.1)
        print(f'{count}: x = {next_x}')
        if abs(next_x - init_x) < tolerance:
            # 이동 전과 후의 x값의 차이가 tolerance 미만이면 반복문 종료
            break
        else:
            # 이동한 점이 다음 반복에서는 시작점이 되어야 함!
            init_x = next_x