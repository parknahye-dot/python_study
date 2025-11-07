# 5단 출력 2~9까지 실습
dan = 5

print(f"=== {dan}단 ===")
for i in range(1, 10):
    result = dan * i
    print(f"{dan} x {i} = {result}")

# for문
for dan in range(2, 10):  # 2~9단
    print(f"\n=== {dan}단 ===")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

# while문
dan = 5
i = 1  # 반복 시작 값 설정

print(f"=== {dan}단 ===")
while i < 10:   # i가 10보다 작을 때까지 반복
    result = dan * i
    print(f"{dan} x {i} = {result}")
    i += 1      # i를 1씩 증가시키지 않으면 무한 반복됨 ⚠️
