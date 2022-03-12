strs = input().upper()
alpha = [0 for _ in range(26)]

for i in range(26):
    alpha[i] = strs.count(chr(65 + i))

maxi = max(alpha)
if alpha.count(maxi) > 1:
    print('?')
else:
    print(chr(alpha.index(maxi) + 65))
