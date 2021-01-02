n= int(input())
cnt = 0
while n>=0 :
    if n % 5 ==0:
        n = n//5
        cnt +=n
        print(cnt)
        break
    n-=3
    cnt+=1
    # print(n)
else:
    print("-1")