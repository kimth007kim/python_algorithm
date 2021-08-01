def check(s):
    prev=s[0]
    LEN=len(s)
    for i in range(1,LEN):
        now = s[i]
        if now == prev:
            left =s[0:i-1]
            right=s[i+1:LEN]
            return left+right
        else:
            prev=now
    return s


def solution(s):
    while len(s)>0:
        slen=len(s)
        s=check(s)
        tlen=len(s)
        if tlen==slen:
            return 0
    if len(s)==0:
        return 1
    else:
        return 0