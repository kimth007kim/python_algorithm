minN=1e9
maxN=-1e9

n= int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

def dfs(i,now):
    global minN,maxN,add,sub,mul,div
    if i == n:
        minN=min(minN,now)
        maxN=max(maxN,now)
    else:
        if add>0:
            print(i,data[i])
            add-=1
            dfs(i+1,now+data[i])
            add+=1
        if sub>0:
            print(i,data[i])
            sub-=1
            dfs(i+1,now-data[i])
            sub+=1
        if mul>0:
            print(i,data[i])
            mul-=1
            dfs(i+1,now*data[i])
            mul+=1
        if div>0:
            print(i,data[i])
            div-=1
            dfs(i+1,int(now/data[i]))
            div+=1

dfs(1,data[0])

print(maxN)
print(minN)