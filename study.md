# 10/28~11/3 - 파이썬 기초 요약

# 📘 Part 1 — 기본 문법

---

## 🧩 1.1 변수와 자료형

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **name, age, height, is_student** | 변수 | `name = "홍길동"` | 변수는 데이터를 저장하는 이름 |
| **int** | 자료형 | `age = 25` | 정수형 데이터 |
| **float** | 자료형 | `height = 175.5` | 실수형 데이터 |
| **str** | 자료형 | `"Hello"` | 문자열 데이터 |
| **bool** | 자료형 | `is_active = True` | 참(True)/거짓(False) 표현 |
| **type()** | 내장 함수 | `type(3.14)` | 값의 자료형을 확인 |
| **int(), float(), str()** | 형 변환 함수 | `int("100")` | 데이터 형식을 변환 |
| **try / except** | 예외 처리 구문 | `try: ... except ValueError:` | 오류를 감지하고 처리 |
| **ValueError** | 예외 클래스 | `except ValueError:` | 변환 실패 시 발생하는 오류 |
| **print()** | 내장 함수 | `print(f"나이: {age}")` | 콘솔 출력 |
| **f-string** | 문자열 포맷 | `f"{name}님 안녕하세요"` | 문자열에 변수 삽입 |
| **float 연산** | 연산식 | `3.14 * 2` | 소수점 포함 계산 |
| **산술 변환 예제** | 계산 | `9/5 + 32` | 섭씨 ↔ 화씨 변환 |
| **예외 처리 후속 코드** | 문법 | `print("숫자가 아닙니다!")` | 오류 시 실행되는 구문 |
| **자료형 관련 키워드** | 참고 | `int, float, str, bool, type, try, except` | 변수/형 변환에 관련된 핵심 개념 |

---

