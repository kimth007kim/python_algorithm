t= int(input())
for i in range(t):
    n= int(input())
    word = list(map(int,input().split()))
    word_dic= {}
    for j in word:
        word_dic[j]=1
    m= int(input())
    target= list(map(int,input().split()))
    for j in target:
        if j in word_dic:
            print(1)
        else:
            print(0)