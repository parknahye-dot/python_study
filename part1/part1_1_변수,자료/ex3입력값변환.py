# 고급 예제: 입력값 검증 및 변환
# 사용자 입력을 받아 안전하게 숫자로 변환
user_input = "123.45689"

try:
    number = float(user_input)
    print(f"변환 성공: {number}")
    print(f"타입: {type(number)}")

    # 정수부와 소수부 분리
    integer_part = int(number)
    decimal_part = number - integer_part
    print(f"정수부: {integer_part}, 소수부: {decimal_part:.2f}")
except ValueError:
    print("숫자가 아닙니다!")