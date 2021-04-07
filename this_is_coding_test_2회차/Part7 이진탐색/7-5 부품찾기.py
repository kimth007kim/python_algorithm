# N개의 부품이있다. 고유한 번호가있다.
# M개 종류의 부품 대량구매

n= int(input())
nlist= list(map(int,input().split()))
nlen=len(nlist)
m= int(input())
mlist=list(map(int,input().split()))
answer=[]
def binary_search(target,start,end):
    while start<=end:
        mid = (start+end)//2

        if nlist[mid] ==target:
            return mid
        elif nlist[mid] >target:
            end= mid-1
        else:
            start=mid+1


for i in mlist:
    result=binary_search(i,0,nlen-1)
    if result==None:
        answer.append("no")
    else:
        answer.append("yes")

for j in answer:
    print(j,end=" ")