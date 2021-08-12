import sys
input = sys.stdin.readline

def reverse(word):
    answer=""
    length= len(word)
    arr=list(word)
    for i in range(length):
        answer+=arr.pop()
    return answer

n= int(input())
result=[]
for i in range(n):
    tmp=""
    word= list(map(str,input().split()))
    for i in range(len(word)):
        tmp += reverse(word[i])
        if i!= len(word)-1:
            tmp+=" "
    result.append(tmp)

for i in result:
    print(i)