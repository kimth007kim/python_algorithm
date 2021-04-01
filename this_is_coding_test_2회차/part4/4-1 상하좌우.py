n= int(input())
direction= list(map(str,input().split()))
x,y=1,1

for i in range(len(direction)):
    p= direction.pop(0)
    nx,ny=0,0
    if p == "R":
        nx=1
    if p == "L":
        nx=-1
    if p == "D":
        ny=1
    if p == "U":
        ny=-1
    if nx+x<=0 or nx+x>n or ny+y<=0 or ny+y>n:
        continue
    else:
        x+=nx
        y+=ny

    print(y,x)