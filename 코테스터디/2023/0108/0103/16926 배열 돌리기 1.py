import sys


def turn(d,graph):
    t,b,l,r=d
    # print(l,r,b,t)
    copied = [[0]*(m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copied[i][j]=graph[i][j]
    # cnt=0
    while r-l>=1 and b-t>=1:
        prev=graph[t][l]
        # print(prev,l,r,b,t)
        for i in range(t+1,b):
            # print(i)
            tmp= graph[i][l]
            copied[i][l]=prev
            prev= tmp

        for i in range(l,r+1):
            tmp= graph[b][i]
            copied[b][i]=prev
            prev = tmp

        for i in range(b-1,t,-1):
            # print("i = ",i)
            tmp=graph[i][r]
            copied[i][r]=prev
            prev= tmp
        for i in range(r,l-1,-1):
            tmp = graph[t][i]
            copied[t][i] = prev
            prev = tmp

        # print("======")
        # if cnt==1:
        #     for i in copied:
        #         print(i)
        # print("======")
        t,b,l,r=t+1,b-1,l+1,r-1
        # cnt+=1
    return copied

input = sys.stdin.readline

n,m,t= map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

d= [0,n-1,0,m-1]
# for i in graph:
#     print(i)
for i in range(t):
    graph=turn(d,graph)

for i in graph:
    print(*i)