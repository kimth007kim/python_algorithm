from collections import deque

n= int(input())
k= int(input())
graph=[["X"]*n for _ in range(n)]
for i in range(k):
    x,y = map(int,input().split())
    graph[x][y]= "A"

dir=[]
narr=[]
com=int(input())
for i in range(com):
    num,c= map(str,input().split())
    dir.append(c)
    narr.append(int(num))
dx=[0,1,0,-1]
dy=[1,0,-1,0]
arr=narr[:]
for i in range(len(arr)-1,0,-1):
    arr[i]=narr[i]-narr[i-1]


def move(n):
    now=deque()
    now.append([0,0])
    d=0
    time=1
    for num in arr:
        while num>0:
            for i in range(len(now)):
                x,y = now.popleft()
                # 사과먹는경우 or 안먹는경우처리
                # 그래프 0으로그리기"
                if 0<=x<n and 0<=y<n:
                    if (0>x + dx[d] or 0>y + dy[d] or x + dx[d]>=n or y + dy[d]>=n ) or (graph[x + dx[d]][y + dy[d]]=="0"):
                        return time
                    if graph[x + dx[d]][y + dy[d]]=="A":
                        now.append([x,y])
                        graph[x][y] = "0"
                    else:
                        graph[x][y]="X"
                    now.append([x+dx[d],y+dy[d]])
                    graph[x + dx[d]][y + dy[d]] = "0"
                    # print("끝")
                    for i in graph:
                        print(i)
                    print(time)
                    print()
                    # 부딪히면 멈추는 함수
                else:
                    return time
            time+=1
            num-=1
        c=dir.pop(0)
        if c=="L":
            d=(4+d-1)%4
        elif c=="D":
            d=(4+d+1)%4
    while  0 <= x < n and 0 <= y < n:
        for i in range(len(now)):
            x, y = now.popleft()
            if (0 > x + dx[d] or 0 > y + dy[d] or x + dx[d] >= n or y + dy[d] >= n) or (graph[x + dx[d]][y + dy[d]] == "0"):
                return time
            if graph[x + dx[d]][y + dy[d]] == "A":
                now.append([x, y])
                graph[x][y] = "0"
            else:
                graph[x][y] = "X"
            now.append([x + dx[d], y + dy[d]])
            graph[x + dx[d]][y + dy[d]] = "0"
            time+=1
    return time
a=move(n)
print(a)