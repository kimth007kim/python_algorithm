def judge(arr,now):
    for i in arr:
        if now not in graph[i]:
            return False
        if i not in graph[now]:
            return False
    return True


def dfs(arr,prev):
    global answer
    if len(arr)==k:
        tmp = []
        for i in arr:
            tmp.append(i)
            tmp.sort()
        if tmp not in answer:
            answer.append(tmp)
        return
    for i in graph[prev]:
        if i not in arr:
            if judge(arr,i):
                arr.append(i)
                dfs(arr,i)
                arr.pop()
    # print(arr,graph)

k,n,f = map(int,input().split())

graph=[[] for _ in range(n+1)]
# print(graph)
for i in range(f):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


answer=[]
# print(graph)

for i in range(1,n+1):
    dfs([i],i)

# print(judge([1,3,2],6))

if len(answer)==0:
    print(-1)
else:
    answer.sort()
    for i in answer[0]:
        print(i)