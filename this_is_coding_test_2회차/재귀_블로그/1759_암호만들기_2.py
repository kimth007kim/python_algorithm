# L,C=map(int,input().split())
# temp=list(map(str,input().split()))

L,C=4,6
alpha=["a","t" ,"c", "i", "s" ,"w"]
all_out=[]
out=[]

alpha.sort()

def solve(depth,idx,L,C):
    if depth==L:
        all_out.append(''.join(map(str,out)))
        return
    for i in range(idx,C):
        out.append(alpha[i])
        solve(depth+1,i+1,L,C)
        out.pop()



solve(0,0,L,C)
print(all_out)

# https://wlstyql.tistory.com/71
# https://www.acmicpc.net/problem/1759