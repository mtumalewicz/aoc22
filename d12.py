file = open('test_data', 'r')
data = file.read().splitlines()

width = len(data[0])
height = len(data)
weight = "SabcdefghijklmnopqrstuvwxyzE"

class Graph:
 
  def __init__(self, vertices):
    self.V = vertices  # No. of vertices
    self.graph = []
 
  # function to add an edge to graph
  def addEdge(self, u, v, w):
    self.graph.append([u, v, w])
 
  # utility function used to print the solution
  def printArr(self, dist):
    print("Vertex Distance from Source")
    for i in range(self.V):
      print("{0}\t\t{1}".format(i, dist[i]))
  
  def print(self, dist, node):
    print("Vertex Distance from Source")
    print("Node:", node, dist[node])

  # The main function that finds shortest distances from src to
  # all other vertices using Bellman-Ford algorithm. The function
  # also detects negative weight cycle
  def BellmanFord(self, src):

    # Step 1: Initialize distances from src to all other vertices
    # as INFINITE
    dist = [float("Inf")] * self.V
    dist[src] = 0

    # Step 2: Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    for _ in range(self.V - 1):
      # Update dist value and parent index of the adjacent vertices of
      # the picked vertex. Consider only those vertices which are still in
      # queue
      for u, v, w in self.graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
          dist[v] = dist[u] + w
 
    # Step 3: check for negative-weight cycles. The above step
    # guarantees shortest distances if graph doesn't contain
    # negative weight cycle. If we get a shorter path, then there
    # is a cycle.

    for u, v, w in self.graph:
      if dist[u] != float("Inf") and dist[u] + w < dist[v]:
        print("Graph contains negative weight cycle")
        return

    # print all distance
    self.printArr(dist)
    self.print(dist, 21)


g = Graph(width*height)
index = 0

for y in range(height):
  for x in range(width):
    if x != width-1:
      if (weight.index(data[y][x+1]) - weight.index(data[y][x]) <= 1):
        print("add edge", data[y][x], data[y][x+1])
        g.addEdge(index, index+1, 1)
    if y != height-1:
      if (weight.index(data[y+1][x]) - weight.index(data[y][x]) <= 1):
        print("add edge", data[y][x], data[y+1][x])
        g.addEdge(index, index+width, 1)
    if x != 0:
      if (weight.index(data[y][x-1]) - weight.index(data[y][x]) <= 1):
        print("add edge", data[y][x], data[y][x-1])
        g.addEdge(index, index-1, 1)
    if y != 0:
      if (weight.index(data[y-1][x]) - weight.index(data[y][x]) <= 1):
        print("add edge", data[y][x], data[y-1][x])
        g.addEdge(index, index-width, 1)

    index += 1

g.BellmanFord(0)

print(width)
