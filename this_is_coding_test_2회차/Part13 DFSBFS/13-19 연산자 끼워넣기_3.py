n=int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
valueMax=-1e9
valueMin=1e9
result=data[0]

def dfs(cnt,result):
    global add,sub,mul,div,valueMax,valueMin
    if cnt==n-1:
        valueMax=max(valueMax,result)
        valueMin = min(valueMin, result)
        return
    if add>0:
        add-=1
        dfs(cnt+1,result+data[cnt+1])
        add+=1
    if sub>0:
        sub-=1
        dfs(cnt+1,result-data[cnt+1])
        sub+=1
    if mul>0:
        mul-=1
        dfs(cnt+1,result*data[cnt+1])
        mul+=1
    if div>0:
        div-=1
        dfs(cnt+1,int(result/data[cnt+1]))
        div+=1

dfs(0,result)

print(valueMax,valueMin)