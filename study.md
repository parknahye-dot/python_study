# 10/28 수업 내용 요약 (1_1~2_2)

---

## part1_1_변수와 자료 (Variable & Data Types)

| 구분 | 문법/키워드 | 관련 예시 | 설명 |
|------|--------------|------------|------|
| **변수 선언** | `x = 10`, `name = "홍길동"` |  | 데이터 저장 |
| **자료형** | `int`, `float`, `str`, `bool`, `None` | `25`, `3.14`, `"hi"`, `True`, `None` | 기본 타입 |
| **자료형 확인** | `type()` | `type(3.14)` | 자료형 출력 |
| **자료형 변환** | `int()`, `float()`, `str()`, `bool()` | `int("100")`, `float(3)`, `str(3.14)` | 형변환 |
| **입출력** | `input()`, `print()` | `int(input())`, `print("Hello")` | 콘솔 입출력 |
| **출력 포맷팅** | `f-string`, `"{}"`, `%d` | `print(f"이름:{name}, 나이:{age}")` | 문자열 포맷 |
| **주석** | `#` | `# 설명문` | 실행 제외 |
| **예외 처리** | `try:`, `except ValueError:` | `try: int(x) except ValueError:` | 오류 방지 |
| **실전 키워드** | `birth_year`, `current_year`, `age`, `celsius`, `fahrenheit`, `try`, `except`, `float()`, `int()`, `ValueError`, `정수부`, `소수부`, `type()` | 나이 계산, 온도 변환, 예외 처리 |

---

## part1_2_연산 (Operators)

| 구분 | 문법/키워드 | 관련 예시 | 설명 |
|------|--------------|------------|------|
| **산술 연산자** | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `a+b`, `a//b`, `a%b`, `a**b` | 사칙연산, 몫, 나머지, 거듭제곱 |
| **비교 연산자** | `==`, `!=`, `>`, `<`, `>=`, `<=` | `x == y`, `x != y` | 참/거짓 비교 |
| **논리 연산자** | `and`, `or`, `not` | `(a>0 and b>0)` | 조건 결합 |
| **복합 대입 연산자** | `+=`, `-=`, `*=`, `/=` | `x += 5` | 자기 자신에 연산 |
| **단항 연산자** | `+`, `-` | `-x`, `+y` | 부호 변경 |
| **우선순위** | `()`, `**`, `*, /`, `+, -` | `2 + 3 * 4 = 14` | 괄호 우선 |
| **실전 키워드** | `price`, `quantity`, `total`, `payment`, `change`, `is_even`, `is_multiple_of_3`, `is_multiple_of_4`, `is_both`, `principal`, `rate`, `years`, `final_amount`, `interest`, `doubling_time` | 가격 계산, 배수 판별, 복리 계산 |

---

## part1_3_if_elif_else (조건문)

| 구분 | 문법/키워드 | 관련 예시 | 설명 |
|------|--------------|------------|------|
| **조건문 기본형** | `if`, `elif`, `else` | `if score >= 90:` | 조건 분기 |
| **중첩 조건문** | `if 안에 if` | `if age >= 18:` `if has_ticket:` | 이중 조건 |
| **조건 표현식** | `"A" if 조건 else "B"` | `"성인" if age>=18 else "미성년자"` | 한 줄 조건 |
| **비교 예시 변수** | `score`, `age`, `is_student`, `is_weekend`, `base_price`, `discount`, `final_price`, `is_leap`, `reason`, `february_days` | 학점, 요금, 윤년 계산 |
| **조건 논리 키워드** | `and`, `or`, `not`, `%`, `==`, `!=`, `<`, `>=` |  | 논리 조합 |
| **예외 처리와 결합** | `try: ... except:` | `try: num=int(input()) except:` | 안전 입력 |
| **pass문** | `if 조건: pass` | `if temp>30: pass` | 빈 블록 유지용 |

---

## part1_4_반복문 (Loops)

| 구분 | 문법/키워드 | 관련 예시 | 설명 |
|------|--------------|------------|------|
| **for문** | `for i in range(n):` | `range(5)` | 횟수 반복 |
| **while문** | `while 조건:` | `while count < 5:` | 조건 반복 |
| **break / continue** | `break`, `continue` |  | 반복 제어 |
| **range() 응용** | `range(시작,끝,간격)` | `for i in range(2,10,2):` | 범위 설정 |
| **enumerate()** | `for i,v in enumerate(list):` |  | 인덱스+값 반복 |
| **else문과 반복** | `for i in range(3): ... else:` |  | 정상 종료 시 실행 |
| **실전 키워드** | `dan`, `result`, `number`, `is_prime`, `fib`, `n`, `next_num`, `golden_ratio`, `math`, `sqrt` | 구구단, 소수, 피보나치, 황금비 |

