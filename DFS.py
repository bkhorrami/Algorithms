__author__ = 'babak_khorrami'

from collections import defaultdict
from Graph import *

class DFS(object):
    def __init__(self,graph = None):
        if graph==None:
            self.graph = Graph()
            self.visited=defaultdict(int)
            self.edge_to=defaultdict(int)
            return

        self.graph = graph
        nodes = self.graph.get_nodes()
        self.visited=defaultdict(int)
        self.visited.update((i,False) for i in nodes)
        self.edge_to=defaultdict(int)
        self.edge_to.update((i,-1) for i in nodes)

    def dfs(self,s):
        stack=[]
        stack.append(s)
        self.visited[s]=True
        self.edge_to[s]=s
        count=0
        while len(stack) != 0:
            v=stack[-1] #peek at the last element pushed
            adj = self.graph.adjacent_nodes(v) #find adjacent nodes of the current node
            kv=[(k,v) for k,v in self.visited.items()]
            not_visited=[t[0] for t in kv if t[1]==False]
            adj_not_visited = [n for n in adj if n in not_visited]
            if(len(adj_not_visited)) != 0:
                w=adj_not_visited.pop()
                self.visited[w] = True
                self.edge_to[w] = v
                stack.append(w)
            else:
                done = stack.pop()
                del(done)

    def print_dfs(self):
        print(self.edge_to.keys())
        print(self.edge_to.values())


            # v=stack.pop()
            # adj = self.graph.adjacent_nodes(v) #find adjacent nodes of the current node
            # kv=[(k,v) for k,v in self.visited.items()]
            # not_visited=[t[0] for t in kv if t[1]==False]
            # adj_not_visited = [n for n in adj if n in not_visited]
            # self.visited.update((i,True) for i in adj_not_visited)
            # stack.extend(adj_not_visited)



            # stack.extend(adj) #add the adjacent nodes to the stack


                # kv=[(k,v) for k,v in self.visited.items()]
                # not_visited=[t[0] for t in kv if t[1]==False]
                # adj_not_visited = [n for n in adj if n in not_visited] #check