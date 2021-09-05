from sys import stdin


def inRange(y: int, x: int):
    return 0 <= x < Size and 0 <= y < Size


def hasWord(y: int, x: int, word: str):
    if not inRange(y, x): return False
    if board[y][x] != word[0]: return False
    if len(word) == 1: return True

    for direction in range(8):
        nextY = y + dy[direction]
        nextX = x + dx[direction]
        if hasWord(nextY, nextX, word[1:]): return True
    return False


def findFirstWord(word: str):
    for y in range(Size):
        for x in range(Size):
            if board[y][x] == word[0]:
                if hasWord(y, x, word): return True
    return False


dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
Size = 5
t = int(stdin.readline())
for _ in range(t):
    board = []
    for i in range(5):
        board.append(list(stdin.readline()))
    n = int(input())  # 단어 수
    for i in range(n):
        words = str(stdin.readline())
        print(words, end=" ")
        if findFirstWord(words):
            print("YES")
        else:
            print("NO")
