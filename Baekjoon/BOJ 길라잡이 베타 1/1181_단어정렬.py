from sys import stdin

N = int(stdin.readline())

words = []
for i in range(N):
    word = stdin.readline().rstrip()
    words.append(word)

words = list(set(words)) # 중복제거
words.sort(key=lambda x: (len(x), x)) # 1. 길이 기준, 2. 사전 순

print("\n".join(word))
