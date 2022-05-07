import sys

input = sys.stdin.readline
n= int(input())
word_dict={}
idx_dict={}
MAX=0
def find():
    for i in word_dict:
        if len(i)==MAX and len(word_dict[i])>1:
            temp=[]
            for j in word_dict[i]:
                temp.append([idx_dict[j],j])
            temp.sort(key = lambda x:x[0])
            return temp[0][1],temp[1][1]
    arr=[]
    for i in idx_dict:
        if len(arr)==2:
            break
        arr.append(i)
    return arr[0],arr[1]
for i in range(n):
    word= input().rstrip()
    idx_dict[word]=i
    for j in range(1,len(word)+1):
        tmp = word[:j]
        if tmp not in word_dict:
            word_dict[tmp]=[word]
        else:
            word_dict[tmp].append(word)
            if len(word_dict[tmp])>=2 and len(tmp)>MAX:
                MAX=len(tmp)
#
a,b= find()
print(a,b)
            # a,b= temp[0][]
            # return temp[:2]