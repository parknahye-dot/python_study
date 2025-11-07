def add(a, b):
    return a + b
    
result = add(3, 5)
print(result)  # 8

# 여러 값 반환
def get_stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg
    
total, avg = get_stats([1, 2, 3, 4, 5])
print(f"합계: {total}, 평균: {avg}")  # 합계: 15, 평균: 3.0