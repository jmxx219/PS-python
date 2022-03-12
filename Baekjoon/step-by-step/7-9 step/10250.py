T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    N -= 1
    layer = (N % H + 1) * 100
    room = N // H + 1
    print(layer + room)
    # layer = N % H
    # room = N // H + 1
    # if layer == 0:
    #     layer = H
    #     room -= 1
    # if room < 10:
    #     room = '0' + str(room)
    # print(f'{layer}{room}')