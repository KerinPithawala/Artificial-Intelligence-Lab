#Constructing undirected graph with adjaceny list representation
class Vertex:
    def __init__(self,n):
        self.name=n
        self.neighbours=list()
    def add_neighbour(self,v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()
            print("Edge added")

class Graph:
    vertices={}
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name]=vertex
            print("vertex added")
            return True
        else:
            print("Vertex not added")
            return False

    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key==u:
                    value.add_neighbour(v)
                if key==v:
                    value.add_neighbour(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+str(self.vertices[key].neighbours))

    def bfs(self,source):
        
        visited={}
        for i in self.vertices:
            visited[i]=False
        q=list()
        q.append(source)
        visited[source]=True
        while q:
            s=q.pop(0)
            print(s, end=" ")
            for i in self.vertices:
                if visited[i]==False:
                    q.append(i)
                    visited[i]=True

g=Graph()
i=0
while i==0:
    print("1. Add vertex 2. Add edge ")
    choice=int(input())
    if choice==1:
        #a=Vertex(v)
        v=input("Enter vertice name ")
        a=Vertex(v)
        g.add_vertex(a)
    else:
        e=input("Add edge").split(" ")
        g.add_edge(e[0],e[1])
    i=int(input("Enter 0 to continue "))

g.print_graph()

src=input("Enter source for breadth first search")
g.bfs(src)

    
