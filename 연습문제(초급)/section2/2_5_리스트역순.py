# 리스트 역순으로 뒤집기

fruits = ["사과", "바나나", "포도", "수박"]
print(fruits[::-1])

# 강사님 풀이

fruits = ["사과", "바나나", "포도", "수박"]

# 방법 1
reversed_fruits = fruits[::-1]
print(reversed_fruits)

# 방법 2
fruits.reverse()
print(fruits)