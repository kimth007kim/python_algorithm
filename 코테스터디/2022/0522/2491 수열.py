n= int(input())
arr = list(map(int,input().split()))


# prev= 1
if n==1:
    print(1)
else:
    MAX=0
    in_prev= 1
    de_prev=1
    for i in range(2,n+1):
        if arr[i-2]>=arr[i-1]:
            de_prev += 1
        else:
            de_prev=1
        if arr[i-2]<=arr[i-1]:
            in_prev+=1
        else:
            in_prev=1
        MAX= max(de_prev,in_prev,MAX)
    print(MAX)