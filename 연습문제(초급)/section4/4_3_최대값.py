# 세 개의 숫자 중 가장 큰 값을 반환하는 함수를 만드세요
# 기대 출력: 25

# 기본적인 방법
def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
        
print(find_max(10, 25, 15))

# 더 간단한 방법
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(10, 25, 15))
