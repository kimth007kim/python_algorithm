from collections import deque
n,m= map(int,input().split())
graph = []
dx=[0,1,0,-1]
dy=[1,0,-1,0]

camera={}
camera[1]=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
camera[2]=[[1,0,1,0],[0,1,0,1]]
camera[3]=[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
camera[4]=[[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1]]
camera[5]=[[1,1,1,1]]

arr=[]
comb=[]
answer=[]
def copy(graph):
    copied= [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copied[i][j]= graph[i][j]
    return copied

def dfs(arr,cnt,tmp):
    global comb
    if cnt == len(arr):
        comb.append(tmp[:])
        return
    for i in range(len(camera[arr[cnt][0]])):
        tmp.append(i)
        dfs(arr,cnt+1,tmp)
        tmp.pop()
def count_blank(board):
    result=0
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                result+=1
    return result


def bfs(cand,arr,board):
    global answer
    q=deque()
    for i in range(len(arr)):
        direction=camera[arr[i][0]][cand[i]]
        for j in range(len(direction)):
            if direction[j] ==1:
                q.append([j,arr[i][1],arr[i][2]])
    while q:
        d,x,y = q.popleft()
        if board[x][y]==6:
            continue
        if board[x][y]==0:
            board[x][y]=9
        nx= dx[d]+x
        ny= dy[d]+y
        if 0<=nx<n and 0<=ny<m:
            q.append([d,nx,ny])
    return count_blank(board)


for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)
    for j in range(len(tmp)):
        if 1<=tmp[j]<=5:
            arr.append([tmp[j],i,j])
dfs(arr,0,[])

MIN= int(1e9)
for cand in comb:
    board=copy(graph)
    MIN= min(MIN,bfs(cand,arr,board))


print(MIN)