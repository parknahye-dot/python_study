 #1부터 10까지의 합을 구하세요.

for i in range(1, 11):
    print(i)
print("전체 합:", sum(range(1, 11)))


# 강사님 정답
total = 0

for i in range(1, 11):
    total += i
print(f"1부터 10까지의 합: {total}")

# 더 간단한 방법
total = sum(range(1, 11))
print(total)