# 균형잡힌 괄호 문자열: 개수만 맞는 경우
# 올바른 괄호 문자열: 개수도 맞고 짝도 맞는경우

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.

# ()))((()
# print(p[2:])     // ))((()
# print(p[:2])     // ()

def solution(p):
    u = ""
    v = ""
    result = []
    word = ""
    plen = len(p)
    if plen == correct(p):
        return p
    if make(p) == 0:
        u += p[:2]
        v += p[2:]
    else:
        u += p[2:]
        v += p[:2]

    return word


# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
def correct(p):
    dd = ""
    plen = len(p)
    point = 0
    cnt = 0
    array = []
    for i in range(plen):
        if p[i] == "(":
            point += 1
        if p[i] == ")":
            point -= 1
        if point == -1 or cnt == plen:
            break
        cnt += 1
    return cnt


def make(p):
    plen = len(p)
    if p[0] != p[1]:
        print("달라1")
        return 0
    if p[plen - 1] != p[plen - 2]:
        print("달라2")
        return 1