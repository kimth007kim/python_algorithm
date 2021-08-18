data= list(map(str,input()))
length = len(data)
left = data[:length//2]
right = data[length//2:]
l=0
for i in left:
    l+=int(i)
r= 0
for i in right:
    r+=int(i)
print(l,r)
if l==r:
    print("LUCKY")
else:
    print("READY")