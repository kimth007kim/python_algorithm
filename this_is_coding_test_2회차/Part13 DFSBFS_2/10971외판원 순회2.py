import sys
input=sys.stdin.readline

n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

number=[1]*n

min_value=10**7

def dfs(cnt,start,prev,result):
    global min_value,number
    if cnt==n-1:
        if graph[prev][start]==0:
            return
        else:
            answer=result+graph[prev][start]
            # print(answer)
            min_value=min(min_value,answer)
        return
    for j in range(n):
        if graph[prev][j]!=0 and number[j]!=0:
            number[j]=0
            dfs(cnt+1,start,j,result+graph[prev][j])
            number[j]=1

for i in range(n):
    number[i]=0
    dfs(0,i,i,0)
    number[i] = 1
print(min_value)