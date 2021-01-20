# graph1=[[0]*10 for i in range(8)]
#
# graph1[1][3]=1
# print("graph1")
# print(graph1)
#
#
# graph2=[[0]*10]*8
#
# graph2[1][3]=1
# print("graph2")
# print(graph2)

#
# for i in range(1):
#     print(i)

graph=[[0,1,0,1,0],[3,100,0,77,9],[0,False,True,"가","a",0]]


for i in range(3):
    for j in range(5):
        if graph[i][j]:
            print(graph[i][j])
