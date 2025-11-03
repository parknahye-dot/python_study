# 상품을 장바구니에 담고, 총 금액을 계산하는 프로그램을 만드세요.

products = {
    "사과": 1000,
    "바나나": 1500,
    "우유": 2000,
    "빵": 3000}
    
cart = []  # 장바구니

# 장바구니에 상품 추가
cart.append("사과")
cart.append("우유")
cart.append("빵")

# 총 금액 계산
total = sum(products[item] for item in cart)
print(f"총 금액: {total}원")

# 강사님 풀이
products = {
    "사과": 1000,
    "바나나": 1500,
    "우유": 2000,
    "빵": 3000
    }
    
cart = []
cart.append("사과")
cart.append("우유")
cart.append("빵")

# 총 금액 계산
total = 0 
for item in cart:
    total += products[item]
print(f"총 금액: {total}원")