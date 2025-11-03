# 학생들의 점수를 입력받아 다음을 출력하는 프로그램을 만드세요:
# - 총점
# - 평균
# - 최고점
# - 최저점
# - 평균 이상인 학생 수

students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "정지원": 88,
    "최동욱": 95}

scores = list(students.values())
total_score = sum(scores)
average_score = total_score / len(students)
max_score = max(scores)
min_score = min(scores)
above_average_count = sum(1 for score in scores if score > average_score)

print(f"총점: {total_score}")
print(f"평균: {average_score:.2f}")
print(f"최고점: {max_score}")
print(f"최저점: {min_score}")
print(f"평균 이상인 학생 수: {above_average_count}")

# 강사님 풀이
students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "정지원": 88,
    "최동욱": 95}
    
# 총점
total = sum(students.values())
print(f"총점: {total}")

# 평균
average = total / len(students)
print(f"평균: {average:.1f}")

# 최고점
max_score = max(students.values())
print(f"최고점: {max_score}")

# 최저점
min_score = min(students.values())
print(f"최저점: {min_score}")

# 평균 이상인 학생 수
count = 0 
for score in students.values():
    if score >= average:
        count += 1
print(f"평균 이상인 학생 수: {count}명")