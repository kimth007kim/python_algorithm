s= int(input())

num=1
total=0
cnt=0

while True:
    total+=num
    cnt+=1
    num+=1
    if total==s:
        print(cnt)
        break
    elif total>s:
        print(cnt-1)
        break
    # print(num,total)