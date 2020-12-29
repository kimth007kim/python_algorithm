word= input()
result=0
for i in range(len(word)):
    a=ord(word[i])
    if a>=65 and a<=67:
        result+=3
    elif a>=68 and a<=70:
        result+=4
    elif a>=71 and a<=73:
        result+=5
    elif a>=74 and a<=76:
        result+=6
    elif a>=77 and a<=79:
        result+=7
    elif a>=80 and a<=83:
        result+=8
    elif a>=84 and a<=86:
        result+=9
    elif a>=87 and a<=90:
        result+=10
print(result)