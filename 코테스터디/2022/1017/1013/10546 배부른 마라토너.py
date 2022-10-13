import sys

input =sys.stdin.readline

n= int(input())
dic = {}
while True:
    name= input().rstrip()
    if len(name)==0:
        break
    if name in dic:
        del dic[name]
    else:
        dic[name]=1

for i in dic:
    print(i)