## 🧩 1.2 연산자

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **+ - * /** | 산술 연산자 | `a + b`, `a / b` | 사칙연산 |
| **//** | 산술 연산자 | `a // b` | 나눗셈의 몫 반환 |
| **%** | 산술 연산자 | `a % b` | 나머지 반환 |
| **\*\*** | 산술 연산자 | `a ** b` | 거듭제곱 |
| **==, !=, >, <, >=, <=** | 비교 연산자 | `x == y`, `x < y` | 두 값 비교 |
| **and, or, not** | 논리 연산자 | `(a and b)`, `(not a)` | 조건 논리 연결 |
| **조건 결합** | 논리식 | `(age >= 18) and has_license` | 여러 조건을 동시에 검사 |
| **변수: a, b, x, y, age, has_license** | 변수 | `age = 20` | 연산에 사용되는 예시 변수 |
| **할당(=)** | 연산자 | `price = 15000` | 변수에 값 저장 |
| **복리 계산 공식** | 수학식 | `P(1 + r)**t` | 복리 계산 수식 |
| **principal, rate, years** | 변수 | `principal = 1000000` | 복리 계산에서 사용 |
| **형식 지정자** | 포매팅 | `f"{value:,.0f}"` | 천 단위, 소수점 포맷 지정 |
| **72의 법칙** | 수학 개념 | `72 / (rate*100)` | 자산이 2배가 되는 기간 계산 |
| **연산자 관련 키워드** | 참고 | `+, -, *, /, //, %, **, ==, !=, >=, <=, and, or, not` | 연산 및 비교 관련 핵심 문법 |

---

## 🧩 1.3 조건문 (if / elif / else)

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **if / elif / else** | 제어문 | `if score >= 90:` | 조건에 따라 분기 실행 |
| **중첩 조건문** | 문법 | `if age >= 18: if has_ticket:` | 조건 안의 조건 |
| **삼항 연산자** | 표현식 | `"성인" if age >= 18 else "미성년자"` | 한 줄 조건문 |
| **비교 연산자** | 연산자 | `>=`, `==`, `<` | 조건 비교에 사용 |
| **논리 연산자** | 연산자 | `and`, `or` | 여러 조건을 결합 |
| **변수: score, age, has_ticket, is_student, is_weekend** | 변수 | `age = 20` | 조건 판단에 사용되는 값 |
| **할인 계산 로직** | 제어 구조 | `if age < 13: discount = 0.5` | 분기별 요금 할인 |
| **reason / is_leap** | 변수 | `reason = "4로 나누어떨어짐"` | 윤년 여부 설명 |
| **윤년 판별 조건** | 논리식 | `year % 400 == 0` | 윤년 판단 기준 |
| **formatting (f-string)** | 문자열 포맷 | `f"{year}년은 윤년입니다"` | 조건 결과 출력 |
| **Value Selection (선택 표현)** | 문법 | `label = 1 if score > 0.5 else 0` | 조건에 따른 값 할당 |
| **조건문 관련 키워드** | 참고 | `if, elif, else, 중첩 if, 삼항 연산자, and, or, not` | 조건 제어의 핵심 구문 |

---

## 🧩 1.4 반복문

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **for문** | 반복문 | `for i in range(5):` | 일정 횟수 반복 실행 |
| **range()** | 내장 함수 | `range(1, 10, 2)` | 숫자 범위 생성 |
| **리스트 순회** | 반복문 | `for fruit in fruits:` | 리스트 요소 반복 |
| **enumerate()** | 내장 함수 | `for idx, fruit in enumerate(fruits):` | 인덱스+값 동시 사용 |
| **while문** | 반복문 | `while count < 5:` | 조건이 참인 동안 반복 |
| **break** | 제어문 | `if i == 5: break` | 반복문 종료 |
| **continue** | 제어문 | `if i == 2: continue` | 다음 반복으로 건너뜀 |
| **range(시작,끝,간격)** | 문법 | `range(1,10,2)` | 숫자 간격 설정 |
| **리스트 인덱스** | 문법 | `fib[-1]`, `fib[-2]` | 리스트 끝 요소 접근 |
| **fib / next_num / n** | 변수 | `fib = [0, 1]` | 피보나치 계산 변수 |
| **append()** | 리스트 메서드 | `fib.append(next_num)` | 리스트 끝에 값 추가 |
| **소수 판별 로직** | 제어 구조 | `if number % i == 0:` | 약수 여부 검사 |
| **break 활용** | 제어문 | `break` | 조건 충족 시 반복 종료 |
| **황금비 계산** | 수학식 | `fib[-1] / fib[-2]` | 연속된 항의 비율 계산 |
| **math.pow() 대체식** | 연산 | `(1 + 5**0.5)/2` | 제곱근을 이용한 수학 상수 |
| **반복문 관련 키워드** | 참고 | `for, while, break, continue, range, enumerate` | 반복 제어의 핵심 구문 |
| **예제 변수들** | 참고 | `age, score, number, year, fib, next_num, rate, has_ticket` | 예제 코드에서 자주 쓰이는 변수들 |

---

# 📘 Part 2 — 자료구조

---

## 🧩 2.1 리스트 (List)

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **numbers, mixed, empty** | 변수 | `[1, 2, 3]`, `[]` | 리스트 생성 예시 |
| **인덱싱** | 문법 | `numbers[0]`, `numbers[-1]` | 요소 접근 (0부터 시작) |
| **슬라이싱** | 문법 | `data[2:5]`, `data[::-1]` | 부분 추출, 역순 가능 |
| **append()** | 리스트 메서드 | `fruits.append("포도")` | 리스트 끝에 추가 |
| **insert()** | 리스트 메서드 | `fruits.insert(1, "딸기")` | 특정 위치에 추가 |
| **extend()** | 리스트 메서드 | `fruits.extend(["수박", "참외"])` | 여러 요소 추가 |
| **remove()** | 리스트 메서드 | `fruits.remove("바나나")` | 값으로 삭제 |
| **pop()** | 리스트 메서드 | `popped = fruits.pop()` | 마지막 요소 삭제 후 반환 |
| **del** | 키워드 | `del fruits[0]` | 인덱스로 삭제 |
| **len()** | 내장 함수 | `len(fruits)` | 리스트 길이 반환 |
| **in** | 연산자 | `"사과" in fruits` | 포함 여부 확인 |
| **sort()** | 리스트 메서드 | `fruits.sort()` | 오름차순 정렬 |
| **reverse()** | 리스트 메서드 | `fruits.reverse()` | 순서 뒤집기 |
| **리스트 컴프리헨션** | 문법 | `[i**2 for i in range(10)]` | 간결한 리스트 생성 |
| **조건 포함 컴프리헨션** | 문법 | `[i for i in data if i%2==0]` | 조건 기반 리스트 생성 |
| **sum()** | 내장 함수 | `sum(scores)` | 합계 계산 |
| **len() / sum() 조합** | 연산 | `sum(scores)/len(scores)` | 평균 계산 |
| **range()** | 내장 함수 | `for i in range(10):` | 숫자 반복 범위 제공 |
| **리스트 변환식** | 컴프리헨션 | `[n*2 if n%2==1 else n*3 for n in numbers]` | 조건에 따라 값 변환 |
| **슬라이싱과 평균** | 로직 | `prices[i:i+window]` | 이동 평균 계산 시 사용 |
| **window, moving_avg** | 변수 | `window = 3` | 슬라이딩 윈도우 예시 변수 |
| **리스트 관련 키워드** | 참고 | `append, insert, extend, remove, pop, del, sort, reverse, sum, len, range, in` | 리스트 조작 핵심 |

---

## 🧩 2.2 튜플 (Tuple)

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **point, rgb** | 변수 | `(10, 20)`, `(255,128,0)` | 튜플 생성 예시 |
| **튜플 (immutable)** | 자료형 | `(1, 2, 3)` | 수정 불가능한 시퀀스 |
| **인덱싱** | 문법 | `point[0]` | 값 접근 (리스트와 동일) |
| **언패킹** | 문법 | `x, y = point` | 여러 값 한 번에 변수로 저장 |
| **튜플 불변성** | 개념 | `point[0] = 30` | 수정 시 오류 발생 |
| **함수 반환 튜플** | 예제 | `return (name, age, grade, score)` | 여러 값 반환에 활용 |
| **math.sqrt(), math.atan2()** | 수학 함수 | `math.sqrt(x**2 + y**2)` | 거리, 각도 계산 |
| **라디안→도 변환** | 연산 | `math.atan2(y, x) * 180 / math.pi` | 각도 단위 변환 |
| **튜플 리스트 변환** | 예제 | `[(x, y, x+y) for x,y in points]` | 튜플 기반 데이터 변환 |
| **polar_coords** | 변수 | `(r, θ)` | 극좌표 계산 결과 |
| **튜플 관련 키워드** | 참고 | `tuple, unpacking, math, sqrt, atan2, immutable` | 튜플의 특징과 관련 함수 |

---

## 🧩 2.3 딕셔너리 (Dictionary)

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **student, person, contacts, students** | 변수 | `{"name":"홍길동","age":20}` | key-value 구조 저장 |
| **키 접근** | 문법 | `student["name"]` | 특정 key의 값 접근 |
| **get()** | 메서드 | `student.get("email","없음")` | 안전한 접근, 기본값 지정 가능 |
| **딕셔너리 추가/수정** | 문법 | `person["city"]="Seoul"` | 값 추가 또는 수정 |
| **del, pop()** | 삭제 구문 | `del person["city"]`, `pop("age")` | 항목 제거 |
| **keys(), values(), items()** | 메서드 | `person.keys()` | key, value, (key,value) 조회 |
| **딕셔너리 순회** | 반복문 | `for key, value in person.items():` | 키-값 반복 처리 |
| **딕셔너리 중첩 구조** | 자료형 | `{ "김철수": {"math":85,"english":90}}` | 내부 딕셔너리 포함 가능 |
| **sum(), len()** | 내장 함수 | `sum(scores.values())/len(scores)` | 평균 계산 |
| **max() + key 인자** | 함수 활용 | `max(word_count, key=word_count.get)` | 특정 기준으로 최대값 찾기 |
| **lambda** | 익명 함수 | `lambda x: x[1][subject]` | 정렬/검색용 키 함수 |
| **딕셔너리 생성/조회/삭제** | 패턴 | `dict[key]=value`, `del dict[key]`, `get()` | 핵심 조작 패턴 |
| **딕셔너리 관련 키워드** | 참고 | `keys, values, items, get, pop, del, lambda, max, sum, len` | 딕셔너리 핵심 기능 정리 |

---

## 🧩 2.4 세트 (Set)

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **numbers, data, unique** | 변수 | `{1,2,3}`, `set(data)` | 중복 제거 및 집합 생성 |
| **집합 연산자** | 연산 | `a | b`, `a & b`, `a - b` | 합집합·교집합·차집합 |
| **set()** | 형 변환 함수 | `set([1,2,2,3])` | 리스트 → 집합 변환 |
| **list() 변환** | 함수 | `list(set(data))` | 집합 → 리스트 변환 |
| **attendance, unique_students** | 변수 | `list(set(attendance))` | 중복 제거 예시 |
| **공통 관심사** | 연산 | `person_a & person_b` | 교집합 사용 |
| **차집합 / 합집합** | 연산 | `person_a - person_b`, `person_a | person_b` | 차이 및 전체 결합 |
| **len()** | 내장 함수 | `len(common)` | 원소 개수 계산 |
| **자카드 유사도** | 수학 개념 | `len(common)/len(all_interests)` | 집합 기반 유사도 계산 |
| **문서 단어 집합화** | 로직 | `set(doc.split())` | 문자열 단어 중복 제거 |
| **lower(), split()** | 문자열 메서드 | `doc.lower().split()` | 소문자 변환 및 분리 |
| **리스트 컴프리헨션 벡터화** | 문법 | `[1 if word in words1 else 0 for word in vocabulary]` | 문서 벡터 표현 |
| **vocabulary** | 변수 | `sorted(all_words)` | 전체 단어 목록 정렬 |
| **세트 관련 키워드** | 참고 | `set, union(|), intersection(&), difference(-), len, list, split, lower` | 집합 및 중복 제거 핵심 |

---

# 📘 Part 3 — 함수

---

## 🧩 3.1 함수 정의와 호출

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **def** | 키워드 | `def greet(name):` | 함수 정의 시작 |
| **함수 이름** | 식별자 | `greet`, `add`, `get_stats` | 동작을 표현하는 이름 |
| **매개변수(parameter)** | 문법 | `(name)`, `(a,b)` | 입력값을 받는 변수 |
| **인자(argument)** | 호출 구문 | `greet("홍길동")` | 함수를 호출할 때 전달하는 값 |
| **docstring** | 주석 | `"""인사 함수"""` | 함수 설명 문자열 |
| **return** | 키워드 | `return a + b` | 결과값 반환 |
| **다중 반환** | 문법 | `return total, avg` | 여러 값 반환 (튜플 형태) |
| **기본 매개변수(default)** | 문법 | `def power(base, exponent=2)` | 인자 기본값 지정 |
| **가변 인자** | 문법 | `*args`, `**kwargs` | 여러 값(또는 키워드)을 받음 |
| **sum(), len()** | 내장 함수 | `sum(numbers) / len(numbers)` | 합계·길이 계산 |
| **print(f"...")** | f-string | `f"합계: {total}"` | 결과를 형식 출력 |
| **함수 호출 순서** | 개념 | `함수 정의 → 호출` | 정의 후 호출해야 실행 |
| **예제 함수명** | 변수 | `rectangle_area`, `convert_temperature`, `calculate_statistics` | 실습용 함수들 |
| **try/except 없음** | 문법 | — | 함수 내 오류 처리는 별도 |
| **dict 반환형** | 자료형 | `{ "mean": mean, "std_dev": std }` | 여러 결과를 딕셔너리로 반환 |
| **표준편차 계산** | 식 | `(sum((x - mean)**2)/n)**0.5` | 수학 계산식 예시 |
| **zip()** | 내장 함수 | `zip(scores, z_scores)` | 여러 리스트 동시 순회 |
| **for key, value in dict.items()** | 반복문 | `for key, value in stats.items()` | 딕셔너리 반복 출력 |
| **함수 관련 키워드** | 참고 | `def, return, parameter, argument, docstring, default value` | 함수 정의 핵심 |

---

## 🧩 3.2 람다 함수 (Lambda)

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **lambda** | 키워드 | `lambda x: x**2` | 익명 함수 정의 |
| **람다 표현식** | 문법 | `lambda x, y: x + y` | 한 줄 함수 |
| **람다 저장 변수** | 변수 | `square_lambda = lambda x: x**2` | 이름을 붙여 재사용 가능 |
| **sorted()** | 내장 함수 | `sorted(students, key=lambda x: x["score"])` | 정렬 기준 지정 |
| **reverse=True** | 옵션 | `sorted(..., reverse=True)` | 내림차순 정렬 |
| **filter()** | 내장 함수 | `filter(lambda x: x%2==0, numbers)` | 조건에 맞는 요소 선택 |
| **map()** | 내장 함수 | `map(lambda x: x*2, numbers)` | 모든 요소에 함수 적용 |
| **reduce()** | 내장 함수 (functools) | `reduce(lambda x,y: x*y, numbers)` | 누적 연산 처리 |
| **compose()** | 사용자 정의 함수 | `compose(f,g)` | 두 함수 합성 (f(g(x))) |
| **add_10, multiply_2, square** | 람다 변수 | `lambda x: x+10` | 합성용 익명 함수 |
| **파이프라인 처리** | 구조 | `map → filter → map` | 함수형 처리 순서 |
| **리스트 정렬** | 응용 | `key=lambda x: x["rating"]` | 람다 활용 예시 |
| **람다식의 반환값** | 문법 | `lambda x: (조건식)` | 한 줄 결과 반환 |
| **reduce import** | 모듈 | `from functools import reduce` | reduce() 사용을 위한 임포트 |
| **람다와 고차함수** | 개념 | `함수를 인자로 전달` | 함수형 프로그래밍 방식 |
| **람다 관련 키워드** | 참고 | `lambda, map, filter, reduce, key, sorted, compose` | 람다 및 함수형 처리 핵심 |

---

## 🧩 3.3 유용한 내장 함수

| 용어 | 종류 | 관련 예시 | 설명 |
|------|------|------------|------|
| **map()** | 내장 함수 | `map(lambda x:x**2, numbers)` | 모든 요소에 함수 적용 |
| **filter()** | 내장 함수 | `filter(lambda x:x%2==0, numbers)` | 조건에 맞는 값만 필터링 |
| **zip()** | 내장 함수 | `zip(names, scores)` | 여러 리스트 병렬 묶기 |
| **dict(zip())** | 변환 | `dict(zip(names,scores))` | 리스트 → 딕셔너리 변환 |
| **enumerate()** | 내장 함수 | `for idx, item in enumerate(fruits)` | 인덱스와 값 동시 접근 |
| **언패킹(*)** | 연산자 | `print(*numbers)` | 리스트 요소를 펼쳐 전달 |
| **패킹(*)** | 문법 | `a, *rest = [1,2,3,4]` | 나머지 값 묶기 |
| **다중 패킹/언패킹** | 문법 | `*start, last = seq` | 유연한 구조 분해 |
| **리스트 컴프리헨션** | 문법 | `[x for x in numbers if x%2==0]` | 간결한 리스트 생성 |
| **sum(), max(), min()** | 내장 함수 | `sum(scores)`, `max(numbers)` | 집계용 함수 |
| **for zip() in loop** | 반복문 | `for name,score in zip(names,scores):` | 여러 리스트 동시 반복 |
| **start 인자** | enumerate 옵션 | `enumerate(fruits,start=1)` | 시작 인덱스 지정 |
| **map+filter 조합** | 고급 사용 | `map(..., filter(...))` | 함수형 파이프라인 |
| **replace(), int(), str()** | 문자열/형변환 | `"1,000".replace(",","")` | 데이터 전처리 예시 |
| **list(map(int,...))** | 변환 패턴 | 문자열 리스트를 숫자로 변환 |
| **lambda 포맷팅** | 문자열 가공 | `f"{x:,}원"` | 천 단위 포맷 지정 |
| **데이터 분석 루프** | 예시 | `for subject, *scores in zip(...):` | 언패킹 기반 평균 계산 |
| **max(..., key=...)** | 고급 패턴 | `max(scores, key=lambda x:x[1])` | 특정 기준으로 최대값 탐색 |
| **내장함수 관련 키워드** | 참고 | `map, filter, zip, enumerate, sum, max, min, *` | 반복·변환 핵심 함수 |

---
