paper = [[0]*102 for _ in range(100)]

for i in range(int(input())):
    x,y= map(int,input().split())
    for i in range(x+1,x+11):
        for j in range(y,y+10):
            paper[j][i]=1


for i in range(1,100):
    for j in range(1,102):
        if paper[i][j]:
            paper[i][j]=paper[i-1][j]+1

max_size= 0

for row in range(100):
    paper_row = paper[row]

    pre_idx_stack = [0]

    for cur_col in range(1,102):

        # print(pre_idx_stack)
        while pre_idx_stack and paper_row[pre_idx_stack[-1]]>paper_row[cur_col]:
            print(cur_col,pre_idx_stack)
            # print(cur_col,paper_row, pre_idx_stack)
            h=paper_row[pre_idx_stack[-1]]
            # print(h)
            pre_idx_stack.pop()
            max_size= max(max_size,(cur_col-pre_idx_stack[-1]-1)*h)
        pre_idx_stack.append(cur_col)

# for i in paper:
# #     print(i)