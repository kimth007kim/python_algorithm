from collections import deque
import sys


input =sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# nxn 공간의 필드
n= int(input())
# 초기 아기상어의 크기는 2



def min_distance(graph,shark,t_x,t_y):
    s_x=shark.x
    s_y=shark.y
    visited=[[False]*n for _ in range(n)]
    visited[s_x][s_y]=True
    s_size= shark.size
    q=deque()
    q.append([s_x,s_y,0])
    while q:
        x,y,cnt=q.popleft()
        if x==t_x and y==t_y:
            return cnt
        for i in range(4):
            nx= dx[i]+x
            ny= dy[i]+y
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
                if graph[nx][ny]<=s_size:
                    q.append([nx,ny,cnt+1])
                    visited[nx][ny]=True
    return -1

def find_distance(graph,shark):
    now_x=shark.x
    now_y=shark.y
    size= shark.size

    candidate=[]
    graph[now_x][now_y]=0

    for i in range(n):
        for j in range(n):
            if graph[i][j]!=0 and graph[i][j]!=9 and size>graph[i][j]:
                distance=min_distance(graph, shark, i, j)
                if distance!=-1:
                    candidate.append([distance,i,j])


    if len(candidate)==0:
        return -1
    else:
        candidate.sort(key = lambda x:(x[0],x[1],x[2]))

        nx,ny= candidate[0][1],candidate[0][2]
        graph[nx][ny]=0
        shark.x= nx
        shark.y= ny
        shark.eating()


        return candidate[0][0]
    # return 0




class Baby:
    def __init__(self,x,y):
        self.size= 2
        self.x= x
        self.y= y
        self.cnt=0
    def eating(self):
        self.cnt += 1
        if self.cnt==self.size:
            self.cnt=0
            self.size+=1

    def __str__(self):
        return "size 는 {} 이고 위치는 x={}, y= {}  ,먹은 물고기 마리수: {}입니다.".format(self.size,self.x,self.y,self.cnt)

time = 0


# 그래프 생성완료
graph=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    for j in range(n):
        if tmp[j]==9:
            # 상어객체 생성
            shark = Baby(i,j)
    graph.append(tmp)


while True:
    number =find_distance(graph,shark)
    if number==-1:
        break
    else:
        time+=number

print(time)