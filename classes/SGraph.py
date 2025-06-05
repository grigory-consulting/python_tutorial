class SGraph: 
    def __init__(self):
        self.adj_d = dict()
    
    def __str__(self):
        return str(self.adj_d)
    
    def add_node(self, node):
        if node not in self.adj_d: # check whether node already in dict
            self.adj_d[node] = set() # if not then add to graph
    
    def add_edge(self, node1, node2):
        if node1 == node2:
            return        # escape or quit the function
        self.add_node(node1)
        self.add_node(node2)
        self.adj_d[node1].add(node2)
        self.adj_d[node2].add(node1)
    
    def neighbors(self, node):
        return self.adj_d.get(node, "Node is not in graph.")
    
    def degree(self,node): # number of neighbors
        return len(self.neighbors(node))

    def nodes(self):
        return self.adj_d.keys()
    
    def size(self):
        return len(self.nodes())
    
    def is_empty(self):
        if self.adj_d:
            return False
        else:
            return True
    
    def remove_edge(self,node1, node2):
        if node1 in self.adj_d and node2 in self.adj_d:
            self.adj_d[node1].discard(node2)
            self.adj_d[node2].discard(node1)
    
    def remove_node(self,node):
        if node in self.adj_d:
            for neighbor in self.neighbors(node):
                self.remove_edge(node,neighbor)
        del self.adj_d[node]


    

def from_dict(d):
    G = SGraph()
    G.adj_d = d
    return G

print(from_dict({1:{2,3}, 2:{1,3,4}, 3: {1,2,4}, 4:{2,3}}))
