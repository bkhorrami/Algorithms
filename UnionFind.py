__author__ = 'babak_khorrami'
import numpy as np

class QuickFindUF(object):

    def __init__(self,n):
        self.size = n
        self.id = []
        for i in range(n):
            self.id.append(i)

    def connected(self,p,q):
        """
        Are p and q connected?
        """
        return self.id[p] == self.id[q]

    def union(self,p,q):
        pid , qid = self.id[p] , self.id[q]
        for i in range(self.size):
            if self.id[i] == pid:
                self.id[i] = qid

    def print_id(self):
        print(self.id)


def main():
    n = 10
    qf = QuickFindUF(n)
    test_case = np.random.randint(0,n,10).reshape((5,2))
    print(test_case)
    for i in range(test_case.shape[0]):
        qf.union(test_case[i,0],test_case[i,1])

    qf.print_id()

    print(qf.connected(0,4))

if __name__ == '__main__':
    main()








