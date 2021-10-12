def solution(grid):
    d=[[-1, 0],[1 ,0] ,[0 ,1] ,[0 ,-1 ]]
    right = {0:3,1:2 ,2 :0 ,3 :1 }
    left = {0: 2, 1:3, 2: 1, 3: 0}

    answer = []

    w,h = len(grid[0]),len(grid)

    visited=[[[1 ] *4 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            for n in range(4):
                if not visited[i][j][n]:
                    continue
                cnt=0
                ty,tx,ti =i ,j,n
                while True:
                    visited[ty][tx][ti]-=1
                    print(visited)
                    cnt+=1
                    now =grid[ ty][tx]
                    if now=='L' :
                        ti=left [ ti]
                    elif now =="R":
                        ti =right [ti]
                    tx,ty = (tx+d[ti] [ 1])%w , ( ty+d[ti ] [0])%h
                    if tx == i and ty == j and ti ==n:
                        break
                answer.append(cnt)
    answer.sort()
    return answer

    return answer