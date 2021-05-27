import heapq

hq=[]
print(hq)
n=int(input())
while n!=-1:
    heapq.heappush(hq, n)
    print(hq)
    n = int(input())