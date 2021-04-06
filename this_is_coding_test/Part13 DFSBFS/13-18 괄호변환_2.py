# p=	"(()())()"
# result="(()())()"

p=	"()))((()"
result="()(())()"
#
# p= 'abcdefg'

def correct(p):
    count=0
    for i in range(len(p)):
        if p[i] =="(":
            count+=1
        else:
            count-=1
        if count == 0:
            return i

def check_proper(p):
    count=0
    for i in p:
        if i == '(':
            count+=1
        else:
            if count == 0:
                return False
            count -=1
    return True

def solution(p):
    answer=''
    if p == '':
        return answer
    index=correct(p)
    print(index)
    u=p[:index+1]
    v=p[index+1:]
    if check_proper(u):
        answer= u+solution(v)
    else:
        answer='('
        answer+=solution(v)
        answer+=')'
        u = list(u[1:-1])
        print(u)
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('
        print(answer)
        answer += "".join(u)
        print(answer)
    return answer

print(solution(p))
