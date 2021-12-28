import sys
sys.setrecursionlimit(90000)
input = sys.stdin.readline

n=1
answer= []
LIMITED= 0
while n!=0:
    n = int(input())
    if n ==0:
        # 0이 들어왔을때 answer안에있는 것들 출력
        for i in answer:
            if i==True:
                print("Yes")
            elif i==False:
                print("No")
        break

    # graph = 경로를 저장하는 배열
    graph = [[] for _ in range(n + 1)]
    # cost = 비용을 저장하는 배열
    cost = [0]

    for i in range(1, n + 1):
        tmp = list(input().split())
        type = tmp[0]
        coin= int(tmp[1])
        # 트롤일때 부호 마이너스 붙여서  비용에다가 집어넣음
        if type == "T":
            coin = -coin
        cost.append(coin)
        for j in range(2,len(tmp)-1):
            graph[i].append(int(tmp[j]))

    isTrue = False
    print(graph,cost)

    for i in cost:
        print(i)


    def dfs(now, value):
        global isTrue
        if now == n:
            isTrue = True
            return
        print(now,value)
        for i in graph[now]:
            if i != now:
                if cost[i] < 0:
                    if value + cost[i] > 0:
                        dfs(i, value - cost[i])
                elif cost[i] > 0:
                    MAX = max(cost[i], value)
                    dfs(i, MAX)
                else:
                    dfs(i, value)

    dfs(1, 0)
    answer.append(isTrue)
