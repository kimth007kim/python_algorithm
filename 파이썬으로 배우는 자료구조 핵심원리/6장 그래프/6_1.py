class Graph:
    def __init__(self,vertex_num=None):
        self.adj_list=[]
        self.vtx_num=0
        self.vtx_arr=[]
        if vertex_num:
            self.vtx_num=vertex_num
            self.vtx_arr=[True for _ in range(self.vtx_num)]
            self.adj_list=[[] for _ in range(self.vtx_num)]

    def is_empty(self):
        if self.vtx_num==0:
            return True
        return False

    def add_vertex(self):
        for i in range(len(self.vtx_arr)):
            if self.vtx_arr[i]==False:
                self.vtx_num+=1
                self.vtx_arr[i]= True
                return i

        self.adj_list.append([])
        self.vtx_num +=1
        self.vtx_arr.append(True)
        return self.vtx_num-1

    def delete_vertex(self,v):
        if v>= self.vtx_num:
            raise Exception(f"There is no vertex of {v}")
        if self.vtx_arr[v]:
            self.adj_list[v]=[]
            self.vtx_num-= 1
            self.vtx_arr[v] =False

            for adj in self.adj_list:
                for vertex in adj:
                    if vertex == v:
                        adj.remove(vertex)

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def delete_edge(self,u,v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def adj(self,v):
        return self.adj_list[v]

def show_graph(g):
    print(f"num of vertices : {g.vtx_num}")
    print("vertices : {", end="")
    for i in range(len(g.vtx_arr)):
        if g.vtx_arr[i]:
            print(f"{i}, ", end="")
    print("}")
    for i in range(len(g.vtx_arr)):
        if g.vtx_arr[i]:
            print(f"[{i}] : {{", end="")
            for j in g.adj_list[i]:
                print(f"{j}, ", end=" ")
            print("}")


if __name__=="__main__":
    g=Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    show_graph(g)
    print()

    added=g.add_vertex()
    g.add_edge(added, 1)
    g.add_edge(added, 2)
    show_graph(g)
    print()

    g.delete_vertex(2)
    show_graph(g)
    print()

    added=g.add_vertex()
    print(added)
    g.add_edge(added, 1)
    g.add_edge(added, 4)
    show_graph(g)
    print()
