from collections import defaultdict
import sys


input = sys.stdin.readline
cnt=0


trees= defaultdict(int)
_set = set()
while True:
    tree =input().rstrip()
    if tree=="":
        break
    trees[tree]+=1
    cnt+=1
    _set.add(tree)

_list = list(_set)
_list.sort()

for i in _list:
    now=trees[i]/cnt*100
    print("%s %.4f"%(i,now))
