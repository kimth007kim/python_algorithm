data=input()
x=ord(data[0])-96
y=int(data[1])
cnt=0
dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]

for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<1 or nx>8 or ny<1 or ny>8:
        continue
    cnt += 1

print(cnt)