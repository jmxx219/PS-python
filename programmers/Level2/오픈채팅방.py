from collections import defaultdict


def solution(record):
    res = []
    user = defaultdict(str)
    enters = []
    for st in record:
        chat = list(map(str, st.split()))
        if chat[0] == "Enter":
            user[chat[1]] = chat[2]
            enters.append([chat[1], True])
        elif chat[0] == "Change":
            user[chat[1]] = chat[2]
        else:
            enters.append([chat[1], False])

    for id, enter in enters:
        s = user[id]
        if enter:
            s += "님이 들어왔습니다."
        else:
            s += "님이 나갔습니다."
        res.append(s)

    return res


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
              "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))