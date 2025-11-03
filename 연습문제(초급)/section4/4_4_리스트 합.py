# 숫자 리스트를 입력받아 합을 반환하는 함수를 만드세요.
# 기대 출력: 15

# 기본적인 방법
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
    
print(calculate_sum([1, 2, 3, 4, 5]))

# 더 간단한 방법
def calculate_sum(numbers):
    return sum(numbers)

print(calculate_sum([1, 2, 3, 4, 5]))