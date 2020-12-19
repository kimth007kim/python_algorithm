a= int(input())
b= int(input())
if b >99 and b<1000:
    b1= b//100
    b2= (b- (b1*100)) //10
    b3= (b-(b1*100)-(b2*10))
else:
    print("에러")
digit1 = a*b3
print(digit1)
digit2 = a*b2
print(digit2)
digit3 = a*b1
print(digit3)
hap= digit1+(digit2*10)+(digit3*100)
print(hap)