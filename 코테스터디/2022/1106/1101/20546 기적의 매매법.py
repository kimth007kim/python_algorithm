def joon():
    remain = total
    cnt=0
    for i in chart:
        if i <= remain:
            cnt = remain//i
            remain=remain%i
            break
    return cnt*chart[-1]+remain

def sung():
    money = total
    purchase=0
    cnt=0
    for i in range(1,len(chart)):
        if chart[i]>chart[i-1]:
            if cnt>=4:
                cnt==4
                # continue
            elif cnt<=0:
                cnt=2
            else:
                cnt+=1
        elif chart[i]<chart[i-1]:
            if cnt<=-4:
                # continue
                cnt==-4
            elif cnt>=0:
                cnt=-2
            else:
                cnt-=1
        # print(chart[i-1],chart[i],cnt, i+1,"일")

        if cnt==4:
            if purchase>=1:
                # print("판매" ,i+1,"일")
                money+=purchase*chart[i]
                purchase=0
        elif cnt==-4:
            if money>=chart[i]:
                # print("구매" ,i+1,"일")
                purchase+=money//chart[i]
                money= money%chart[i]
        # print(purchase,money, i+1,"일")
    # if purchase==0:
    #     return
    return purchase*chart[-1]+money



total = int(input())
chart = list(map(int,input().split()))

j=joon()
s=sung()
# print(j,s)
if j==s:
    print("SAMESAME")
elif j>s:
    print("BNP")
else:
    print("TIMING")