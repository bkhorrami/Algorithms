__author__ = 'babak_khorrami'

import numpy as np

class QuickUnionUF(object):
    def __init__(self,n):
        self.size = n
        self.id = []
        for i in range(n):
            self.id.append(i)

    def root_find(self,p):
        """
        Finds and returns the root of element p
        """
        while self.id[p] != p:
            p=self.id[p]

        return p

    def connected(self,p,q):
        """
        If p and q are connected return True, else return False
        """
        return self.root_find(p) == self.root_find(q)

    def union(self,p,q):
        """
        Union between p and q
        """
        p_root = self.root_find(p)
        q_root = self.root_find(q)
        if p_root != q_root:
            self.id[p_root] = q_root

    def print_id(self):
        print(self.id)


def main():
    n = 10
    qu = QuickUnionUF(n)
    test_case = np.random.randint(0,n,10).reshape((5,2))
    print(test_case)
    for i in range(test_case.shape[0]):
        qu.union(test_case[i,0],test_case[i,1])

    qu.print_id()

    print(qu.connected(0,4))

if __name__ == '__main__':
    main()




