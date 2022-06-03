n= int(input())
arr = []
SET= set()
for i in range(n):
    num= int(input())
    SET.add(num)
    arr.append(num)

MAX=0
for s in SET:
    now=0
    cnt=0
    for i in range(len(arr)):
        if s == arr[i]:
            continue
        if now !=arr[i]:
            now=arr[i]
            cnt=1
        else:
            cnt+=1

        MAX=max(cnt,MAX)

print(MAX)