# 세 개의 숫자 중 가장 큰 수를 찾으세요.

a = 15
b = 27
c = 19

if a >= b and a >= c:
    max = a
elif b >= a and b >= c:
    max = b
else:
    max = c

print("가장 큰 수는:", max)