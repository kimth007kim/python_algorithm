n,m= map(int,input().split())
duk= list(map(int,input().split()))

duk.sort()
# 적어도 떡을 M만큼은 가져갈수있도록 해야한다. n은 떡 개수 len(duk)


def binary(target,start,end):
    result=0
    while start<=end:
        mid = (start+end)//2
        # print(mid)
        answer=0
        for i in range(n):
            if duk[i]-mid >0:
                answer+=duk[i]-mid
        # print(answer)
        if answer == m:
            return mid
        elif answer > m:
            result=mid
            start=mid+1
        else:
            end=mid-1
        # print(start,"    ",end,"   ",mid)
    return result
print(binary(m,0,duk[n-1]))
