def solution(queue1, queue2):
    SUM=sum(queue1)+sum(queue2)
    if SUM%2==1:
        return -1
    target=SUM//2
    length = len(queue1)+len(queue2)
    MAXLEN = len(queue1)+len(queue2)-1
    q= queue1+queue2+queue1
    start=0
    end=0
    cnt=0
    total=0
    tcnt=0
    arr=[]
    while start<length and end<length:
        while total<target and cnt<MAXLEN and end<length:
            total+=q[end]
            end+=1
            cnt+=1
            tcnt+=1
            # print(start,end,cnt,total)
        if total==target:
            arr.append([start,end-1])
            break
        total-=q[start]
        cnt-=1
        start+=1
        tcnt+=1
    if len(arr)==0:
        return -1
    s1=0
    e1=len(queue1)-1
    s2=len(queue1)
    e2=len(queue1)+len(queue1)-1
    answer =int(1e10)
    for s,e in arr:
        print(s,e)
        if end<len(queue1)-1:
            answer = min(answer,length-(e-s)-1)
        else:
            answer= min(answer,abs(s-s1)+abs(e-e1),abs(s-s2)+abs(e-e2))
    return answer