from collections import deque

a,b = map(int,input().split())
cand=["4","7"]
q= deque()
q.append("4")
q.append("7")
cnt=0
while q:
    now =q.popleft()
    if int(now)>b:
        continue
    if a<=int(now)<=b:
        cnt+=1

    for i in range(2):
        q.append(now+cand[i])

print(cnt)



    # print(now)