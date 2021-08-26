
import sys
from itertools import combinations

input = sys.stdin.readline
data=[]
for i in range(9):
    data.append(int(input()))

def find():
    comb =combinations(data,7)
    for i in list(comb):
        total= 0
        for j in i:
            total+=j
        if total==100:
            return list(i)
dwarf =find()
dwarf.sort()
for i in dwarf:
    print(i)