n=int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
mxvalue=-1e9
mnvalue=1e9


def calc(cnt,now):
    global add,sub,mul,div,mxvalue,mnvalue
    if cnt==n-1:
        mxvalue=max(mxvalue,now)
        mnvalue=min(mnvalue,now)
        return
    else:
        if add>0:
            add-=1
            calc(cnt+1,now+data[cnt+1])
            add+=1
        if sub>0:
            sub-=1
            calc(cnt+1,now-data[cnt+1])
            sub+=1
        if mul>0:
            mul-=1
            calc(cnt+1,now*data[cnt+1])
            mul+=1
        if div>0:
            div-=1
            calc(cnt+1,int(now/data[cnt+1]))
            div+=1

calc(0,data[0])

print(mxvalue,mnvalue)