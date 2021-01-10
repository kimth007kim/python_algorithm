# 시간 51분까지

size= int(input())
data= map(str,input().split())

x=1
y=1

dx =[-1,1,0,0]
dy =[0,0,-1,1]
moving= ["L","R","U","D"]

for datas in data:
    for i in range(4):
        if datas == moving[i]:
            nx = x+dx[i]
            ny = y+dy[i]
            print("nx",nx)
            print("ny",ny)
            if nx >=1 and nx <= size and ny >=1 and ny<= size:
                x=nx
                y=ny
print(y,x)