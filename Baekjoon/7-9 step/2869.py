import math

a, b, v = map(int, input().split())
day = (v - a) / (a - b) + 1
print(math.ceil(day))  # 올림 함수

# day = (v - b - 1) // (a - b) + 1
# print(day)  # 올림 함수
