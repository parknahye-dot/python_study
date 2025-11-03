# 3명의 학생 정보를 딕셔너리로 관리하고, 각 학생의 이름을 출력하세요.

students = {
    "김철수": {"나이": 20, "점수": 85},
    "이영희": {"나이": 21, "점수": 92},
    "박민수": {"나이": 20, "점수": 78}
}

for student_name in students.keys():
    print(student_name)

# 정보까지 포함
# for name, info in students.items():
#     print(f"이름: {name}, 나이: {info['나이']}, 점수: {info['점수']}")