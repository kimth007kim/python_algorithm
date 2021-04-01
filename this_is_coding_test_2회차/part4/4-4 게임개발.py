n,m=map(int,input().split())
a,b,d=map(int,input().split())

dx=[-1,0,1,0]
dy=[0,1,0,-1]

direct=['n','e','s','w']

field=[]
for i in range(n):
    field.append(list(map(int,input().split())))
field[a][b]=2
visited=1

while True:
    if d==0:
        d=3
    else:
        d=d-1
    nx=a+ dx[d]
    ny=b+ dy[d]
    print(nx,ny)
    if (field[a-1][b]==1 or field[a-1][b]==2) and (field[a][b-1]==1 or field[a][b-1]==2) and (field[a+1][b]==1 or field[a+1][b]==2) and (field[a][b+1]==1 or field[a][b+1]==2):
        nx,ny= a+dx[(d+2)%4], b+dy[(d+2)%4]
        if field[nx][ny]==1:
            break
        else:
            a,b=nx,ny
            continue

    if field[nx][ny]==0:
        a,b= nx,ny
        field[a][b] = 2
        visited+=1

    elif field[nx][ny]==1:
        if d==0:
            d=3
        else:
            d-=1

print(visited)