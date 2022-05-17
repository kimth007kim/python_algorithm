# 수행해야 할 작업 N개 (3 ≤ N ≤ 10000)가 있다.
# 각각의 작업마다 걸리는 시간(1 ≤ 시간 ≤ 100)이 정수로 주어진다.

# 몇몇 작업들 사이에는 선행 관계라는 게 있어서, 어떤 작업을 수행하기 위해 반드시 먼저 완료되어야 할 작업들이 있다.
# 이 작업들은 번호가 아주 예쁘게 매겨져 있어서,
# K번 작업에 대해 선행 관계에 있는(즉, K번 작업을 시작하기 전에 반드시 먼저 완료되어야 하는) 작업들의 번호는 모두 1 이상 (K-1) 이하이다.
# 작업들 중에는, 그것에 대해 선행 관계에 있는 작업이 하나도 없는 작업이 반드시 하나 이상 존재한다. (1번 작업이 항상 그러하다)

# 모든 작업을 완료하기 위해 필요한 최소 시간을 구하여라.
# 물론, 서로 선행 관계가 없는 작업들은 동시에 수행 가능하다.

from collections import defaultdict
n= int(input())
indegree=defaultdict(list)
# indegree= [0]*(n+1)
graph= [[] for _ in range(n+1)]
cost={}
for i in range(1,n+1):
    arr= list(map(int,input().split()))
    cost[i]=arr[0]
    indegree[len(arr[2:])].append(cost[i])
    # for j in arr[2:]:
    #     graph[j].append(i)
answer=0
for i in indegree:
    MAX=-1
    for j in indegree[i]:
        MAX= max(MAX,j)
    answer+=MAX
print(answer)