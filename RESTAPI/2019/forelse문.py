
a=[]
b=[1,2,3,4,5,6,7]

for i in a:
    print(i)
else:
    print("없다")

for i in b:
    if i == 4:
        print("4")
        break
else:
    print("else문 발동")