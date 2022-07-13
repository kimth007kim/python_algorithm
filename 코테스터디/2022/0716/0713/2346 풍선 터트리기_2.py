n=int(input())

visited=[False]*n
visit =n
arr= list(map(int,input().split()))
now=0

answer=[]

while visit>0:
    move = arr[now]
    answer.append(now+1)
    visited[now]=True
    visit-=1

    if visit==0:
        break
    if move>0:
        while move>0:
            now+=1
            if now>=n:
                now=0
            if visited[now]==True:
                continue
            move-=1

    else:
        while move<0:
            now-=1
            if now<0:
                now=n-1
            if visited[now]==True:
                continue
            move+=1
print(*answer)