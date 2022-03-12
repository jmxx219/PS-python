def hanoi(n, start, end):
    if n > 1:
        hanoi(n-1, start, 6-start-end)  # 기둥이 1개 이상이면 그룹으로 묶인 n-1개 원판을 중간(2)으로

    print(start, end) # 마지막 원판을 끝(3)으로

    if n > 1:
        hanoi(n-1, 6-start-end, end)    # 기둥이 1개 이상이면 그룹으로 묶인 n-1개 원판을 끝(3)으로


n = int(input())
print(2**n -1)  #총 이동해야 하는 횟수
hanoi(n, 1, 3)  # 원반갯수, 시작, 목표



# def 하노이(원반갯수, 시작, 목표, 보조):
#     if 원반갯수 == 1:
#         print(시작, 목표)
#         return
#     하노이(원반갯수, 시작, 보조, 목표)
#     print(시작, 목표)
#     하노이(원반갯수, 보조, 목표, 시작)

# 하노이(n, 1, 2, 3)