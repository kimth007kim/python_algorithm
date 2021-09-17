n=5

data = [10,20,30,40,50]

sum_value=0
prefix_sum=[0]
for i in data:
    sum_value+=i
    prefix_sum.append(sum_value)
    print(sum_value,prefix_sum)

left,right= map(int,input().split())
print(prefix_sum[right]-prefix_sum[left-1])

