from collections import defaultdict
import sys
input = sys.stdin.readline
dic= defaultdict(int)
treeSet= set()
total_cnt=0
while True:
    tree = input().rstrip()
    if tree=="":
        break
    dic[tree]+=1
    treeSet.add(tree)
    total_cnt+=1
arr= list(treeSet)
arr.sort()


for i in arr:
    a=dic[i]/total_cnt*100
    print("%s %.4f"%(i,a))
