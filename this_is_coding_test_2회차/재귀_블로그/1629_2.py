# a,b,c=map(int,input().split())
#
# def pow(a,b,c):
#     if b==1:
#         return a%c
#     val = pow(a,b/2,c);
#     val=val*val%c
#     if b%2==0:
#         return val
#     return val * a %c
#
# print(pow(a,b,c))

def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % C
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.

        if b % 2 == 0:
            print(1,temp,temp*temp%C)
            return temp * temp % C # b가 짝수인 경우
        else:
            print(2,temp,temp*temp*a%C)
            return temp * temp * a % C # b가 홀수인 경우


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B)
    print(result)
