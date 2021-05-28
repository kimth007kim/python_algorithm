n,m=map(int,input().split())
data=[]
temp=[[0]*m for i in range(n)]

for i in range(n):
    data.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]
max_score=0


def plague(x,y):
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                plague(nx,ny)
def score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

def dfs(cnt):
    global max_score
    if cnt==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]= data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    plague(i,j)
        max_score=max(max_score,score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j]=1
                cnt+=1
                dfs(cnt)
                data[i][j]=0
                cnt-=1

dfs(0)
print(max_score)