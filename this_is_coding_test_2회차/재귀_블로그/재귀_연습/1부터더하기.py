# n~1까지 출력
n=int(input())
def plus(num):
    if num==0:
        return
    else:
        print(num, end=" ")
        return plus(num-1)

tot=0
def sum(num,tot):
    if num==0:
        print(tot)
        return
    tot+=num
    return sum(num-1,tot)
plus(n)
sum(n,tot)
# 1~n 까지 합을 출력하는 함수