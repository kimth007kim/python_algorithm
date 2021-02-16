a= [1,2,3]
b=[2,4,6,14]
c=[2,4,8,16]

def Quiz(arr):
    while len(arr)!=1:
        a=arr.pop()
        b=arr.pop()
        c=gcd(a,b)
        print("a",a,"b",b,"c",c)
        arr.insert(0,int(a*b/c))
        print(arr)
    answer=arr[0]
    return answer


def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while b>0:
        print("gcd 연산")
        print(b)
        print(a%b)
        a,b= b,a%b
        print("리턴되는 a",a)
    return a


print(Quiz(c))