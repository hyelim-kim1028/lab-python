"""
1) open the file
2) read/write the file
3) close the file
- 열려져 있는 파일을 닫지 않으면 다시 열 수 없다
- 파일을 열었으면 반드시 닫아줘야한다!!!!!! 꼭꼭!!!!!
"""

f = open('test.txt', 'w', encoding='utf-8')
# among all the parameters, file name is the must-give parameter (w/o default)
# we gave 'w' which stands for write mode
# mode (읽기 전용, 쓰기 가능 등)

# file에 텍스트를 씀
for i in range(1,11):
    f.write(f'{i}번째 줄...\n')
    # did not return anything
    # we could check it in a separate file
    # why am I encountering an error:
    # Fatal Python error: init_sys_streams: can't initialize sys standard streams
    # LookupError: unknown encoding: x - windows - 949
    # Current thread0x00001b10(most recent call first):
    # The error started when I changed the encoding type (it worked perfectly fine) and inserted \n to the line
    # weird
    # menu > file > setting > file encodings and turn it to UTF - 8

# close the file
f.close()
# so it's better to make into a habit that once you open a file, immediately write a code to close it

# how to delete a file: right click on the file > delete and click do refactor at the console below

# with 구문: 리소스를 사용한 후 close() 메소드를 자동으로 호출
# with ... as 변수:
#       실행문

with open('test2.txt', mode = 'w', encoding = 'utf-8') as f:
    f.write('Hello, Python!\n')
    f.write('점심 식사는 맛있게 하셨나요?\n')
    f.write('0123456789\n')

