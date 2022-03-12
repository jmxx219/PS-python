a = int(input())

# for j in range(a):
#     print("*" * (j+1))

for j in range(a):
    print(" " * (a - j - 1) + "*" * (j+1))
