#
#
# from itertools import combinations
# from collections import deque
# import sys
#
# input= sys.stdin.readline
#
# def calc(cgraph):
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if cgraph[i][j]==0:
#                 cnt+=1
#     return cnt
#
# def spread(graph,virus):
#     dx=[1,0,-1,0]
#     dy=[0,1,0,-1]
#     q=deque(virus)
#
#     while q:
#         x,y =q.popleft()
#         for i in range(4):
#             nx=dx[i]+x
#             ny=dy[i]+y
#             if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
#                 graph[nx][ny]=2
#                 q.append((nx,ny))
#
#     return calc(graph)
#
# n,m=map(int,input().split())
# graph=[]
#
# virus=[]
# space=[]
# answer=[]
#
# for i in range(n):
#     tmp=list(map(int,input().split()))
#     graph.append(tmp)
#     for j in range(len(tmp)):
#         if tmp[j]==0:
#             space.append((i,j))
#         elif tmp[j]==2:
#             virus.append((i,j))
#
# comb = combinations(space,3)
# for i in list(comb):
#     cgraph = [graph[j][:] for j in range(n)]
#     for x,y in i:
#         cgraph[x][y]=1
#
#     answer.append(spread(cgraph,virus))
#
#     for x,y in i:
#         cgraph[x][y]=0
#
# print(max(answer))


data=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(4):
    tmp= [data[i][:] for i in range(3)]
    print(tmp,"-----")
    tmp[0][0]=3
    print("------------",data)
    print(tmp)