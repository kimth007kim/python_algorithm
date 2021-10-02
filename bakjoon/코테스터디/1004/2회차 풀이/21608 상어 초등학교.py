import sys

input=sys.stdin.readline

n=int(input())


arr=[[0]*n for _ in range(n)]
likedict={}
dx= [-1,0,1,0]
dy=[0,-1,0,1]

for _ in range(n*n):
    tmp= list(map(int,input().split()))
    likedict[tmp[0]]=tmp[1:]
    maxLike=-1
    maxEmpty=-1
    maxX=0
    maxY=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                likeCnt=0
                emptyCnt=0
                for k in range(4):
                    nx=dx[k]+i
                    ny=dy[k]+j
                    if 0<= nx < n and 0<=ny<n:
                        if arr[nx][ny]==0:
                            emptyCnt+=1
                        elif arr[nx][ny] in tmp:
                            likeCnt+=1
                if maxLike<likeCnt or (maxLike == likeCnt and emptyCnt>maxEmpty):
                    maxX=i
                    maxY=j
                    maxLike= likeCnt
                    maxEmpty= emptyCnt
    arr[maxX][maxY]=tmp[0]
score= 0
for i in range(n):
    for j in range(n):
        cnt=0
        number=arr[i][j]
        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in  likedict[number]:
                    cnt+=1
        if cnt ==0:
            score+=0
        else:
            score+= 10**(cnt-1)

print(score)