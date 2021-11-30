from heapq import heappush,heappop

class Element:
    def __init__(self,key,string):
        self.key =key
        self.data= string

class MinPriorityQueue:
    def __init__(self):
        self.heap=[]

    def is_empty(self):
        if not self.heap:
            return True
        return False

    def push(self,item):
        heappush(self.heap(item.key,item.data))

    def pop(self):
        return heappop(self.heap)

    def min(self):
        return self.heap[0]