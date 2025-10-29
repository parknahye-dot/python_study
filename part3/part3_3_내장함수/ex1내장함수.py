# 여러 리스트 조합
names = ["김철수", "이영희", "박민수"]
math = [85, 92, 78]
english = [90, 88, 85]

# zip으로 묶어서 출력
print("=== 학생 성적 ===")
for i, (name, m, e) in enumerate(zip(names, math, english), 1):
    total = m + e
    print(f"{i}. {name}: 수학 {m}, 영어 {e}, 합계 {total}")