"""
산점도 그래프 (scatter plot)
- 화면상에다 x,y 값을 점으로 표시하는 그래프
- to know the correlation of x and y
"""

import matplotlib.pyplot as plt

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67] # 친구 수
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190] # SNS에 머무는 시간
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends, minutes, c='r')
plt.title('Correlation between Time Spent on SNS and Number of Friends ')
plt.xlabel('# of Friends')
plt.ylabel('Average Time (Min)')
plt.annotate('a', xy = (70,175),
              xytext = (5, 5),
              textcoords = 'offset points') #plt.scatter() 다음에 온다
# 이 값을 주면 한 점에 (70,175의 값을 갖는) a 라고 레이벨이 새겨진다
# 위치 조정도 가능 -> la letra 'a' pegaba en el dot exactamente, por eso nos hemos mudado la letra xytext = (5, -5)
# +5 만큼 x-axis 로, -5 만큼 y-axis 로 그리고 'offset'
# xytext 를 기준으로 textcoords 방법으로 (x축에서 5만큼, y축에서 -5만큼 offset 방법으로)
# xytext = (5, 5) 이면 올라가서 보인다

# 세개의 리스트가 원소의 갯수가 같기 때문에 ( the same number of rows) 그래서 zip 으로 묶어서 iterate 해줄 수도 있다

for l,f,m in zip(labels, friends, minutes):
    plt.annotate(l, xy=(f, m),
                 xytext=(5, 5),
                 textcoords='offset points')
# 짱짱 신기방기 ^0^!!!

plt.show()


plt.title('Science vs Math')
plt.xlabel('Math')
plt.ylabel('Science')

math = [99,90,85,97,80]
science = [100,85,60,90,70]

plt.scatter(math, science)
# 대략 기울기가 보이고, 수학을 잘 하면 과학도 잘 하는 구나~ 정도라고 생각해줄 수 있다
# But the scale between Math and Science are different
# x = 80~100, y = 60~100 (x축과 y축의 스케일이 다르면 왜곡되어 보인다)
# 막대그래프, 산점도 등등 affected very much
# 왜곡되어 보이지 않게 하려면 pyplot 이 기본으로 가지고 있는 scaling 말고 다른 방법도 사용해보아야한다

plt.axis('equal')
# 대략 60~100으로 맞춰졌다
# 수학점수는 분산이 작고, 과학 점수는 분산이 크다는 것, 그리고 기울기가 굉장히 가파르다는 것을 알 수 있다
# 그냥 했을 때의 기울기는 완만했었다

plt.show()





























