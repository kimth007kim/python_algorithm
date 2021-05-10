L,C=map(int,input().split())
data=list(map(str,input().split()))

data.sort()
print(data)

all_out=[]
out=[]

def solution(depth,idx,L,C):
    if depth==L:
        all_out.append(''.join(map(str,out)))
        return
    for i in range(idx,C):
        out.append(data[i])
        solution(depth+1,i+1,L,C)
        out.pop()

def check(array):
    for i in array:
        ja=0
        mo=0
        for k in i:
            if k in 'aeiou':
                mo+=1
            else:
                ja+=1
        if ja>=2 and mo>=1:
            print(i)
solution(0,0,L,C)
check(all_out)