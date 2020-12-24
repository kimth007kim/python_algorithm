cnt = int(input())
hap=0
nindex =0
max = 0

newlist = []

nlist = list(map(float, input().split()))
for i in range(cnt):
    if nlist[i] > max:
        max = nlist[i]
        nindex= i

for i in range(cnt):
    newone = nlist[i]/max*100
    newlist.append(newone)

for i in range(cnt):
    hap += newlist[i]

print(hap/cnt)
