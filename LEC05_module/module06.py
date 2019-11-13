"""
module06.py
"""

from numpy import random

print(random.randint(1,5))
# 이렇게 했을 때는 numpy. 이렇게 쓰면 안된다
# import 는 이름을 가져오는 것 (random 이라는 이름을 가져온 것 -> 그러면 random 부터 시작해서 더 작게 들어가야한다)


import numpy
print(numpy.random.randint(1,5))
# 이렇게 import 를 했을 때에는 numpy부터 해주는 것
# 여기서는 numpy 에서는 numpy라는 폴더 이름부터 가져온 것 그래서 폴더 이름부터 -> 더 작게 들어오는 것
# 어떤 이름을 가지고 왔느냐, import 했느냐가 중요하다