---

## part2_1_리스트 (List)

| 구분 | 문법/키워드 | 관련 예시 | 설명 |
|------|--------------|------------|------|
| **리스트 생성** | `[ ]` | `numbers = [1,2,3]`, `mixed = [1,"hi",3.14]` | 여러 값 저장 |
| **인덱싱/슬라이싱** | `[0]`, `[-1]`, `[1:4]`, `[::2]`, `[::-1]` |  | 데이터 접근 |
| **메서드** | `.append()`, `.insert()`, `.remove()`, `.pop()`, `.extend()`, `.sort()`, `.reverse()`, `len()`, `in`, `.clear()` |  | 추가, 삭제, 포함 |
| **리스트 컴프리헨션** | `[표현식 for 변수 in 반복 if 조건]` | `[i**2 for i in range(10)]` | 간결한 생성 |
| **내장함수 활용** | `sum()`, `max()`, `min()` | `avg = sum(scores)/len(scores)` | 통계 계산 |
| **슬라이싱 문법 요약** | `[start:end:step]` | `data[::2]`, `data[::-1]` | 구간·간격 지정 가능 |
| **리스트 결합/복제** | `+`, `*` | `a+b`, `nums*2` | 병합/반복 |
| **리스트 특징** | 순서 있음 / 수정 가능 / 중복 가능 / 인덱스로 접근 |  | 가장 기본적인 시퀀스 자료형 |
| **실전 키워드** | `scores`, `total`, `average`, `numbers`, `evens`, `squares`, `filtered_squares`, `transformed`, `prices`, `window`, `moving_avg`, `moving_avg_short`, `trends` | 점수 관리, 필터링, 이동평균, 추세 분석 |
| **핵심 문법 요약** | `[]`, `.append()`, `.remove()`, `.insert()`, `.sort()`, `.reverse()`, `.extend()`, 슬라이싱 `[::]`, `len()`, `in`, 리스트 컴프리헨션 | 리스트 조작 핵심 문법 |

---

## part2_2_튜플 (Tuple)

| 구분 | 문법/키워드 | 관련 예시 | 설명 |
|------|--------------|------------|------|
| **튜플 생성** | `( )` | `t = (1,2,3)`, `point = (10,20)` | 수정 불가 자료형 |
| **접근** | `t[0]`, `t[1]` |  | 인덱스 접근 |
| **언패킹** | `x, y = point` |  | 변수 분리 |
| **불변성** | `point[0] = 30 ❌` |  | 수정 불가 |
| **함수 반환 예시** | `return (name, age, grade, score)` | `get_student_info()` | 다중 반환 |
| **좌표 계산** | `(x**2 + y**2)**0.5`, `math.atan2(y,x)` |  | 거리, 각도 계산 |
| **형 변환** | `list(t)`, `tuple(list)` |  | 리스트 ↔ 튜플 변환 |
| **튜플 특징** | 순서 있음 / 수정 불가 / 중복 가능 / 인덱스로 접근 |  | 리스트보다 메모리 효율적 |
| **수학 관련 함수** | `math.sqrt()`, `math.atan2()`, `math.degrees()` |  | 거리·각도 계산에 활용 |
| **실전 키워드** | `points`, `transformed`, `polar_coords`, `r`, `theta`, `math`, `sqrt`, `atan2`, `degrees` | 좌표 변환, 극좌표 변환 |
| **핵심 문법 요약** | `()`, 언패킹, 불변(immutable), `tuple()`, `math`, `sqrt`, `atan2`, `degrees` | 수정 불가한 고정 데이터 |

---

# 10/29 수업 내용 요약 (2_3,2_4,3_3)

## part2_3_딕셔너리 (Dictionary)

