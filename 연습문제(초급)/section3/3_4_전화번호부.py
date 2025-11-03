# 이름을 입력하면 전화번호를 출력하는 프로그램을 만드세요.

phonebook = {
    "엄마": "010-1234-5678",
    "아빠": "010-2345-6789",
    "친구": "010-3456-7890"}
    
name = "엄마"

if name in phonebook:
    print(f"{name}의 전화번호는 {phonebook[name]}입니다.")