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

# 강사님 풀이

a = 15
b = 27
c = 19

if a > b and a > c:
    print(f"가장 큰 수: {a}")
elif b > c:
    print(f"가장 큰 수: {b}")
else:
    print(f"가장 큰 수: {c}")
    
# 더 간단한 방법
print(f"가장 큰 수: {max(a, b, c)}")