| 구분 | 문법/키워드 | 관련 예시 | 설명 |
|------|--------------|------------|------|
| **기본 구조** | `{키:값}` | `{"name":"홍길동","age":20}` | key-value 쌍 저장 |
| **생성** | `student = {"name":"홍길동","age":20}` |  | 선언 시 중괄호 사용 |
| **접근** | `student["name"]`, `student.get("age")` |  | 키로 값 접근 |
| **안전 접근** | `.get("key","기본값")` | `student.get("email","없음")` | 키 없을 때 기본값 반환 |
| **수정/추가** | `dict["key"]=값` | `person["city"]="Seoul"` | 존재 시 수정, 없으면 추가 |
| **삭제** | `del dict["key"]`, `.pop("key")` | `del person["city"]` | 키 삭제 |
| **조회** | `.keys()`, `.values()`, `.items()` | `for k,v in dict.items():` | 전체 순회 |
| **중첩 구조** | `{"이름":{"math":90,"eng":80}}` |  | 딕셔너리 안 딕셔너리 |
| **빈도수 계산** | `if key in dict:` / `dict[key]+=1` | `word_count[word] = word_count.get(word,0)+1` | 단어 수 세기 |
| **max 함수 응용** | `max(dict,key=dict.get)` | `max_word = max(word_count,key=word_count.get)` | 최댓값 찾기 |
| **람다 활용** | `max(dict.items(), key=lambda x:x[1])` |  | 특정 값 기준 정렬 |
| **딕셔너리 특징** | 순서 유지 / 키 중복 불가 / 값 중복 가능 / 수정 가능 |  | key-value 구조 |
| **실전 키워드** | `contacts`, `word_count`, `students`, `subjects`, `avg`, `best_student`, `grades`, `scores` | 전화번호부, 빈도수, 성적 관리 |
| **핵심 문법 요약** | `.get()`, `.items()`, `.values()`, `.keys()`, `.pop()`, `max(dict,key=...)`, `lambda`, `in`, `del`, 중첩 딕셔너리 | 딕셔너리 조작 핵심 도구 |

---

## part2_4_세트 (Set)

| 구분 | 문법/키워드 | 관련 예시 | 설명 |
|------|--------------|------------|------|
| **기본 구조** | `{}` | `{1,2,3}` | 순서 없음, 중복 제거 |
| **생성** | `set()`, `{1,2,3}` | `numbers = {1,2,3,3}` | 중복 자동 제거 |
| **리스트 변환** | `list(set(list))` | `unique = list(set(data))` | 중복 제거용 |
| **형 변환** | `set(list)` / `list(set)` | `unique = list(set([1,1,2,3]))` | 리스트 ↔ 세트 변환 |
| **집합 연산** | `|`, `&`, `-`, `^` | `a|b`, `a&b`, `a-b`, `a^b` | 합집합, 교집합, 차집합, 대칭차집합 |
| **in 연산자** | `x in s` / `x not in s` | `if "apple" in fruits:` | 포함 여부 검사 |
| **비교/유사도** | `len(a&b)/len(a|b)` | `similarity = len(common)/len(all)` | 자카드 유사도 |
| **정렬 필요 시** | `sorted(set)` | `sorted({3,1,2}) → [1,2,3]` | 순서가 없으므로 정렬로 접근 |
| **세트 특징** | 순서 없음 / 수정 가능 / 중복 불가 / 인덱스 접근 불가 |  | 수학적 집합 구조 |
| **실전 키워드** | `attendance`, `unique_students`, `person_a`, `person_b`, `common`, `only_a`, `only_b`, `all_interests`, `jaccard`, `words1`, `words2`, `common_words` | 중복 제거, 관심사 비교, 문서 유사도 |
| **핵심 문법 요약** | `set()`, `{}`, `|`, `&`, `-`, `^`, `in`, `list(set())`, `len()`, `sorted()`, 자카드 유사도 | 중복 제거 및 집합 연산 핵심 문법 |

---

## part3_3_유용한 내장 함수 (map / filter / zip / enumerate)

| 함수 | 문법/키워드 | 관련 예시 | 설명 |
|------|--------------|------------|------|
| **map()** | `map(함수, iterable)` | `map(int, ["1","2","3"])` | 모든 요소에 함수 적용 |
| **lambda** | `lambda x: x+1` | `map(lambda x:x**2, numbers)` | 한 줄짜리 익명 함수 |
| **filter()** | `filter(조건함수, iterable)` | `filter(lambda x:x%2==0, numbers)` | 조건 만족만 남김 |
| **zip()** | `zip(list1,list2,...)` | `for n,s in zip(names,scores):` | 여러 리스트 묶기 |
| **enumerate()** | `enumerate(iterable,start=1)` | `for i,v in enumerate(list,1):` | 인덱스+값 반복 |
| **dict(zip())** | `dict(zip(keys,values))` | `student_dict = dict(zip(names,scores))` | zip으로 딕셔너리 생성 |
| **sum / max / min** | `sum(list)`, `max(list)`, `min(list)` | `max(scores)` | 합계 및 최대/최소 |
| **언패킹 연산자** | `*` | `for subject,*scores in zip(subjects,*students)` | zip 결과 분해 |
| **any / all** | `any()`, `all()` | `any(x>0 for x in nums)` | 하나라도 / 전부 참인지 검사 |
| **sorted() / reversed()** | `sorted()`, `reversed()` | `sorted(nums)`, `reversed(nums)` | 정렬, 역순 변환 |
| **실전 키워드** | `lambda`, `map`, `filter`, `zip`, `enumerate`, `sum`, `max`, `min`, `list()`, `dict()`, `any`, `all`, `sorted
