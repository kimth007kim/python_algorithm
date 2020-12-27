# a=input()
# alpha= [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
#
# for i in range(len(a)):
#
#     if a[i]=='a':
#         if alpha[0]==-1:
#             alpha[0]=i
#     elif a[i]=='b':
#         if alpha[1]==-1:
#             alpha[1]=i
#     elif a[i] == 'c':
#         if alpha[2] == -1:
#             alpha[2] = i
#     elif a[i]=='d':
#         if alpha[3]==-1:
#             alpha[3]=i
#     elif a[i] == 'e':
#         if alpha[4]==-1:
#             alpha[4]=i
#     elif a[i]=='f':
#         if alpha[5]==-1:
#             alpha[5]=i
#     elif a[i]=='g':
#         if alpha[6]==-1:
#             alpha[6]=i
#     elif a[i] == 'h':
#         if alpha[7]==-1:
#             alpha[7]=i
#     elif a[i]=='i':
#         if alpha[8]==-1:
#             alpha[8]=i
#     elif a[i]=='j':
#         if alpha[9]==-1:
#             alpha[9]=i
#     elif a[i] == 'k':
#         if alpha[10]==-1:
#             alpha[10]=i
#     elif a[i]=='l':
#         if alpha[11]==-1:
#             alpha[11]=i
#     elif a[i]=='m':
#         if alpha[12]==-1:
#             alpha[12]=i
#     elif a[i] == 'n':
#         if alpha[13]==-1:
#             alpha[13]=i
#     elif a[i]=='o':
#         if alpha[14]==-1:
#             alpha[14]=i
#     elif a[i]=='p':
#         if alpha[15]==-1:
#             alpha[15]=i
#     elif a[i]=='q':
#         if alpha[16]==-1:
#             alpha[16]=i
#     elif a[i] == 'r':
#         if alpha[17]==-1:
#             alpha[17]=i
#     elif a[i]=='s':
#         if alpha[18]==-1:
#             alpha[18]=i
#     elif a[i]=='t':
#         if alpha[19]==-1:
#             alpha[19]=i
#     elif a[i]=='u':
#         if alpha[20]==-1:
#             alpha[20]=i
#     elif a[i]=='v':
#         if alpha[21]==-1:
#             alpha[21]=i
#     elif a[i]=='w':
#         if alpha[22]==-1:
#             alpha[22]=i
#     elif a[i]=='x':
#         if alpha[23]==-1:
#             alpha[23]=i
#     elif a[i]=='y':
#         if alpha[24]==-1:
#             alpha[24]=i
#     elif a[i]=='z':
#         if alpha[25]==-1:
#             alpha[25]=i
#
# for i in alpha:
#     print(i,end=" ")

print(map(input().find,map(chr,range(97,123))), sep=" ")