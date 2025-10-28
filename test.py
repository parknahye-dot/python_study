age = int(input("나이: "))
is_student = input("학생인가요? (y/n): ").lower() == "y"

base_price = 1200
if age < 8:
    price = 0
elif age < 19:
    price = 720 if is_student else 1000
elif age >= 65:
    price = 500
else:
    price = base_price

print(f"요금: {price}원")