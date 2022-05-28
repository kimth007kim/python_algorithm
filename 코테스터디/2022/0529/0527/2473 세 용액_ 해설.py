import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer=[0,0,0]
MIN = 0

tmp = int(1e11)
for i in range(n - 2):
    if i>0 and arr[i]==arr[i-1]:
        continue
    left,right=i+1,n-1

    while left<right:
        sum= arr[i]+arr[left]+arr[right]
        if abs(sum)<abs(tmp):
            answer[0] = arr[i]
            answer[1] = arr[left]
            answer[2] = arr[right]
            tmp = sum

        if sum<0:
            left+=1
        elif sum>0:
            right-=1
        else:
            print(arr[i],arr[left],arr[right])
            sys.exit(0)

answer.sort()
print(*answer)