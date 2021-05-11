n=input()
nlen=len(n)//2
left  = n[:nlen]
right = n[nlen:]

sleft=0
sright=0
for i in left:
    sleft+=int(i)

for j in right:
    sright+=int(j)

if sleft == sright:
    print("LUCKY")
else:
    print("READY")