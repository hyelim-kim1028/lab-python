"""
utils.__init__
- 패키지에 대한 설명과 설정을 담당하는 파일
- 다른 모듈에서 패키지이름을 import했을 때 공개할 모듈이름들을 설정할 수 있다
  (i.e. utils. 했을 때 mymath1,2 가 안나왔던 것 처럼 -> 이걸 나오게 설정할 수 있다)
"""
# from 패키지 import * 구문에서 공개할 모듈 이름들의 리스트
__all__ = ['mymath1']

# import 패키지 구문에서 공개할 모듈 이름들의 리스트
from . import mymath2
# init.py 가 mymath2를  import 하는 것 -> 그러면 module05 에서
# . -> current file
# 실행하지 않아도 다른데서 부르면 자동으로 실행이 된다 (다른 모듈에 의해서) 그래서 얘를 직접 실행시키려고하면 안된다?

