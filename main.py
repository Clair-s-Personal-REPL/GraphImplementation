# The main purpose of this application is to take in a graph, and to find a shortest path from one node to another node
# This program uses the pseudocode from this video: https://www.youtube.com/watch?v=oDqjPvD54Ss
# Had to make a few changes from the pseudocode since I am using an object here to implement the graph

# Instead of enqueue, it is put
# Instead of dequeue, it is get
# Instead of isEmpty, it is empty
from queue import Queue
import string
import random as rd

'''
graph_imp contains an adjacency list implemented as a dictionary, a number of nodes in the graph, and a queue that is only
to be used within the class. It currently contains functions that list all of the nodes and their adjacent nodes, functions 
that can add and remove nodes inside the graph, and a function that finds the shortest path from one node to another node

input: graph - an adjacency dictionary that contains a node and a list of every node that is connected to it (default is 
an empty dictionary)

output: None
'''
class graph_imp() :

  def __init__(self, graph={}) :
    self.graph = graph
    self.num_nodes = len(graph)
    self.to_traverse = Queue()

  '''
  list_all_nodes prints out all of the nodes that are inside the adjacency list

  input: self

  output: None
  '''
  def list_all_nodes(self):
    for node in self.graph:
      print(node, end = " ")
    print()

  '''
  list_all_nodes_and_connections prints out all of the nodes that are inside the adjacency list, as well as all of the nodes that
  they are adjacent to

  input: self

  output: None
  '''
  def list_all_nodes_and_connections(self):
    for node in self.graph:
      print("%s ->" % (node), end=" ")
      for adjacents in self.graph[node]:
        print("%s" % (adjacents), end=" ")
      print()

  '''
  add_node adds a node and every node that is adjacent to it to the graph's adjacency list. Will update every other node in
  the table that the new node connects to. If a node in the given adjacency list does not exist, then that node will be added
  to the adjacency list as well. If the node exists and the adjacency list is different from the original adjacency list, the
  adjacency list will be replaced, and any nodes that are not in the new list will lose their link to the original node. Any
  node that is added will update the num_nodes variable as well.

  input: self
    node_name - the name of the node that is being added to the graph's adjacency list
    node_adjacents - a list of all of the nodes that node_name is connected to

  output: None
  '''
  def add_node(self, node_name, node_adjacents):

    for node in self.graph:

      if not self.graph[node]:
        continue

      if node_name not in self.graph:
        continue

      if node not in node_adjacents and node in self.graph[node_name]:
        self.graph[node].remove(node_name)

    if node_name not in self.graph:
      self.num_nodes += 1

    self.graph[node_name] = node_adjacents
    for node in node_adjacents:
      if node in self.graph:
        if node_name not in self.graph[node]:
          self.graph[node].append(node_name)
      else:
        self.graph[node] = [node_name]
        self.num_nodes += 1

    return

  '''
  remove_node removes a node from the adjacency graph, as well as removing every occurance of the node in the adjacency
  lists of each other node.

  input: self
    node_name - the name of the node that is being removed from the list

  output: None
  '''
  def remove_node(self, node_name):
    del self.graph[node_name] 
    for node in self.graph:
      if node_name in self.graph[node]:
        self.graph[node].remove(node_name)

