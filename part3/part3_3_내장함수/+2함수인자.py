def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

# 방법 1: 하나씩 전달
result = add(numbers[0], numbers[1], numbers[2])

# 방법 2: 언패킹 (훨씬 간단!)
result = add(*numbers)  # add(1, 2, 3)과 동일
print(result)  # 6