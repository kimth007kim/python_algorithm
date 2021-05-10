n,k=map(int,input().split())

cnt=0
c=0
def chicken(n,c,idx,cnt):
    if idx==0:
        # print(1)
        cnt+=1
        return cnt
    if c==k:
        # print(2)
        cnt+=1
        c=0
        chicken(n+1,c+1,idx-1,cnt+1)
    # print(cnt)
    chicken(n, c+1, idx-1, cnt+1)



print(chicken(n,c,n,cnt))