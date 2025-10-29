# 1부터 10까지의 숫자를 리스트로 만들고, 다음을 출력하세요:
# - 첫 번째 요소
# - 마지막 요소
# - 처음 5개 요소

numbers = list(range(1, 11))

print(numbers[0])
print(numbers[-1])
print(numbers[:5])

# 강사님 풀이

numbers = list(range(1, 11))

print(f"첫 번째: {numbers[0]}")
print(f"마지막: {numbers[-1]}")
print(f"처음 5개: {numbers[:5]}")