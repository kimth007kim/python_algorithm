import re
result=[]
html=input()
start=0
end=0
arr=re.split('<main>|<div>|<p>|</div>|</main>|]',html)

for i in arr:
    if i!="":
        if len(i)>12 and i[:11]=="<div title=":
            word="title : "+i[12:-2]
            result.append(word)
        else:
            prev=""
            tmp=""
            flag=False
            for idx,val in enumerate(i):
                if val == "<":
                    flag=True
                elif val==">":
                    flag=False
                else:
                    if flag==False:
                        tmp+=val
                prev= val
            if len(tmp)>=1:
                rem=len(tmp)-1
                for i in range(len(tmp)-1,-1,-1):
                    if tmp[i]!=" ":
                        break
                    else:
                        rem=i
                tmp= tmp[:rem+1]
                if tmp[0]==" ":
                    rem=0
                    for i in range(len(tmp)):
                        if tmp[i]!=" ":
                            break
                        else:
                            rem=i
                    tmp=tmp[rem+1:]
                if len(tmp)>=2:
                    answer=tmp[0]
                    prev=tmp[0]
                    blank=0
                    for i in range(1,len(tmp)):
                        if tmp[i]!=" ":
                            if blank==0:
                                answer+=tmp[i]
                            if blank==1:
                                answer+=" "+tmp[i]
                                blank=0
                        else:
                            if blank==0:
                                blank=1
                        prev=tmp[i]
                    result.append(answer)
                else:
                    result.append(tmp)
            else:
                result.append(tmp)

for i in result:
    print(i)