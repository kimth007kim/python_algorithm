import sys

input =sys.stdin.readline
def check(x,y,n,flag):
    MAX=0
    for i in range(n):
        previous=""
        count=0
        for j in range(n):
            if previous==data[i][j]:
                count+=1
            else:
                previous=data[i][j]
                count=1
            MAX=max(count,MAX)
    for i in range(n):
        previous=""
        count=0
        for j in range(n):
            if previous == data[j][i]:
                count += 1
            else:
                previous = data[j][i]
                count = 1
            MAX = max(count, MAX)
    return MAX

def solution(n,data):
    # if not linChecker(n,data):
    #     return n
    answer=1
    for i in range(n):
        for j in range(n-1):
            tmp1= data[i][j]
            tmp2= data[i][j+1]
            if tmp1!= tmp2:
                data[i][j],data[i][j+1]=tmp2,tmp1
                check(i, j, n, 0)
                answer= max(answer,check(i,j,n,0))
                data[i][j], data[i][j + 1] = tmp1, tmp2
    for i in range(n):
        for j in range(n-1):
            tmp1= data[j][i]
            tmp2= data[j+1][i]
            if tmp1!=tmp2:
                data[j][i],data[j+1][i]=tmp2,tmp1
                check(j,i,n,1)
                answer= max(answer,check(j,i,n,1))
                data[j][i], data[j + 1][i] = tmp1, tmp2
    return answer




n=int(input())
data=[]
for i in range(n):
    data.append(list(input().strip()))
# n = 5
# data=[['Y', 'C', 'P', 'Z', 'Y'], ['C', 'Y', 'Z', 'Z', 'P'], ['C', 'C', 'P', 'P', 'P'], ['Y', 'C', 'Y', 'Z', 'C'], ['C', 'P', 'P', 'Z', 'Z']]
# data = [['Y', 'Y', 'Y', 'Y', 'Y'], ['C', 'Y', 'Z', 'Z', 'P'], ['C', 'C', 'P', 'P', 'P'], ['Y', 'C', 'Y', 'Z', 'C'],['C', 'P', 'P', 'Z', 'Z']]


print(solution(n,data))