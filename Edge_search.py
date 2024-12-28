from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, a, b):
        self.graph[a].append(b)

    def DFSutil(self, a, visited):
        visited.add(a)
        print(a)
        for neighbour in self.graph[a]:
            if neighbour not in visited:
                self.DFSutil(neighbour, visited)
    
    def DFS(self, a):
        visited = set()
        self.DFSutil(a, visited)

vert = Graph()
vert.addedge(0,1)
vert.addedge(0,2)
vert.addedge(1,2)
vert.addedge(2,0)
vert.addedge(2,3)
vert.addedge(3,2)

print("The following example is demonstrating Depth First Search, starting from vertex 0.")

vert.DFS(0)

print("Now, it's starting from vertex 1.")

vert.DFS(1)

print("Now, it's starting from vertex 2.")

vert.DFS(2)

print("Now, it's starting from vertex 3.")

vert.DFS(3)

userinput=input(int())