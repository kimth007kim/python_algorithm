
# https://www.acmicpc.net/problem/7662
import heapq
import sys

input =sys.stdin.readline
# I n 정수 삽입연산
# D -1 최솟값 삭제 연산
# D 1 최댓값 삭제 연산

class Heap:
    def __init__(self):
        self.min_heap=[]
        self.max_heap=[]

    def insert(self,number):
        heapq.heappush(self.min_heap, number)
        heapq.heappush(self.max_heap, -number)

    def MaxValue(self):
        if len(self.min_heap) > 0:
            Maximum= heapq.heappop(self.max_heap)
            self.min_heap.remove(-Maximum)

    def MinValue(self):
        if len(self.min_heap)>0:
            Minimum= heapq.heappop(self.min_heap)
            self.max_heap.remove(-Minimum)

    def finish(self):
        if len(self.min_heap)==0:
            return "EMPTY"

        elif len(self.min_heap)==1:
            word= ""
            tmp=str(self.min_heap[0])
            word+=tmp+" "+tmp
            return word
        else:
            tmpMX=-(self.max_heap[0])
            tmpMN=str(self.min_heap[0])
            word=""
            word+=str(tmpMX)+" "+tmpMN
            return word

    def __str__(self):
        return "maxHeap= {} minHeap={}".format(self.max_heap,self.min_heap)

result=[]
for i in range(int(input())):
    h = Heap()
    for j in range(int(input())):
        cmd, number = map(str,input().split())
        if cmd =="I":
            h.insert(int(number))
        elif cmd=="D":
            if number=="1":
                h.MaxValue()
            else:
                h.MinValue()
    result.append(h.finish())

for i in result:
    print(i)