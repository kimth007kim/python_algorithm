from collections import deque
import sys

input =sys.stdin.readline
# n=접시수
# d= 초밥의 가짓수
# k= 연속해서 먹는 접시수
# c= 쿠폰번호

class Number:
    def __init__(self,target):
        self.dic={}
        self.LEN=0
        self.prev=deque()
        self.MAX=0
        self.target= target

    def delete(self):
        now = self.prev.popleft()
        if self.dic[now]==1:
            del self.dic[now]
        else:
            self.dic[now]-=1

    def count(self):
        self.LEN= len(self.dic)
        self.in_value()
        self.MAX=max(self.MAX,self.LEN)

    def append(self,n):
        if n in self.dic:
            self.dic[n]+=1
        else:
            self.dic[n]=1
        self.prev.append(n)
    def in_value(self):
        if self.target not in self.dic:
            self.LEN+=1

    def __str__(self):
        return "{} {} {} {} ".format(self.dic, self.prev,self.LEN,self.MAX)



n ,d,k,c= map(int,input().split())
store = []
diction =Number(c)
for i in range(n):
    store.append(int(input()))


store += store[:k-1]


for i in range(k):
    diction.append(store[i])
diction.count()

for i in range(k,n):
    diction.delete()
    diction.append(store[i])
    diction.count()
    # print(diction)
print(diction.MAX)