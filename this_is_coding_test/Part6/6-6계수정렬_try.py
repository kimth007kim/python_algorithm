array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
print(max(array))

visit= [0]*(max(array)+1)
print(visit)
for j in range(len(array)):
    for k in range(len(visit)):
        if array[j]== k:
            visit[k]+=1

for e in range(len(visit)):
    for d in range(visit[e]):
        print(e,end=" ")