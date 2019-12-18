# How to read the file
# open - read - close

f = open('test.txt', mode = 'r', encoding = 'utf-8')
#read: read(), readline()
# read 는 파라미터 없이 사용할 수 있다 ( = 가 있으면 default 가 있는 파라미터)
content = f.read(3) #안에 파라미터가 없는 경우에 문서 전체를 읽음
print(content)
# 마지막에 11번째 라인이 생김 (마지막 \n 에 넣었기 때문에 한 줄 더 생긴 것)

# open 한다 -> 파일을 읽을 수 있도록 file pointer 을 첫번 째 줄에 만들어 준다
# read() 파일 포인터의 위치가 한줄 한줄 바뀌며 읽어준다
# content = f.read()
# read() 한번 더 해주면 읽을 내용이 없다 (한번 다 읽고 마지막 줄에서부터 읽는건데, 그러면 읽을 내용이 없는 것)
# close 뜻은 닫아서 다른 사람이 새로 들어와서 다시 처음부터 읽을 수 있도록 하는 것

#content = f.read(1) #1
#content = f.read(2) #1번
#content = f.read(3) #1번째
# 숫자는 length, 넣어준 숫자 만큼 읽겠다
# read(n): n개의 문자만 읽음

#content = f.read(3) -a
#content = f.read(3) -b
# a와 b를 실행하면 아래와 같이 출력해준다 a에서 3 에서 끝나면 4부터 읽어준다
# 1번째
#  줄.
# 1번째 줄... 그러니까 a = 1번째 b= 줄. 이렇게 출력해주는 것
print(content)

#close
f.close()


# read.line: 한줄씩 출력
f = open('test2.txt',mode = 'r', encoding = 'utf-8')
line = f.readline() #(convert into string type)
print(line)
print(f'line: {line}, length: {len(line)}')
"""
 아래와 같이 출력된다. 왜 , 는 아래에 가 있을까? 눈에 보이지 않은 \n is at work! 
 we always put \n(줄바꿈) after sentences (Hello, Python!\n), so ',' went below 
line: Hello, Python!
, length: 15
then why is the length 15 not 14? because Python counts \n as 1 as well (len(sentence) = 14 + 1 (\n) = 15) 
공백 세줌! (count the spaces!) 
"""
# this is important because when importing csv files into Python,
# wrong count or converting \n to numbers is critical
# \n 없애는 걸 생각해줘야한다 # readline()  할 때, 뒤에 공백이 필요 없다고 한다면  strip() 써주기!
# so we add .strip()
line = f.readline()
print(f'line: {line}')
line = line.strip()
print(f'length: {len(line)}')

line = f.readline().strip()
print(f'line: {line}, length: {len(line)}')
# Python does not read the space anymore

# readline 은 한 줄 자체를 모두 읽어버린다
# 안에 있는 것 만큼 반복해주면 -> 전체 출력
line = f.readline()
print(line)
line = f.readline()
print(line)
# 왜 한칸씩 떨어져서 출력될까? # 줄 바꿈 때문에!
"""
    Hello, Python!
    
    점심 식사는 맛있게 하셨나요?
    
    0123456789
"""
f.close()

print('     \t  hello     python \t\n  '.strip())
# strip 시켜주면 앞뒤로 공백이 없다 ^0^!
# 중간에 들어가있는 공백을 없애주는 역할은 하지 않는다


# 파일을 한줄 한줄 읽어서 끝까지 읽고 싶다면
# 무한루프와 readline()을 사용해서 문서 끝까지 읽기
f = open('test2.txt', mode = 'r', encoding = 'utf-8')

while True: # infinite loop
    line = f.readline()
    if line == '': #파일의 끝(EOF: End of File) 에 도달했다
        # why is EOF a ''? because EOF will be an empty line
        break # ends the infinite loop
    print(line.strip())
"""
Hello, Python!
점심 식사는 맛있게 하셨나요?
0123456789
"""

f.close()

f = open('test.txt', mode = 'r', encoding = 'utf-8')
line = f.readline() # boolean type: if the line is not empty = TRUE
while line:
    # 라인이 빈 문자열이면 거짓, 그렇지 않으면 참
    print(line.strip())
    line = f.readline() # when line goes empty = FALSE (stops the loop)
    """
1번째 줄...
2번째 줄...
3번째 줄...
4번째 줄...
5번째 줄...
6번째 줄...
7번째 줄...
8번째 줄...
9번째 줄...
10번째 줄...
    """

f.close()

with open('test2.txt', mode = 'r', encoding = 'utf=8') as f:
     line = f.readline()
     while line:
         print(line.strip())
         line = f.readline()


