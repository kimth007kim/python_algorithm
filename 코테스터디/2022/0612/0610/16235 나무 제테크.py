from collections import deque

def spring(tree,land):
    for i in range(n):
        for j in range(n):
            if len(tree[i][j])!=0:
                tmp_arr= []
                score = land[i][j]
                tree[i][j].sort(reverse=True)
                while score>0 and len(tree[i][j])>0:
                    now= tree[i][j][-1]
                    if score<now:
                        break
                    tree[i][j].pop()
                    score-=now
                    tmp_arr.append(now+1)
                land[i][j]=score
                for k in tree[i][j]:
                    land[i][j]+=k//2
                tree[i][j]=tmp_arr

# 2. 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
# 소수점 아래는 버린다.

# 3. 가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 어떤 칸 (r, c)와 인접한 칸은
# (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
# 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.



def fall(tree):
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,+1,-1,1,-1,0,1]
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) != 0:
                for k in tree[i][j]:
                    if k % 5==0:
                        for l in range(8):
                            nx= dx[l]+i
                            ny=dy[l]+j
                            if 0<=nx<n and 0<=ny<n:
                                tree[nx][ny].append(1)
# 4. 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

def winter(land,robot):
    for i in range(n):
        for j in range(n):
            land[i][j]+=robot[i][j]


def season():
    spring(tree,land)
    fall(tree)
    winter(land,robot)

# n *n 배열  k년후 살아있냐
n,m,k= map(int,input().split())
tree=[[[] for _ in range(n)] for _ in range(n)]
land=[[5]*n for _ in range(n)]
robot =[]
for i in range(n):
    tmp = list(map(int,input().split()))
    robot.append(tmp)

for i in range(m):
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)

for i in range(k):
    season()
cnt=0
for i in range(n):
    for j in range(n):
        cnt+=len(tree[i][j])

print(cnt)