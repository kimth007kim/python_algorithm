n=int(input())
number=[2,3,5]
array=[]
array.append(1)
prev=1
i=2
while prev<n:
    if i%2==0 or i%3==0 or i%5==0:
        array.append(i)
        prev+=1
    i+=1

print(array)
print(array[n-1])