# 리스트에서 짝수만 골라내는 함수를 만드세요.

# 반복문 사용
def get_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 리스트 컴프리헨션 사용
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))