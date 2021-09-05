while True:
    list_n = list(map(int, input().split()))
    list_n.sort()
    if list_n[0] == 0:
        break
    if list_n[0]**2 + list_n[1]**2 == list_n[2]**2:
        print("right")
    else:
        print("wrong")