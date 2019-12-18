"""
Gradient Descent (경사 하강법)
데이터 고학을 하다보면 최적화 문제들을 만나게 됨.
최적화 문제 - 특정 상황에서 가장 적합한 모델을 찾는 문제
(예) 모델의 오류(error)을 "최소화", likelihood(우도)를 최대화
타겟 함수를 최소 혹은 최대로 만들어 주는 파라미터를 찾는 문제

곡선의 접선을 찾고, 접선의 기울기 방향으로 점을 이동시켜 나가면서 최소(최댓)값을 찾음
"""

import matplotlib.pyplot as plt

def f(x):
    """y = x**2 """
    return x**2

def f_derivative(x):
    """y = x**2의 도함수(미분): y = 2x"""
    return 2 * x

def tangent(x, a, x1, y1):
    """기울기가 a이고, 점 (x1, y1)을 지나는 직선의 방정식
        y - y1 = a(x -x1) """
    return a * (x - x1) + y1

def difference_quotient(f, x, h):
    """함수 f의 도함수의 근사값"""
    return (f(x + h) - f(x))/h