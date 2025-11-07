## 11/7 수업내용

# 📘 Pandas
---

## 🧩 Part 2.1 Pandas란?

| 함수 / 명령어 | 설명 | 예시 |
|----------------|------|------|
| `pip install pandas` | Pandas 설치 | 터미널에서 실행 |
| `import pandas as pd` | pandas 불러오기 | 코드 상단에 import |

---

## 🧩 Part 2.2 Series & DataFrame

### 📍 Series 관련

| 메소드 / 속성 | 설명 | 예시 결과 |
|----------------|------|------------|
| `pd.Series()` | 리스트나 배열을 Series로 생성 | `0 10`, `1 20`, ... |
| `index` | 인덱스 지정 가능 | `pd.Series([10,20], index=['a','b'])` |
| `s['a']` | 특정 인덱스 값 접근 | 10 |
| `s.values` | 값 배열 반환 | `[10 20 30]` |
| `s.index` | 인덱스 객체 반환 | `Index(['a','b','c'], dtype='object')` |
| `s.dtype` | 데이터 타입 확인 | `int64` |

### 📍 DataFrame 관련

| 메소드 / 속성 | 설명 | 예시 결과 |
|----------------|------|------------|
| `pd.DataFrame()` | 2차원 데이터프레임 생성 | 행·열 구조 데이터 |
| `df.columns` | 컬럼 이름 확인 | `Index(['name','age','city'], dtype='object')` |
| `df.index` | 인덱스 확인 | `[0,1,2]` |
| `df.shape` | (행, 열) 형태 반환 | `(3,3)` |
| `pd.date_range(start, periods, freq)` | 날짜 인덱스 생성 | start: 시작 날짜, periods: 생성할 날짜 개수, freq: 빈도/간격 ('D'=일, 'M'=월, 'H'=시간 등) |
| `df.loc['2024-01-05']` | 특정 날짜(라벨) 선택 | 한 행 반환 |
| `df.loc['2024-01-03':'2024-01-07']` | 날짜 구간 슬라이싱 | 부분 데이터 |
| `df.resample('W').mean()` | 주간 단위 리샘플링 평균 | 주별 평균값 |

---

## 🧩 Part 2.3 CSV 파일 읽기 / 쓰기

| 메소드 / 옵션 | 설명 | 예시 |
|----------------|------|------|
| `pd.read_csv('file.csv')` | CSV 파일 읽기 | DataFrame 반환 |
| `encoding='utf-8' / 'cp949'` | 파일 인코딩 설정 | 한글 깨짐 방지 |
| `usecols=['name','score']` | 특정 열만 읽기 | 필요한 컬럼만 불러옴 |
| `index_col='id'` | 특정 컬럼을 인덱스로 지정 | ID 기준 인덱스 |
| `nrows=5` | 앞부분 일부만 읽기 | 상위 5개 행 |
| `chunksize=100` | 대용량 파일 청크 단위로 읽기 | 반복 처리 가능 |
| `dtype={'id':'int32','value':'float32'}` | 타입 지정으로 메모리 절약 | float32 등 |
| `to_csv('output.csv', index=False)` | CSV 파일 저장 | 인덱스 제외 저장 |
| `encoding='utf-8-sig'` | 한글 CSV 저장용 인코딩 | Excel 호환 |
| `pd.concat(list, ignore_index=True)` | 여러 조각 결합 | 청크 합치기 |

---

## 🧩 Part 2.4 데이터 확인하기

| 메소드 / 속성 | 설명 | 예시 결과 |
|----------------|------|------------|
| `df.head()` | 상위 5개 행 출력 | 처음 일부 미리보기 |
| `df.head(n)` | 상위 n개 행 출력 | `df.head(10)` |
| `df.tail()` | 마지막 5개 행 출력 | 끝부분 확인 |
| `df.info()` | 열별 타입, 결측치, 메모리 요약 | DataFrame 구조 |
| `df.describe()` | 수치형 통계 요약 | count, mean 등 |
| `df.shape` | (행, 열) 개수 | `(1000, 3)` |
| `df.columns` | 열 이름 목록 | `Index(['id','name','score'],dtype='object')` |
| `df.dtypes` | 열별 자료형 확인 | `int64`, `object`, 등 |

---

## 🧩 Part 2.5 데이터 선택하기

### 📍 열 선택

| 문법 / 메소드 | 설명 | 예시 결과 |
|----------------|------|------------|
| `df['col']` | 단일 열 선택 | Series 반환 |
| `df[['col1','col2']]` | 여러 열 선택 | DataFrame 반환 |
| `df['new'] = values` | 새 열 추가 | 계산 결과나 리스트 |

