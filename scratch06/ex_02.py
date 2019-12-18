"""
사건의 종속성 vs 독립성 여부
- 사건 A의 발생 여부가 사건 B의 발생 여부에 대한 정보를 제공한다면 사건 A와 사건 B는 종속사건이다
- 사건 A의 발생 여부가 사건 B의 발생 여부와 상관이 없다면 사건 A와 사건 B는 독립 사건이다
- 사건(event) , 종속(dependent), 독립(independent)

동전 두개를 던지는 경우, A 사건 = 첫번째 동전이 앞면, B 사건 = 두번째 동전이 뒷면 -> A와 B는 독립 (independent)
c 사건 = 두 동전 모두 앞면 -> 처음 동전이 앞면이거나 뒷면인 경우가 두번째 동전의 결과에 영향을 미친다
-> A & C are dependent events, but A and B are independent events
P(A) & P(B) are independent, P(A) and P(C) are dependent variables
P(AnB) = occurence of A and B at the same time
P(AnB) = P(A,B)

P(A): possibilty of an occurence of event A
P(B): possibilty of an occurence of event B
P(A,B): occurence of A and B at the same time (교집합이 일어날 확률) (두 조건이 모두 일어날 경우)
      : P(A) * P(B) 이 성립하면, 두 사건은 독립사건
P(AuB):
"""

# Regardless of all genetics stuffs
# Having two babies:
# A: First child is a girl
# B: Second child is a boy
# C: both kids are boys(girls)

import random
child = ('boy', 'girl')
trials = 10_000
event_a = 0
event_b = 0
event_a_b = 0
event_c = 0
event_a_c = 0

for _ in range(trials):
    first = random.choice(child)
    second = random.choice(child)
    if first == 'girl':
        event_a += 1
    if second == 'boy':
        #elif 가 아니고 전부다 if (what does it mean? is he mean that he treated all the events as independent ones?)
        # ohhhh if it's in if-elif statement (once the first one is a girl, in if-elif statement, the second one won't be counted)
        # por eso, pusimos if - que puedamos contar todos de (kids-variable o list)
        event_b += 1
    if first == 'girl' and second == 'boy':
        # union of event A and event B
        event_a_b += 1
    if first == 'girl' and second == 'girl':
        event_c += 1
    if first == 'girl' and (first == 'girl' and second == 'girl'):
        # union of event A and event C #contamos una vez mas de event_c (종속 관계가 이렇게 보이는 것)
        event_a_c += 1
    # return event_a,event_b,event_c,event_a_b,event_a_c -> we can make the codes into a function easily:
    # drag all the lines to be included in the function > click refactor > click method > name the function YA!

    p_a = event_a/trials
    p_b = event_b/trials
    p_a_b = event_a_b/trials
    p_c = event_c/trials
    p_a_c = event_a_c/trials

    print(f'P(A,B) = {p_a_b}, P(A)P(B) = {p_a * p_b}')
    print(f'p(A,C) = {p_a_c}, P(A)P(C) = {p_a * p_c}')
# lo podemos hacer en el metodo mismo que hicimos el coin (la moneda)

# si hacemos la funcion de las lineas arriba:
# DESDE for _ in range(trials): ... A  ... event_a_c += 1




