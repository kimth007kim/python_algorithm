def solution(p):
    if p == '':
        return p
    n = check(p)
    # 2단계
    u = p[:n + 1]
    v = p[n + 1:]
    # print("u=",u,"  ","v=",v)

    # 3단계
    if correct(u) == True:
        # 3-1단계
        return u + solution(v)
        # print("참")
    else:
        # 4단계
        temp = ""
        temp += "("
        temp += solution(v)
        temp += ")"

        # print(temp)
        for i in range(1, len(u) - 1):
            if u[i] == "(":
                temp += ")"
            else:
                temp += "("
            # print("----------------",u[i])
        # print(temp)
        return temp


# 올바른 문자열인지 확인
def correct(u):
    cnt = 0
    for i in range(len(u)):
        if u[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True


# 균형잡힌 괄호 문자열이 있을 경우, '(' , ')' 의 개수가 같다.
# 균형잡힌 문자열인지 체크하는것
def check(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt -= 1
        else:
            cnt += 1
        if cnt == 0:
            return i
            break
    return len(p)