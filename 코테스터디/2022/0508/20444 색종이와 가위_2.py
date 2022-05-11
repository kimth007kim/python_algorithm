n,k = map(int,input().split())

def solution(lt,rt):
    print(lt,rt)
    while lt<rt:
        mid = (lt+rt)//2
        value = (mid+1)*(n-mid+1)
        print(mid,value)
        if value == k:
            print("YES")
            return
        if value>k:
            rt =mid -1
        else:
            lt= mid+1
    print("NO")
    return

solution(0,n)