import sys
from collections import deque
input =sys.stdin.readline
# n=접시수
# d= 초밥의 가짓수
# k= 연속해서 먹는 접시수
# c= 쿠폰번호

n, d, k, c = map(int,input().split())

def visit_plus(num,visited):
    if num in visited:
        visited[num]+=1
    else:
        visited[num]=1
def visit_minus(num,visited):
    if visited[num]==1:
        del visited[num]
    else:
        visited[num]-=1



store= []
for i in range(n):
    store.append(int(input()))

visited={}

store+= store[:k]
q=deque()
for i in range(k):
    visit_plus(store[i], visited)
    q.append(store[i])


MAX= len(visited)
if c not in visited:
    MAX+=1


for i in range(k,n+k-1):
    lt=q.popleft()
    visit_minus(lt, visited)

    q.append(store[i])
    visit_plus(store[i], visited)
    tmp = len(visited)

    if c not in visited:
        tmp += 1

    if tmp>MAX:
        MAX=tmp
print(MAX)
