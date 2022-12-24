import sys,heapq

input =sys.stdin.readline

n= int(input())
q=[]

for i in range(n):
    s,e= map(int,input().split())
    q.append([s,e])

q.sort()

room=[]
heapq.heappush(room,q[0][1])


for i in range(1,n):
    if q[i][0]<room[0]:
        heapq.heappush(room,q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,q[i][1])
    print(room)
print(len(room))