### 📍 행 선택

| 문법 / 메소드 | 설명 | 예시 |
|----------------|------|------|
| `df[:3]` | 처음 3개 행 | 슬라이싱 |
| `df[1:4]` | 1~3행 선택 | 슬라이싱 |

### 📍 loc / iloc

| 메소드 | 기준 | 예시 | 결과 |
|---------|-------|-------|--------|
| `df.loc[row_label]` | 라벨 기반 | `df.loc[0]` | 첫 번째 행 |
| `df.loc[0:2, ['name','age']]` | 행·열 이름 선택 | 부분 DataFrame |
| `df.iloc[row_idx]` | 위치 기반 | `df.iloc[0]` | 첫 번째 행 |
| `df.iloc[0,1]` | 위치 기반 (행,열) | 특정 값 |
| `df.iloc[0:3, 0:2]` | 위치 슬라이싱 | 부분 선택 |

---

## 🧩 Part 2.6 조건 필터링

| 표현식 | 설명 | 결과 |
|----------|------|------|
| `df[df['age'] >= 30]` | 나이 30 이상 행 | 조건에 맞는 행 |
| `df[df['city'] == 'Seoul']` | 특정 값 필터링 | 도시가 서울인 행 |
| `(조건1) & (조건2)` | AND 조건 | 둘 다 만족 |
| `(조건1) \| (조건2)` | OR 조건 | 둘 중 하나 만족 |
| `df['city'].isin(['Seoul','Busan'])` | 여러 값 중 포함 여부 | 해당 도시 필터 |

---

## 🧩 Part 2.7 결측치 처리

| 메소드 | 설명 | 예시 결과 |
|----------|------|------------|
| `df.isnull()` | 결측치 여부(True/False) | 불리언 DataFrame |
| `df.isnull().sum()` | 컬럼별 결측치 개수 | 수치로 표시 |
| `df.dropna()` | 결측치 있는 행 제거 | 새 DataFrame 반환 |
| `df.fillna(0)` | 결측치를 0으로 채움 | 수치형 컬럼에 자주 사용 |
| `df.fillna({'age':0,'city':'Unknown'})` | 컬럼별 다른 값으로 채움 | 맞춤 채우기 |
| `df['col'].fillna(df['col'].mean(), inplace=True)` | 평균으로 결측치 대체 | 원본 수정 |

---

## 🧩 Part 2.8 정렬

| 메소드 | 설명 | 예시 결과 |
|----------|------|------------|
| `df.sort_values('col')` | 해당 컬럼 기준 오름차순 정렬 | 기본 asc=True |
| `df.sort_values('col', ascending=False)` | 내림차순 정렬 | 큰 값이 위로 |
| `df.sort_values(['col1','col2'])` | 여러 열 기준 정렬 | 우선순위 순서대로 |

---

## 🧩 Part 2.9 집계와 그룹화

| 메소드 / 함수 | 설명 | 예시 |
|----------------|------|------|
| `df['col'].sum()` | 합계 | `df['age'].sum()` |
| `df['col'].mean()` | 평균 | `df['score'].mean()` |
| `df['col'].max()` | 최대값 | `df['age'].max()` |
| `df['col'].min()` | 최소값 | `df['age'].min()` |
| `df['col'].count()` | 데이터 개수 | `df['name'].count()` |
| `df.groupby('col')['target'].mean()` | 그룹별 평균 | 도시별 평균 나이 |
| `df.groupby('col')['target'].agg(['mean','max','min'])` | 여러 통계 | 평균/최대/최소 |
| `df['col'].value_counts()` | 각 값 빈도수 | 도시별 개수 등 |

---

## 🧩 Part 2.10 데이터 변경

| 메소드 / 문법 | 설명 | 예시 |
|----------------|------|------|
| `df['new'] = df['age'] * 100` | 계산으로 새 열 생성 | `bonus` 추가 |
| `df['col'].apply(lambda x: ...)` | 조건 기반 새 열 생성 | `grade` 구분 |
| `df.drop('col', axis=1)` | 열 삭제 | 새 DataFrame 반환 |
| `df.drop(['col1','col2'], axis=1, inplace=True)` | 여러 열 삭제 + 원본 수정 | `inplace=True` |
| `df.drop(index)` | 행 삭제 | 인덱스로 삭제 |
| `df.drop([0,1,2])` | 여러 행 삭제 | 부분 제거 |

---

