class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = ['(', '{', '[']
        closed = [')', '}', ']']

        for c in s:
            if c in opened:
                stack.append(c)
            elif not len(stack) or opened.index(stack.pop()) != closed.index(c):
                return False

        return len(stack) == 0

    def isValid2(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or stack.pop() != table[char]:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    t = Solution()
    s = "()"
    print(t.isValid(s))
