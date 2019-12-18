"""
for line in file:
    실행문
file에서 readline()을 호출한 결과를 line 변수에 저장
line이 빈 문자열('')이 아닐 때 실행문 실행
line이 빈 문자열이면 for 루프 종료
"""
with open('test.txt', mode = 'r', encoding = 'utf-8') as f:
    # mode can be skipped since it is positional argumention, but encoding must be indicated for it is a keyword argument
    for line in f:
        print(line.strip()) #.strip() is optional
    # no need to know the readline()!!!! just put them in for loop
    # dictionary type 일때는 (그런데 key 만 뽑아줌) -> 아니면 items 해주고 key 와 value 를 모두 뽑을 수 있다 (해보기)
    # f: 파일이 올 때는 readline 을 호출해준다?
    # 그러면 line 이 아니라 다른걸 줘도 같은 결과를 줄까? 그렇다
    # 어떻게 라인을 ,,?!


    # for ... in ... 구문은 그런 아이다
    # in 다음에 list 가 오면 원소들을 꺼내주고, dictionary 가 오면 key 값들을 그리고 파일이 오면 readline() 을 출력!

