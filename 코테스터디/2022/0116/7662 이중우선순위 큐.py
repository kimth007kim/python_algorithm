
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
        self.visited=[False]*200000

    def insert(self,number,id):
        heapq.heappush(self.min_heap,( number,id))
        heapq.heappush(self.max_heap, (-number,id))
        self.visited[id]=True

    def MaxValue(self):
        while self.max_heap and not self.visited[self.max_heap[0][1]]:
            # print("초기", self.max_heap[0])

            heapq.heappop(self.max_heap)
        if self.max_heap:
            self.visited[self.max_heap[0][1]]=False
            # print(self.max_heap[0])
            heapq.heappop(self.max_heap)

        # if len(self.min_heap) > 0:
        #     Maximum= heapq.heappop(self.max_heap)
        #     self.min_heap.remove(-Maximum)

    def MinValue(self):
        while self.min_heap and not self.visited[self.min_heap[0][1]]:
            # print("초기기", self.min_heap[0])
            heapq.heappop(self.min_heap)
        if self.min_heap:
            self.visited[self.min_heap[0][1]]=False
            # print(self.min_heap[0])
            heapq.heappop(self.min_heap)
        # if len(self.min_heap)>0:
        #     Minimum= heapq.heappop(self.min_heap)
        #     self.max_heap.remove(-Minimum)


    def finish(self):
        # if len(self.min_heap)==0:
        #     return "EMPTY"
        #
        # elif len(self.min_heap)==1:
        #     word= ""
        #     tmp=str(self.min_heap[0])
        #     word+=tmp+" "+tmp
        #     return word
        # else:
        #     tmpMX=-(self.max_heap[0])
        #     tmpMN=str(self.min_heap[0])
        #     word=""
        #     word+=str(tmpMX)+" "+tmpMN
        #     return word
        while self.min_heap and not self.visited[self.min_heap[0][1]]:
            heapq.heappop(self.min_heap)
        while self.max_heap and not self.visited[self.max_heap[0][1]]:
            heapq.heappop(self.max_heap)
        if self.min_heap and self.max_heap:
            result.append(str(-self.max_heap[0][0])+" "+str(self.min_heap[0][0]))
        else:
            result.append("EMPTY")
    def __str__(self):
        return "maxHeap= {} minHeap={}".format(self.max_heap,self.min_heap)

result=[]
for i in range(int(input())):
    h = Heap()
    for j in range(int(input())):
        cmd, number = map(str,input().split())
        if cmd =="I":
            h.insert(int(number),j)
            # print(h)
        elif cmd=="D":
            if number=="1":
                # print("최댓값")
                h.MaxValue()
                # print(h)
            else:
                # print("최솟값")
                h.MinValue()
                # print(h)
    h.finish()
for i in result:
    print(i)