import matplotlib.pyplot as plt

# 선 그래프 (line chart)
x = [i for i in range(10)]
print(x)

y1 = [2 ** x for x in range(10)]
print(y1)
plt.plot(x, y1, 'm*-', label = 'example1')
# color 라는 키워드 없이 'r' 만 줘도 선이 빨간색, 'r:' 은 빨간색 점선으로 보여준다
# ctrl + q 해서 더 보자 :) !

y2 = [2**x for x in range (9, -1, -1)] #(start, end, range?) -> 9 부터 0 승까지 (index 의 하나 적게까지), -1씩 감소 (
print(y2)
plt.plot(x, y2, 'r--', label = 'example2') # 왜 별거 안했는데 둘이 같이 나오냐...

y3 = [x + y for x, y in zip(y1, y2)]
# zip 을 사용해서 리스트 두개를 묶어서 값을 꺼내올 수 있다
print(y3)
plt.plot(x, y3,'g:',label='example3')
# how to display colors on the plot 1) give the full name of the color: i.e. 'green' or
# 2) give RGB value hex strings ('#008000')
# 16진수 색상은 #RRGGBB와 같은 형태로 RR(적색), GG(녹색), BB(청색)을 진수로 나타내며, 0~FF사이의 값을 가지게 된다(대소문자 구분하지 않음).
# RGB or RGBA tuples ((0,1,0,1)) (Red,Green,Blue,A);  A is 불투명도 (opacity/transparency)

plt.legend(loc = 0) #the same as (loc = 'best')
plt.title('Line Chart Example')
plt.show()


















