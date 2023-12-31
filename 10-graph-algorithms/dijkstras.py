# class for weighted edges

import heapq

class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

# class for nodes (vertex)
        
class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.parent = None # parent node to track path
        self.neighbors = []
        self.shortest_path = float("inf") # set vertex to infinity


    def __lt__(self, other_vertex):
        # returns true if current nodes min distance is lesser than neighboring nodes min distance
        return self.shortest_path < other_vertex.shortest_path
    
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)


# Dijkstra algorithm
        
class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.shortest_path = 0 # start vertex distance is 0
        heapq.heappush(self.heap, start_vertex) # push start vertex to heap
        while self.heap: # while there is an element in the heap
            actual_vertex = heapq.heappop(self.heap) # pop element with least distance
            if actual_vertex.visited: # if visited, continue to next node
                continue
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.shortest_path + edge.weight
                if new_distance < target.shortest_path:
                    target.shortest_path = new_distance # compare the shortest path
                    target.parent = start # update parent node
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True


    def get_shortest_path(self, vertex): 
        print(f"shortest path: {vertex.shortest_path}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.parent



# testing - create nodes
nodeA = Vertex("A")
nodeB = Vertex("B")
nodeC = Vertex("C")
nodeD = Vertex("D")
nodeE = Vertex("E")
nodeF = Vertex("F")
nodeG = Vertex("G")
nodeH = Vertex("H")

# create edge

nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)
nodeB.add_edge(5, nodeD)
nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)
nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)
nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)
nodeE.add_edge(10, nodeG)
nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)            





