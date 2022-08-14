import sys
from collections import defaultdict


input = sys.stdin.readline

def time_to_int(time):
    total=0
    hr,mm = time.split(":")
    total+=int(hr)*60+int(mm)
    return total


s,e,q =map(str,input().rstrip().split())
start=time_to_int(s)
end=time_to_int(e)
quit=time_to_int(q)
student= defaultdict(set)


while True:
    now = input().rstrip()
    if now =="":
        break
    t,name=map(str,now.split())
    time= time_to_int(t)
    if time>quit:
        break
    if time<=start:
        student[name].add(0)
    if time>=end:
        student[name].add(1)

answer=0
for i in student:
    if len(student[i])==2:
        answer+=1

print(answer)