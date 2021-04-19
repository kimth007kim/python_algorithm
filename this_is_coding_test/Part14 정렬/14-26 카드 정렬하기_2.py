import heapq

n= int(input())

heap=[]
for i in range(n):
    data=int(input())
    heapq.heappush(heap,data)

result=0
print(heap)

while len(heap)!=1:
    one=heapq.heappop(heap)
    two=heapq.heappop(heap)
    print(one,two)
    sum_value=one+two
    result+=sum_value
    heapq.heappush(heap,sum_value)

print(result)