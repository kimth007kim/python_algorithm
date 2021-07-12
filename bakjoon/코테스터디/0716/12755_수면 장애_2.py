import sys
input=sys.stdin.readline()
def digit(n):
    # 자릿수와 그자릿수의 시작,끝값을 리턴하는 함수
    differ=0
    for i in range(0,10):
        big=9*(i+1)*(10**i)
        # print(differ,"   ",n," ",differ+big)
        if differ<=n<=differ+big:
            return i,differ,differ+big
        else:
            differ+=big
        # if 9*(10**i)<n<9*(10**(i+1)):
        #     return i+2

n=int(input)
d,start,end=digit(n)
result=n-start
# print(d,start,end)
s=""
# print("--------",n-start)
while len(s)<result:
    start += 1
    s+=str(start)
# print(s)
# print(len(s))
print(s[result-1])
# a=""
# cnt=0
# number=1
# while cnt<=98:
#     a+=str(number)
#     # print(a)
#     cnt+=1
#     number+=1
# print(a)
# print(len(a))