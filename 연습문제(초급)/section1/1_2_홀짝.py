# 숫자를 입력받아 짝수인지 홀수인지 판별하세요.

number = int(input("숫자를 입력하세요: "))

is_even = (number % 2 == 0)
print(f"{number}는 {'짝수' if is_even else '홀수'}입니다")