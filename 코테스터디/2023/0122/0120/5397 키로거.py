t=  int(input())
for i in range(t):
    word= list(input())
    length =len(word)
    answer= []
    for i in word:
        if i=="<" or i ==">" or i=="-":
            answer.append("")
        else:
            answer.append(i)
    cand=[]
    start=0
    for i in range(length):
        if word[i] != "<" and word[i] != ">" and word[i] != "-":
            cand.append([start,i])
            start=i+1



    print(answer)
    print(word)
    print(cand)
    # for i in range(len(word)):
    #     print()
    # print(word)