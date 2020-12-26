end= int(input())
a=0
nlist=[]

while True:
    if a<100:
        if a !=0:
            nlist.append(a)

    elif a>=100:
        n1= a//100
        n2= (a-n1*100)//10
        n3= (a-n1*100-n2*10)
        for i in range(0,5):
            if n1+i == n2 and n2+i == n3:
                nlist.append(a)
            elif n1-i== n2 and n2-i == n3:
                nlist.append(a)
    a+=1
    if a == end+1:
        break
print(len(nlist))