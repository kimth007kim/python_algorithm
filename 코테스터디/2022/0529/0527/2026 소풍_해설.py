
def dfs(v,arr):
    if len(arr)==k:
        for num in arr:
            print(num)
        exit()
        # return
    for i in range(v+1,n+1):
        # print(i)
        if not visited[i]:
            for num in arr:
                if num not in graph[i]:
                    break
            else:
                visited[i]=True
                dfs(i,arr+[i])


k,n,f = map(int,input().split())

graph= {i: [] for i in range(1,n+1)}

for _ in range(f):
    a,b = map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]



for i in range(1,n+1):
    visited={i:False for i in range(1,n+1)}
    visited[i]=True
    # print(visited)
    dfs(i,[i])

print(-1)