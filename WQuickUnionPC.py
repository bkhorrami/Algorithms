__author__ = 'babak_khorrami'


import numpy as np

class WQuickUnionPCUF(object):
    #** weighted quick union with path compression
    def __init__(self,n):
        self.size = n # No. elements
        self.id = []
        self.sub_tree_size = []
        for i in range(n):
            self.id.append(i)
            self.sub_tree_size.append(1) #each node has a size One

    def size(self):
        return self.size

    def root_find(self,p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]] #Path Compression happens here!
            p = self.id[p]

        return p

    def connected(self,p,q):
        return self.id[p] == self.id[q]


    def union(self,p,q):
        p_root , q_root = self.root_find(p) , self.root_find(q)
        if p_root == q_root:
            return
        if self.sub_tree_size[p] < self.sub_tree_size[q]:
            self.id[p] = q_root
            self.sub_tree_size[q] += self.sub_tree_size[p]
        else:
            self.id[q] = p_root
            self.sub_tree_size[p] += self.sub_tree_size[q]

    def print_id(self):
        print(self.id)

#***** Testing the code :
def main():
    n = 10
    wqf = WQuickUnionPCUF(n)
    test_case = np.random.randint(0,n,20).reshape((10,2))
    print(test_case)
    for i in range(test_case.shape[0]):
        wqf.union(test_case[i,0],test_case[i,1])

    wqf.print_id()

    print(wqf.connected(0,4))

if __name__ == '__main__':
    main()

