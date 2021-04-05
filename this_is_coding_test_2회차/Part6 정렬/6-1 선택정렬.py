array= [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    FNUM = array[i]
    MNUM= max(array)
    for j in range(i+1,len(array)):
        if MNUM>array[j]:
            MNUM=array[j]
            index=j
    array[i],array[index]=MNUM,FNUM

print(array)
