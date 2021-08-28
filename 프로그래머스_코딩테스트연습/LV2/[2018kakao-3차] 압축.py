def check(message,start,cnt,dic,answer):
    for i in range(start,len(message)):
        t="".join(message[start:i+1])
        if t not in dic:
            dic[t]=cnt
            cnt+=1
            for k in dic:
                if k==t[:len(t)-1]:
                    answer.append(dic[k])
            return i
    for i in dic:
        if i== "".join(message[start:]):
            answer.append(dic[i])
            return -1
def solution(msg):
    answer = []
    dic={}
    message=list(msg)
    cnt=0
    for i in range(65,91):
        cnt+=1
        dic[chr(i)]=cnt
    seq=0
    start=0
    while start!=-1:
        cnt+=1
        start=check(message,start,cnt,dic,answer)
    return answer