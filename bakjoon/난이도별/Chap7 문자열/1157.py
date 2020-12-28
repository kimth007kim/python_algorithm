word =input()
wlist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
max = 0
cnt =0
index=0
for i in range(len(word)):
    if word[i]== 'a' or word[i]=='A':
        wlist[0]+=1
    elif word[i]== 'b' or word[i]=='B':
        wlist[1]+=1
    elif word[i]== 'c' or word[i]=='C':
        wlist[2]+=1
    elif word[i]== 'd' or word[i]=='D':
        wlist[3]+=1
    elif word[i]== 'e' or word[i]=='E':
        wlist[4]+=1
    elif word[i]== 'f' or word[i]=='F':
        wlist[5]+=1
    elif word[i]== 'g' or word[i]=='G':
        wlist[6]+=1
    elif word[i]== 'h' or word[i]=='H':
        wlist[7]+=1
    elif word[i]== 'i' or word[i]=='I':
        wlist[8]+=1
    elif word[i]== 'j' or word[i]=='J':
        wlist[9]+=1
    elif word[i]== 'k' or word[i]=='K':
        wlist[10]+=1
    elif word[i]== 'l' or word[i]=='L':
        wlist[11]+=1
    elif word[i]== 'm' or word[i]=='M':
        wlist[12]+=1
    elif word[i]== 'n' or word[i]=='N':
        wlist[13]+=1
    elif word[i]== 'o' or word[i]=='O':
        wlist[14]+=1
    elif word[i]== 'p' or word[i]=='P':
        wlist[15]+=1
    elif word[i]== 'q' or word[i]=='Q':
        wlist[16]+=1
    elif word[i]== 'r' or word[i]=='R':
        wlist[17]+=1
    elif word[i]== 's' or word[i]=='S':
        wlist[18]+=1
    elif word[i]== 't' or word[i]=='T':
        wlist[19]+=1
    elif word[i]== 'u' or word[i]=='U':
        wlist[20]+=1
    elif word[i]== 'v' or word[i]=='V':
        wlist[21]+=1
    elif word[i]== 'w' or word[i]=='W':
        wlist[22]+=1
    elif word[i]== 'x' or word[i]=='X':
        wlist[23]+=1
    elif word[i]== 'y' or word[i]=='Y':
        wlist[24]+=1
    elif word[i]== 'z' or word[i]=='Z':
        wlist[25]+=1

for i in range(26):
    if max< wlist[i]:
        max= wlist[i]

for i in range(26):
    if wlist[i]==max:
        cnt+=1
        index = i
if cnt == 1:
    if index==0:
        print("A")
    elif index==1:
        print("B")
    elif index==2:
        print("C")
    elif index==3:
        print("D")
    elif index==4:
        print("E")
    elif index==5:
        print("F")
    elif index==6:
        print("G")
    elif index==7:
        print("H")
    elif index==8:
        print("I")
    elif index==9:
        print("J")
    elif index==10:
        print("K")
    elif index==11:
        print("L")
    elif index==12:
        print("M")
    elif index==13:
        print("N")
    elif index==14:
        print("O")
    elif index==15:
        print("P")
    elif index==16:
        print("Q")
    elif index==17:
        print("R")
    elif index==18:
        print("S")
    elif index==19:
        print("T")
    elif index==20:
        print("U")
    elif index==21:
        print("V")
    elif index==22:
        print("W")
    elif index==23:
        print("X")
    elif index==24:
        print("Y")
    elif index==25:
        print("Z")
else:
    print("?")