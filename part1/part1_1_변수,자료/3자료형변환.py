# ✅ 자료형 확인 및 변환
# 자료형 확인
print(type(25))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hi"))      # <class 'str'>

# 자료형 변환
x = "100"
y = int(x)             # 문자열 → 정수
z = float(y)           # 정수 → 실수
s = str(z)             # 실수 → 문자열

print(y, type(y))      # 100 <class 'int'>