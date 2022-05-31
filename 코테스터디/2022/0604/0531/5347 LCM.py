def dfs(now,dict,MAX,SET):
    for i in range(2,MAX+1):
        if now % i==0:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
            SET.add(i)
            dfs(now//i,dict,MAX,SET)
            return
    return


t= int(input())
for i in range(t):
    a,b= map(int,input().split())
    MAX=max(a,b)
    SET=set()
    dict_a={}
    dict_b={}
    answer=1
    dfs(a,dict_a,MAX,SET)
    dfs(b,dict_b,MAX,SET)
    for j in SET:
        _a = 0
        _b = 0
        if j in dict_a:
            _a= dict_a[j]
        if j in dict_b:
            _b= dict_b[j]
        tmp = max(_a,_b)
        answer*=j**tmp

    print(answer)
    # break