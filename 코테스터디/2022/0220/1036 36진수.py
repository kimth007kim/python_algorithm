cand=[]
priority={}
arr=[]

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


for _ in range(int(input())):
    tmp = input()
    arr.append(tmp)
    l = len(tmp)
    for j in range(len(tmp)):
        if tmp[j] not in priority:
            priority[tmp[j]]=36**(l-j)
        else:
            priority[tmp[j]]+=36**(l-j)
dic={}
word = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(word)):
    dic[word[i]]=i


cand =[]
for i in priority:
    cand.append([priority[i],dic[i],i])

cand.sort(key= lambda x:(-x[0],x[1]))
print(cand)
num=int(input())
if len(cand)<num:
    num= len(cand)
total = []
for i in range(num):
    total.append(cand[i][2])
print(total)

array=[]
for i in range(len(arr)):
    temp=""
    for j in range(len(arr[i])):
        if arr[i][j] in total:
            temp+="Z"
        else:
            temp+=arr[i][j]
    array.append(temp)

answer=0

for i in array:
    tmp=convert_to_10(i)
    answer+=tmp

print(convert_to_36(answer))