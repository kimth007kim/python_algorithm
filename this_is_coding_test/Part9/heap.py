import heapq

# def heapsort(iterable):
#     h=[]
#     result=[]
#     for value in iterable:
#         heapq.heappush(h,value)
#         # print(heap)
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result
#
# result = heapsort([1,3,5,7,9,2,4,6,8])
# print(result)

testheap = [(1,3),(1,4),(2,2)]
# heapq.heappush(testheap, 3)
# heapq.heappush(testheap, 5)
# heapq.heappush(testheap, -3)
# heapq.heappush(testheap, 1)
heapq.heappop(testheap)
# heapq.heappop(testheap)
print(testheap)

