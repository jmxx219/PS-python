import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[~!@#$%^&*()=+\[\{\]\}:?,\<\>/]", "", new_id)
    new_id = re.sub("(([.])\\2{1,})", ".", new_id)

    # 4단계
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]

    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]

    # 5단계
    if new_id == "":
        new_id = "a"

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == ".":
        new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        while len(new_id) <= 3:
            new_id += new_id[-1]

    return new_id


def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
