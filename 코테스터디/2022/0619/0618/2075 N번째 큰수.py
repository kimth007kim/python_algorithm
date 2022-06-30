import sys
import heapq

input = sys.stdin.readline


n= int(input())
heap =[]

for i in range(n):
    nums = list(map(int,sys.stdin.readline().split()))

    if not heap:
        print("여기")
        for num in nums:
            heapq.heappush(heap,num)
            print(heap)

    else:
        for num in nums:
            if heap[0]<num:
                print("두번째",heap[0],num)
                heapq.heappush(heap,num)
                heapq.heappop(heap)
                print(heap)

print(heap[0])