############################################################################################################################  


  '''
  bfs_shortest_path uses breadth first search (bfs) to determine the shortest possible path between two different nodes

  input: self
    start_node - the starting node that is being traversed from
    end_node - the ending node that is being traversed to

  output: path - a list that contains the nodes from left to right to traverse through. If there is no path between the nodes,
  the function returns an empty list.
  '''
  def bfs_shortest_path(self, start_node, end_node):

    '''
    solve uses a queue to determine the node that needs to be searched next. At the end, solve determines a path to each node 
    inside the adjacency list.

    input: self
      start_node - the starting node that is being traversed from

    output: prev - a reverse list that contains a node and the node that points to it
    '''
    def solve(self, start_node):
      self.to_traverse.put(start_node)

      visited = {}
      for node in self.graph:
        visited[node] = False
      visited[start_node] = True

      prev = {}
      for node in self.graph:
        prev[node] = None

      while(not self.to_traverse.empty()):
        node = self.to_traverse.get()
        neighbors = self.graph[node]

        for nextt in neighbors:
          if not visited[nextt]:
            self.to_traverse.put(nextt)
            visited[nextt] = True
            prev[nextt] = node
      
      return prev

    '''
    reconstruct_path builds a path using the end node, and goes up to the start_node.

    input: self
      start_node - the starting node that is being traversed from
      end_node - the ending node that is being traversed to
      prev - a reverse list that contains a node and the node that points to it

    output: path - a list that contains the nodes from left to right to traverse through
    '''
    def reconstruct_path(self, start_node, end_node, prev):
      path = []
      at = end_node
      while at != None:
        path.append(at)
        at = prev[at]
      
      path.reverse()

      if path[0] == start_node:
        return path
      return []

    prev = solve(self, start_node)

    path = reconstruct_path(self, start_node, end_node, prev)
    return path

############################################################################################################################

  '''
  dfs_connected_nodes takes a node and determines which nodes that it can reach based off of the connections in the adjacency
  list.

  input: self
    node_to_check - the node that is being checked for all nodes that it can reach

  output: connected - nodes that the input node is connected to
  
  '''
  def dfs_connected_nodes(self, node_to_check):
    visited = {}
    connected = []

    for key in self.graph:
      visited[key] = False

    '''
    dfs takes a node and visits its next neighbor, if it is able, if it is unable to visit a node (one that is already visited), it will continue to look at its neighbors until they have all been visited, and goes back to the prior method called.

    input: self
      next_node - the node that is being visited

    output: None

    '''
    def dfs(self, next_node):
      visited[next_node] = True
      for node in self.graph[next_node]:
        if not visited[node]:
          connected.append(node)
          dfs(self, node)

    dfs(self, node_to_check)

    return connected

############################################################################################################################

  '''
  create_random_graph takes a graph object and populates it using a variable for the amount of times to loop through the 
  randomizer. The nodes correspond to a single uppercase letter in the English alphabet. 

  input: self
    iterations - the number of times the loop should run

  output: None
  '''
  def create_random_graph(self, iterations):

    for i in range(0, iterations):
      j = rd.randint(0, 25)
      new_node = string.ascii_uppercase[j]

      adjacent_list = []
      for node in self.graph:
        check = rd.randint(0, 2)
        if check == 1:
          adjacent_list.append(node)

      self.add_node(new_node, adjacent_list)

  '''
  two_random_nodes takes a graph object and attempts to return two random nodes from the graph.

  input: self

  output: node1 - a node from the graph
    node2 - a node from the graph
  '''
  def two_random_nodes(self):
    listOfNodes = []
    for nodes in self.graph:
      listOfNodes.append(nodes)

    return rd.choice(listOfNodes), rd.choice(listOfNodes)
    


############################################################################################################################  

graph_object = graph_imp(graph={ "A": ["B", "C"],
                                 "B": ["A", "G"],
                                 "C": ["A", "D"],
                                 "D": ["C", "H", "J"],
                                 "E": ["F"],
                                 "F": ["E", "I", "K"],
                                 "G": ["B", "H"],
                                 "H": ["D", "G"],
                                 "I": ["F"],
                                 "J": ["D"],
                                 "K": ["F"]
                                 })

graph_object.list_all_nodes_and_connections()

print(graph_object.dfs_connected_nodes("A"))



# graph_object = graph_imp()

# graph_object.create_random_graph(10)

# graph_object.list_all_nodes_and_connections()

# print(graph_object.num_nodes)

# start_node, end_node = graph_object.two_random_nodes()

# print("%s -> %s" % (start_node, end_node))

# path = graph_object.bfs_shortest_path(start_node, end_node)

# print(path)

# print(len(path) - 1)
  

