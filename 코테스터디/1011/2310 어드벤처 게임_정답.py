import sys
sys.setrecursionlimit(90000)
input = sys.stdin.readline

while True:
    n= int(input())
    if n==0:
        break
    graph= [[] for _ in range(n+1)]
    cost=[0]

    for i in range(1,n+1):
        tmp = input().split()
        type = tmp[0]
        coin = int(tmp[1])
        if type =="T":
            coin = -coin
        cost.append(coin)
        graph[i].extend(list(map(int,tmp[2:-1])))


    isTrue =False
    pocket= 0
    def dfs(now):
        global isTrue
        global pocket
        global visited
        # print("now,pocket",now,pocket)
        if cost[now] >0 and pocket <cost[now]:
            pocket =cost[now]
        if cost[now]<0:
            pocket+=cost[now]

        if pocket>=0:
            if now == n:
                isTrue=True
                return
            else:
                for i in graph[now]:
                    if i!= now and not visited[i]:
                        visited[i]=True
                        dfs(i)
                        visited[i]=False


        visited[now]=False

    visited =[False]*(n+1)
    dfs(1)
    if isTrue:
        print("Yes")
    else:
        print("No")