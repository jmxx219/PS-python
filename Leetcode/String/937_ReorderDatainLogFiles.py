from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs_st = []
        logs_di = []
        for st in logs:
            if 48 <= ord(st[-1]) <= 57:
                logs_di.append(st)
            else:
                logs_st.append(list(st.split(" ", 1)))

        logs_st.sort(key=lambda x: (x[1], x[0]))

        res = []
        for st in logs_st:
            res.append(" ".join(st))

        return res + logs_di


    def reorderLogFiles2(self, logs: List[str]) -> List[str]:
        logs_st = []
        logs_di = []
        for log in logs:
            if log.split()[1].isdigit():
                logs_di.append(log)
            else:
                logs_st.append(log)

        logs_st.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return logs_st + logs_di


if __name__ == "__main__":
    t = Solution()
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(t.reorderLogFiles2(logs))
