import sys

input = sys.stdin.readline

n,k,q,m= map(int,input().split())
sleep= set(list(map(int,input().split())))
# number= list(map(int,input().split()))
answer=set()

# for i in number:
#     if i in sleep:
#         break
#     answer.add(i)
#     now =i
#     cnt=2
#     while True:
#         now = i*cnt
#         if 3>now or now>n+2:
#             break
#         if now not in sleep:
#             answer.add(now)
#             cnt+=1
#         else:
#             break
for i in map(int, input().split()):
    if i in sleep:
        continue

    for j in range(i, n + 3, i):
        if j not in sleep:
            answer.add(j)
graph=[0]
for i in range(1,n+3):
    if i in answer:
        graph.append(graph[-1]+1)
    else:
        graph.append(graph[-1]+0)
# print(graph)
# prev= graph[0]
# for i in range(1,n+3):
#     graph[i]+=prev
#     prev=graph[i]
# print(graph)
for _ in range(m):
    s,e= map(int,input().split())
    print(e-s+1-(graph[e]-graph[s-1]))

