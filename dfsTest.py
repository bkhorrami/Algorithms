__author__ = 'babak_khorrami'

from Graph import *
import pandas as pd
from DFS import *
import numpy as np

def main():
    data = pd.read_csv("/Users/babak_khorrami/Downloads/soc-Epinions1.txt",header=0,sep="\t")
    dt=np.array(data)
    nodes = set(dt[:,0:2].ravel())
    g=Graph()
    for n in nodes:
        g.add_node(n)

    for i in range(dt.shape[0]):
        g.add_edge(dt[i,0],dt[i,1],1)
    print(g.get_node_count())
    print("------ Graph Created -------")

    dfs_small = DFS(g)
    dfs_small.dfs(0)
    dfs_small.print_dfs()

if __name__ == '__main__':
    main()

