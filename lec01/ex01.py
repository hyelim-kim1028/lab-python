# November 04, 2019
# package is just a folder where we save what we have made
print('hell,python!')
# ctrl + shift + F10 : 실행
# Python Interpreter: 기계어로 변환해서 실행을 시켜주는 것 > 만약 이게 실행이 안될 경우:
# Files > settings > project interpreter > 여기서 라이브러리 설치된 파일 찾아서 wd 설정
# 덧) 여기서 + 클릭해서 원하는 패키지 다운 가능 + 버전번호 선택 가능 > 최신이 늘 좋은 것이 아니다

# terminal : 도스명령창/ 도스 prompt (not often used)
# Python Console : Jupyter notebook 과 비슷한 명령창 (a.k.a. ipython console)
# 문장을 실행 할 때마다 숫자가 늘어난다 In[1], In[2], In[3], ... etc

"""
이게 주석인가 주석이 된건가 
"""
#이건 주석이 맞는데 위에꺼가 주석이 아닌지 모르겠다

# Python 문장은 문장을 끝낼 때 ; (semi-colon)을 사용하지 않는다, 그냥 한문장 한문장 논리적으로 바로바로 실행
# 들여쓰기 (indentation?) 이 매우 중요

# 프로그램 변수 선언/사용
# 변수: 프로그램에 필요한 데이터를 저장하는 공간이다
# 파이썬에서는 반드시 등호만 사용한다 -> 변수 이름 = 값
# 숫자를 저장하고 싶다면
age = 16
print('I am',age)
print(16)

# 문자열/이름을 저장하고 싶다면 변수이름을 만들어서
# 파이썬은 문자열을 사용할 때 큰 따옴표(""), 작은 따옴표('') 둘 다 사용가능 (Need to be coherent with the symbols)
name = '오쌤'
print(name)

company = "ITWILL"
print(company)

# normally, we use '' than ""
# In case of there is ''/"" in a sentence, it's better use the other option
str1 = 'He said "Yes!"'
print(str1)

# This is not possible : "He said "YES""; For Python, this is the same as "He said" YES "" > weird
str2 = "I'm a boy."

# But this is not possible: 'I'm a boy'; For Python, this is the same as 'I' m a boy ' > weird
# Pero si esta frase es una mezcla de '' / "", en estos casos tenemos que usar \' o \"
str3 = 'I\'m a girl.'
print(str3)
# This way Python would understand that ' beside m is not to indicate the end of the sentence, rather it is just a part of a sentence







