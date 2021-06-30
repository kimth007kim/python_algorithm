number=int(input())
n=int(input())

answer=""

while number >=1 :
    remain = number%n
    print(remain)
    number //=n
    answer =str(remain)+answer

print(answer)