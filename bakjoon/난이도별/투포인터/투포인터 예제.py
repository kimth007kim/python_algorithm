n= 5
m= 5
data =[1,2,3,2,5]

count = 0
interval_sum=0
end= 0

for start in range(n):
    while interval_sum<m and end<n:
        print("end: ",end,"<",n ,"interval_sum:", interval_sum,"<",m)
        interval_sum+= data[end]
        end+=1
        print("바뀐값:", "interval_sum",interval_sum ,"end",end)


    # print("start:",start, "end:",end, "interval_sum:",interval_sum)
    if interval_sum == m:
        print("여기","start:", start, "end:", end, "interval_sum:", interval_sum)
        count+=1
    interval_sum-=data[start]
    print("start:", start, "end:", end, "interval_sum:", interval_sum)

print(count)