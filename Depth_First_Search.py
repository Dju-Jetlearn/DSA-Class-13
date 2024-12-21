from collections import defaultdict

#DFS does as far down a graph as it can go, whereas BFS goes as far across a graph that it can go

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) # Default'dict' = default dictionary. its to store the graph

    def addedge(self, a, b):
        self.graph[a].append(b)
    
    #A function used by DFS -> depth first search
    def DFSutil(self, a, visited): # DFSutil is used to visit all vertices
        visited.add(a)
        print(a)
        for neighbour in self.graph[a]:
            if neighbour not in visited:
                self.DFSutil(neighbour, visited)
    
    def DFS(self, a):
        visited = set() # a set makes it so that in visited, any repeats of vertices, eg. 11223344, is abbreviated to 1234
        self.DFSutil(a, visited) # this line just calls DFSutil

vert = Graph()
vert.addedge(0,1)
vert.addedge(0,2)
vert.addedge(1,2)
vert.addedge(2,0)
vert.addedge(2,3)
vert.addedge(3,2)

print("The following example is demonstrating Depth First Search, starting from vertex 0.")
#just call the function
vert.DFS(0)

print("Now, it's starting from vertex 1.")

vert.DFS(1)

print("Now, it's starting from vertex 2.")

vert.DFS(2)

print("Now, it's starting from vertex 3.")

vert.DFS(3)