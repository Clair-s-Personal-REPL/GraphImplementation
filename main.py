# The main purpose of this application is to take in a graph, and to find a shortest path from one node to another node
# This program uses the pseudocode from this video: https://www.youtube.com/watch?v=oDqjPvD54Ss
# Had to make a few changes from the pseudocode since I am using an object here

# Instead of enqueue, it is put
# Instead of dequeue, it is get
# Instead of isEmpty, it is empty
from queue import Queue
import string

'''
graphImp contains an adjacency list implemented as a dictionary, a number of nodes in the graph, and a queue that is only
to be used within the class. It currently contains functions that list all of the nodes and their adjacent nodes, functions 
that can add and remove nodes inside the graph, and a function that finds the shortest path from one node to another node

input: graph - an adjacency dictionary that contains a node and a list of every node that is connected to it (default is 
an empty dictionary)

output: None
'''
class graphImp() :

  def __init__(self, graph={}) :
    self.graph = graph
    self.numNodes = len(graph)
    self.toTraverse = Queue()

  '''
  listAllNodes prints out all of the nodes that are inside the adjacency list

  input: self

  output: None
  '''
  def listAllNodes(self):
    for node in self.graph:
      print(node, end = " ")
    print()

  '''
  listAllNodesAndConnections prints out all of the nodes that are inside the adjacency list, as well as all of the nodes that
  they are adjacent to

  input: self

  output: None
  '''
  def listAllNodesAndConnections(self):
    for node in self.graph:
      print("%s ->" % (node), end=" ")
      for adjacents in self.graph[node]:
        print("%s" % (adjacents), end=" ")
      print()

  '''
  addNode adds a node and every node that is adjacent to it to the graph's adjacency list. Will update every other node in
  the table that the new node connects to. If a node in the given adjacency list does not exist, then that node will be added
  to the adjacency list as well. If the node exists and the adjacency list is different from the original adjacency list, the
  adjacency list will be replaced, and any nodes that are not in the new list will lose their link to the original node. Any
  node that is added will update the numNodes variable as well.

  input: self
    nodeName - the name of the node that is being added to the graph's adjacency list
    nodeAdjacents - a list of all of the nodes that nodeName is connected to

  output: True/False - if the node is not found, output True, if the node is found, output False
  '''
  def addNode(self, nodeName, nodeAdjacents):
    for node in self.graph:
      if node in self.graph[nodeName] and node not in nodeAdjacents:
        self.graph[node].remove(nodeName)

    if nodeName not in self.graph:
      self.numNodes += 1

    self.graph[nodeName] = nodeAdjacents
    for node in nodeAdjacents:
      if node in self.graph:
        if nodeName not in self.graph[node]:
          self.graph[node].append(nodeName)
      else:
        self.graph[node] = [nodeName]
        self.numNodes += 1

    return True

  '''
  removeNode removes a node from the adjacency graph, as well as removing every occurance of the node in the adjacency
  lists of each other node.

  input: self
    nodeName - the name of the node that is being removed from the list

  output: None
  '''
  def removeNode(self, nodeName):
    del self.graph[nodeName] 
    for node in self.graph:
      if nodeName in self.graph[node]:
        self.graph[node].remove(nodeName)

  '''
  shortestPath uses breadth first search (bfs) to determine the shortest possible path between two different nodes

  input: self
    startNode - the starting node that is being traversed from
    endNode - the ending node that is being traversed to

  output: path - a list that contains the nodes from left to right to traverse through
  '''
  def bfsShortestPath(self, startNode, endNode):

    '''
    solve uses a queue to determine the node that needs to be searched next. At the end, solve determines a path to each node 
    inside the adjacency list.

    input: self
      startNode - the starting node that is being traversed from

    output: prev - a reverse list that contains a node and the node that points to it
    '''
    def solve(self, startNode):
      self.toTraverse.put(startNode)

      visited = {}
      for node in self.graph:
        visited[node] = False
      visited[startNode] = True

      prev = {}
      for node in self.graph:
        prev[node] = None

      while(not self.toTraverse.empty()):
        node = self.toTraverse.get()
        neighbors = self.graph[node]

        for nextt in neighbors:
          if not visited[nextt]:
            self.toTraverse.put(nextt)
            visited[nextt] = True
            prev[nextt] = node
      
      return prev

    '''
    reconstructPath builds a path using the end node, and goes up to the startNode.

    input: self
      startNode - the starting node that is being traversed from
      endNode - the ending node that is being traversed to
      prev - a reverse list that contains a node and the node that points to it

    output: path - a list that contains the nodes from left to right to traverse through
    '''
    def reconstructPath(self, startNode, endNode, prev):
      path = []
      at = endNode
      while at != None:
        path.append(at)
        at = prev[at]
      
      path.reverse()

      if path[0] == startNode:
        return path
      return []

    prev = solve(self, startNode)

    path = reconstructPath(self, startNode, endNode, prev)
    return path

    def dfs(self, startNode, endNode):
      pass


# for i in range(0, 100):


# graph = {"A": ["B", "C", "F"], 
#  "B": ["A", "D"], 
#  "C": ["A", "E", "F"], 
#  "D": ["B", "E"], 
#  "E": ["C", "D"], 
#  "F": ["C"]}

# numNodes = 6

graphObject = graphImp()

graphObject.addNode("A", ["B", "C"])
graphObject.addNode("B", ["A", "C"])
graphObject.addNode("C", ["B"])

graphObject.listAllNodesAndConnections()

print(graphObject.numNodes)

# path = graphObject.bfsShortestPath("F", "B")

# print(path)

# print(len(path) - 1)
  

