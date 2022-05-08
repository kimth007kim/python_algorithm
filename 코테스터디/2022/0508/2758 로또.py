def dfs(cnt,now,start):
    global result,visited
    visited[start].add(now)
    print(visited,cnt,now,start)
    if  now>10:
        return
    if cnt ==4 and now<=10:
        result+=1
        return
    temp = now*2
    # if now not in visited[start]:
    #     temp+=1
    dfs(cnt+1,temp,start)
    dfs(cnt,now+1,start)
    # temp+=1

t=int(input())
n,m = map(int,input().split())
visited=[set()]
result=0

for i in range(1,2):
    visited.append(set())
    dfs(1,1,1)

print(result)