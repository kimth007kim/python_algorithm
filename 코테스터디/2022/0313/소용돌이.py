from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]


def clock(q,graph,start,length,dir,turn,number):
    x,y= start
    for i in range(0,length):
        nx=dx[dir]*i+x
        ny=dy[dir]*i+y
        number+=1
        graph[nx][ny]=number

    print()
    for i in graph:
        print(i)


n= 8
graph=[[0]*n for _ in range(n)]
q=deque()
for i in graph:
    print(i)

q.append([[0,0],len(graph)-1,0,0,0])
q.append([[0,n-1],len(graph)-1,1,1,0])
q.append([[n-1,n-1],len(graph)-1,2,2,0])
q.append([[n-1,0],len(graph)-1,3,3,0])
while q:
    start,length,direction,turn,number= q.popleft()
    clock(q, graph,start, length,direction, turn,number)