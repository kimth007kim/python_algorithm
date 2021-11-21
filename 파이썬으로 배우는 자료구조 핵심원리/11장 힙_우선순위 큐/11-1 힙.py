class Element:
    def __init__(self,key):
        self.key = key


class MaxHeap:
    MAX_ELEMENTS = 100
    def __init__(self):
        self.arr=[None for i in range(self.MAX_ELEMENTS+1)]
        self.heapsize=0

    def is_empty(self):
        if self.heapsize==0:
            return True
        return False

    def is_full(self):
        if self.heapsize>= self.MAX_ELEMENTS:
            return True
        return False

    def parent(self,idx):
        return idx >>1

    def left(self,idx):
        return idx<<1

    def right(self,idx):
        return(idx<<1)+1

    def push(self,item):
        if self.is_full():
            raise IndexError("the heap is full!!")
        self.heapsize+=1
        cur_idx = self.heapsize

        while cur_idx !=1 and item.key>self.arr[self.parent(cur_idx)].key:
            self.arr[cur_idx]=self.arr[self.parent(cur_idx)]
            cur_idx= self.parent(cur_idx)
        self.arr[cur_idx]=item

    def pop(self):
        if self.is_empty():
            return None

        rem_elem= self.arr[1]

        temp= self.arr[self.heapsize]
        self.heapsize-=1

        cur_idx =1

        child =self.left(cur_idx)

        while child <=self.heapsize:
            if child <self.heapsize and self.arr[self.left(cur_idx)].key< self.arr[self.right(cur_idx)].key:
                child =self.right(cur_idx)

            if temp.key>=self.arr[child].key:
                break

            self.arr[cur_idx]=self.arr[child]
            cur_idx=child
            child=self.left(cur_idx)
        self.arr[cur_idx]=temp

        return rem_elem

def print_heap(h):
    for i in range(1,h.heapsize+1):
        print("{}".format(h.arr[i].key),end="  ")
    print()

if __name__ == "__main__":
    h= MaxHeap()

    h.push(Element(2))
    h.push(Element(14))
    h.push(Element(9))
    print_heap(h)
    h.push(Element(11))
    h.push(Element(6))
    print_heap(h)
    h.push(Element(8))

    while not h.is_empty():
        rem= h.pop()
        print(f"poped item is{rem.key}")
        print_heap(h)

    print_heap(h)