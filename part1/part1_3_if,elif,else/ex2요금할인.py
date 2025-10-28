age = 15
is_student = True
is_weekend = False

# 기본 요금
base_price = 10000

# 나이별 할인
if age < 13:
    discount = 0.5  # 50% 할인
elif age < 19:
    discount = 0.3  # 30% 할인
elif age >= 65:
    discount = 0.4  # 40% 할인
else:
    discount = 0    # 할인 없음
    
# 학생 추가 할인
if is_student and 13 <= age < 19:
    discount += 0.1  # 10% 추가 할인

# 주말 할증
if is_weekend:
    base_price = base_price * 1.2
    
# 최종 요금
final_price = base_price * (1 - discount)
    
print(f"나이: {age}세")
print(f"학생 여부: {is_student}")
print(f"주말 여부: {is_weekend}")
print(f"할인율: {discount * 100}%")
print(f"최종 요금: {final_price:,.0f}원")