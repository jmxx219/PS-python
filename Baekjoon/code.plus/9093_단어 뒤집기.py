def solve(st_list):
    for st in st_list:
        while len(st) > 0:
            print(st.pop(), end="")
        print(' ', end="")
    print()


T = int(input())
st_list = []
for _ in range(T):
    st_list = list(map(list, input().split(' ')))
    solve(st_list)