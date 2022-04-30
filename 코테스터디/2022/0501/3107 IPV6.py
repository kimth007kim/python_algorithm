def decompression(n):
    temp=":0000"
    result ="0000"
    for i in range(n-1):
        result+=temp
    return result



address= input()
length = len(address)
target=39
prev = ""
count=0
double=[]
for idx,now in enumerate(address):
    if now ==":":
        count+=1
        if prev ==":":
            double.append([idx-1,idx])
    prev= now

if len(double)!=0:
    if double[0][0]==0 and double[0][1]==length-1:
       word ="0000:0000:0000:0000:0000:0000:0000:0000"
    elif double[0][0]==0:
        word = decompression(9-count)+address[double[0][1]:]
    elif double[0][1]==length-1:
        word =address[:double[0][0]+1]+decompression(9-count)
    else:
        word = address[:double[0][0] + 1] + decompression(8 - count) + address[double[0][1]:]
else:
    word =address

if len(word)!=target:
    arr= word.split(":")
    for i in range(len(arr)):
        if len(arr[i])!=4:
            temp=arr[i]
            temp_length=len(temp)
            result=""
            result+="0"*(4-temp_length)+temp
            arr[i]=result

    print(":".join(arr))
else:
    print(word)

# tmp = 0
# for i in word:
#     if i==":":
#         tmp+=1
# print(tmp)