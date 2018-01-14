__author__ = 'babak_khorrami'

from collections import defaultdict

class Node(object):
    def __init__(self,id,value = 0):
        self.id = id
        self.value = value

    def get_id(self):
        return self.id

    def get_value(self):
        return self.value


class Edge(object):
    def __init__(self,tail,head,weight=1):
        self.tail = tail
        self.head = head
        self.weight = weight

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def get_weight(self):
        return self.weight

    def get_opposite(self,v):
        if self.tail == v:
            return self.head
        elif self.head == v:
            return self.tail


    def get_ends(self):
        """
        :return: a tuple containing (tail.head)
        """
        return (self.tail,self.head)

#**** Graph Class :
class Graph(object):
    def __init__(self,nodes=None,edges_incoming=None,edges_outgoing=None,directed=True):
        self.directed = directed
        if nodes == None:
            self.nodes = set()
        else:
            self.nodes = nodes

        self.edges = defaultdict(int)

        if edges_outgoing==None:
            self.edges_outgoing = defaultdict(int)
        else:
            self.edges_outgoing = edges_outgoing

        if self.directed:
            if edges_incoming==None:
                self.edges_incoming = defaultdict(int)
            else:
                self.edges_incoming = edges_incoming
        else:
            self.edges_incoming = self.edges_outgoing

        self.node_count = len(self.nodes)
        self.edge_count = 0 #ADD CODE HERE


    def get_node_count(self):
        return self.node_count

    def get_edge_count(self):
        return self.edge_count

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        pass

    def add_node(self,v):
        self.nodes.add(v) #add the new node to the list of nodes
        self.edges[v] = defaultdict(int)
        self.edges_outgoing[v]=defaultdict(int) #add the node to the adjacency list & add a dict for incident nodes
        self.edges_incoming[v]=defaultdict(int)

    def add_edge(self,t,h,w):
        # Add nodes to the nodes set, if not there:
        self.nodes.add(t)
        self.nodes.add(h)
        self.edges[t][h]=w
        self.edges_outgoing[t][h]=w
        if self.directed:
            self.edges_incoming[h][t]=w

    def adjacent_nodes(self,v):
        return list(self.edges[v].keys())

    def incident_edges(self,v):
        pass


















