num_student= int(input())
student_list=[]

for _ in range(num_student):
    w,h= map(int,input().split())
    student_list.append([w,h])

for a,b in student_list:
    rank=1
    for c,d in student_list:
        if a<c and b<d:
            rank+=1
    print(rank,end=" ")