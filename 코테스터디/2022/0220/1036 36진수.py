import sys

input= sys.stdin.readline

cand=[]
arr=[]
priority={}
dic={}
word = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(word)):
    dic[word[i]]=i

def convert_to_10(n):
    result = 0
    length=len(n)
    for idx,value in enumerate(n):
        result += 36**(length-1-idx)*dic[value]
    return result

def convert_to_36(n):
    q,r = divmod(n,36)
    if q==0:
        return word[r]
    return convert_to_36(q)+ word[r]
result=0
for _ in range(int(input())):
    tmp = input().rstrip()
    l = len(tmp)
    for j in range(len(tmp)):
        if tmp[j] not in priority:
            priority[tmp[j]]=(35-dic[tmp[j]])*36**(l-j-1)
        else:
            priority[tmp[j]]+=(35-dic[tmp[j]])*36**(l-j-1)
    result+=convert_to_10(tmp)
n= int(input())
if len(priority)<n:
    n=len(priority)
arr=[]
for i in priority:
    arr.append(priority[i])

arr.sort(reverse=True)
arr= arr[:n]
result+=sum(arr)
print(convert_to_36(result))