from collections import deque



row,column,m = map(int,input().split())
dx=[1,0,-1,0]
dy=[0,1,0,-1]
score=0

def shark_catch(now,shark):
    global score
    result = deque()
    same= deque()
    MIN=1e9
    while shark:
        r, c, s, d, z = shark.popleft()
        if c==now:
            if MIN>r:
                MIN=r
            same.append([r,c,s,d,z])
        else:
            result.append([r,c,s,d,z])
    while same:
        r, c, s, d, z = same.popleft()
        if MIN!= r:
            result.append([r,c,s,d,z])
        else:
            score+=z
    return result


def shark_move(shark):
    tmp = deque()
    dic={}
    result=[]
    while shark:
        r,c,s,d,z= shark.popleft()
        for i in range(s):
            nx=r+dx[d]
            ny=c+dy[d]
            # print(nx,ny)
            if nx<1 or ny<1 or nx>row or ny>column:
                d= (d+2)%4
                nx = r + dx[d]
                ny = c + dy[d]
            r,c= nx,ny
        word = str(r)+"_"+str(c)
        if word not in dic:
            dic[word]=[[r,c,s,d,z]]
        else:
            dic[word].append([r,c,s,d,z])
    for i in dic:
        dic[i].sort(key = lambda x:(-x[4]))
        tmp.append(dic[i][0])
    return tmp

shark = deque()
for i in range(m):
    r1,c1,s,d,z=map(int,input().split())
    if d==1:
        d=0
    elif d==2:
        d=2
    elif d==3:
        d=1
    else:
        d=3
    shark.append([r1,c1,s,d,z])

for now in range(1,column+1):
    shark = shark_catch(now,shark)
    print(shark)
    shark=shark_move(shark)
    print(shark)
print(score)
