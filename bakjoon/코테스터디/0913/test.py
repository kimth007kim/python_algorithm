arr=[ {1,2,3,4},{5,3,2,4},{4,2,3,1}]
data=[]

for i in arr:
    if i not in data:
        data.append(i)
        print(data)