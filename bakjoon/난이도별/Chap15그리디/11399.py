# ATM 1대
# n명줄서있다 1~n 사람의수 =n

# [3,1,4,3,2]
# 3+1+4+3+

num= int(input())
graph=(list(map(int,input().split())))
ans=[]
result=0
graph.sort()
for i in graph:
    result+=i
    ans.append(result)
an=0
for j in ans:
    an+=j
print(an)