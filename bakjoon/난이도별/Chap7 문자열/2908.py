a,b =map(int,input().split())

a1= a // 100
a2= (a- a1*100)//10
a3= (a-a1*100-a2*10)

newa= a3*100+a2*10+a1

b1= b // 100
b2= (b- b1*100)//10
b3= (b-b1*100-b2*10)

newb= b3*100+b2*10+b1

if newa > newb:
    print(newa)
elif newb> newa:
    print(newb)