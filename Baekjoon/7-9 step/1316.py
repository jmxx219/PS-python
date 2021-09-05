t = int(input())
cnt = 0
for i in range(t):
    bl = True
    strs = list(input())
    if len(strs) == 1:
        cnt += 1
        continue
    str_set = set()
    str_set.add(strs[0])
    for x in range(1, len(strs)):
        if strs[x-1] == strs[x]:
            continue
        elif strs[x] not in str_set:
            str_set.add(strs[x])
        else:
            bl = False
    if bl:
        cnt += 1
print(cnt)

# result = 0
# for i in range(int(input())):
#     word = input()
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)