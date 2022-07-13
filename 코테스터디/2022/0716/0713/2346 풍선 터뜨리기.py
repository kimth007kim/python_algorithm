from collections import deque

n=int(input())

arr= list(map(int,input().split()))
q= deque()
# print(arr)
for i in range(1,n+1):
    q.append([i,arr[i-1]])

answer=[]
while len(answer)<n:
    print("!!!!!!!!!!!",answer,q)
    num,val= q.popleft()
    # print(num,val)
    answer.append(num)
    if len(answer)==n:
        break
    if val>0:
        q.append([num,0])
        # print("===================",q)
        while q[0][1]==0:
            a,b = q.popleft()
            q.append([a,b])
        while val-1>0:
            nu,v = q.popleft()
            q.append([nu,v])
            # print(val,q)
            if v==0:
                continue
            val-=1
        while q[0][1]==0:
            a,b = q.popleft()
            q.append([a,b])
    else:
        q.appendleft([num,0])
        print("===================",q)
        while q[len(q)-1][1] == 0:
            a, b = q.pop()
            q.appendleft([a, b])
        # print("===================",q)
        while val<0:
            nu,v = q.pop()
            q.appendleft([nu,v])
            print("--",q)
            if v==0:
                continue
            val+=1


print(*answer)