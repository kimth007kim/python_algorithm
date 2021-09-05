# https://www.acmicpc.net/problem/16964


n= int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)

result=list(map(int,input().split()))
answer=[]
visited=[ i for i in range(1,n+1)]
print(visited)

def dfs(num,arr,visited):
    print(num,graph[num],arr)
    if graph[num]==[] and len(arr)>=1:
        answer.append(arr)
        # arr.remove(num)
        return
    print(arr)
    for i in graph[num]:
        arr.append(i)
        dfs(i,arr,visited)
        arr.remove(i)
    return
dfs(1,[],visited)
print(answer)
