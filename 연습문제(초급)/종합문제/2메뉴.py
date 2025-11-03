# 다음과 같은 메뉴 시스템을 만드세요:

menu = {
    "1": "회원가입",
    "2": "로그인",
    "3": "종료"
}

# 메뉴 출력
for key, value in menu.items():
    print(f"{key}. {value}")

# 사용자 선택 (여기서는 하드코딩)
choice = "2"

# 선택에 따른 메시지 출력
if choice == "1":
    print("회원가입을 선택했습니다.")
elif choice == "2":
    print("로그인을 선택했습니다.")
elif choice == "3":
    print("프로그램을 종료합니다.")
else:
    print("잘못된 선택입니다.")

# 다른 방법
menu = {
    "1": "회원가입",
    "2": "로그인",
    "3": "종료"
}

# 메뉴 출력
for key, value in menu.items():
    print(f"{key}. {value}")

choice = "2"

if choice == "1":
    print(menu["1"])
elif choice == "2":
    print(menu["2"])
elif choice == "3":
    print(menu["3"])
else:
    print("잘못된 선택입니다.")


