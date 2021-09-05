s = list(str(input()))
res = [-1 for _ in range(26)]
for i in range(len(s)):
    if res[ord(s[i]) - 97] == -1 :
        res[ord(s[i]) - 97] = i
for i in range(len(res)):
    print(res[i], end=' ')

# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위

# for x in alphabet :
#     print(word.find(chr(x)))