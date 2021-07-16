import sys
input=sys.stdin.readline()
def digit(n):
    # 자릿수와 그자릿수의 시작,끝값을 리턴하는 함수
    differ=0
    for i in range(0,10):
        big=9*(i+1)*(10**i)
        if differ<=n<=differ+big:
            return i,differ,differ+big
        else:
            differ+=big

n=int(input)
d,start,end=digit(n)
# print(d,start,end)

# print("&&&&&&&&&&&&&&",n-start-1)
NEWNUM= (10**d)+(n-start-1)//(d+1)
print(start)
# start+=1
# NEWNUM=start+(n-start+1)//d
# print(NEWNUM)
word=str(NEWNUM)
# print("답답답답답답답답답",word[(n-start-1)%d])
# if 1<=n<=9:
#     print(n)
# else:
#     print(word[(n-start-1)%(d+1)])
print(word[(n-start-1)%(d+1)])



# result=n-start
# print(d,start,end)
# s=""
# print("--------",n-start)
#
# while len(s)<result:
#     start += 1
#     s+=str(start)
# print(s)
# print(len(s))
# print(s[result-1])
