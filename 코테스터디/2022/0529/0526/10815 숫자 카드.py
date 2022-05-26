def binary_search(have,target):
    start= 0
    end= len(have)-1
    while start<=end and end<=len(have):

        mid = (start+end)//2
        if have[mid]==target:
            return 1
        elif have[mid]<target:
            start=mid+1
        else:
            end= mid-1
    return 0


n=int(input())
have= list(map(int,input().split()))
m=int(input())
cand= list(map(int,input().split()))

have.sort()

answer=[]
for i in cand:
    answer.append(binary_search(have,i))

print(*answer)
