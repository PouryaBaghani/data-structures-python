"""
=============================================
  🚀 Graph Project - By BASH 🚀
=============================================
"""
class Graph:
    def __init__(self):
        self.adjList = {}


    def AddVertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []


    def AddEdge(self, firstVertex, secondVertex):
        #By Baqani
        pass


    def RemoveEdge(self, firstVertex, secondVertex):
        if firstVertex in self.adjList and secondVertex in self.adjList:
            if secondVertex in self.adjList[firstVertex]:
                self.adjList[firstVertex].remove(secondVertex)
            if firstVertex in self.adjList[secondVertex]:
                self.adjList[secondVertex].remove(firstVertex)


    def RemoveVertex(self, vertex):
        #By Baqani
        pass


    def BFS(self, start):
        visited = set()
        queue = []
        result = ""

        queue.append(start)
        visited.add(start)

        while queue:
            current = queue.pop(0)
            result += current + " "

            for neighbor in self.adjList[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result.strip()


    def DFS(self, start):
        #By Baqani
        pass


#TEST:
g = Graph()

g.AddVertex("A")
g.AddVertex("B")
g.AddVertex("C")
g.AddVertex("D")
g.AddVertex("E")

g.AddEdge("A", "B")
g.AddEdge("A", "C")
g.AddEdge("B", "D")
g.AddEdge("C", "E")

print("BFS:", g.BFS("A"))
print("DFS:", g.DFS("A"))