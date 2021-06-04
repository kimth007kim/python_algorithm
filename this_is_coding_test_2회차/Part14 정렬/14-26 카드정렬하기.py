import heapq

n= int(input())
q=[]
for i in range(n):
    heapq.heappush(q,int(input()))

result=0
while len(q)!=1:
    one = heapq.heappop(q)
    two = heapq.heappop(q)

    summary=one+two
    result+=summary
    heapq.heappush(q,summary)

print(result)