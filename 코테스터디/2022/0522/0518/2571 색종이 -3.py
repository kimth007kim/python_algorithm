length=102

paper = [[0]*length for _ in range(length)]
n=int(input())
for i in range(n):
    a,b =map(int,input().split())
    paper[a][b]=1
    paper[a+10][b+10]=1
    paper[a+10][b]=-1
    paper[a][b+10]=-1

for i in range(1,length):
    tmp=0
    for j in range(length):
        paper[i][j]+=tmp
        tmp=paper[i][j]

for i in range(1,length):
    tmp=0
    for j in range(length):
        paper[j][i]+=tmp
        tmp=paper[j][i]

dp=[[0]*length for _ in range(length)]

for i in range(1,length):
    for j in range(1,length):
        dp[i][j]=(min(paper[i-1][j],paper[i][j-1],paper[i-1][j-1]))+1

max_size =0

for row in range(100):
    paper_row = paper[row]
    pre_idx_stack=[0]
    print(row)
    for cur_col in range(1,102):
        while pre_idx_stack and paper_row[pre_idx_stack[-1]]> paper_row[cur_col]:
            h= paper_row[pre_idx_stack[-1]]
            pre_idx_stack.pop()
            max_size= max(max_size,(cur_col-pre_idx_stack[-1]-1)*h)
        pre_idx_stack.append(cur_col)
print(max_size)