"""
module05.py
"""

# import utils
# # print(utils.)
# # print(utils.(shift + space) 하면 __all__ 에 있는 원소인 mymath1 만 보여주고, 여기에 있는 pi, add, subtract 를 사용할 수 있다
#
# import utils
#
# print(utils.mymath1.pi)
# print(utils.mymath2.multiply(11,12))
# # Error: AttributeError: module 'utils' has no attribute 'mymath1'

# Above: NONE

from utils import *
# from 패키지 import * 에서 임포트되는 모듈 이름들은 패키지 폴더의 __init__ .py파일의 __all__ 변수에 설정된 모듈 이름들임
print(mymath1.pi)
# print(mymath2.multiply(11,12))
# __all__ = [mymath1] 일 때는 mymath2.multiply(11,12) 는 안됨

import utils
print(utils.mymath2.multiply(11,22))
# 이렇게 하면 mymath2 가 파일에 아이콘이 붙어있는채로 보임
# mymath1 은 아이콘이 없음

# 어디서부터 놓친건지 모르겠다 ㅠㅠㅜㅜ
























