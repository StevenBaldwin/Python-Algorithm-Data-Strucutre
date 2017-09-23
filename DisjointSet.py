class DisjointSet:
    """Takes integers as types for a DisjointSet"""
    def __init__(self, numel):
        """takes numel as the number of integers to be in the disjoint set"""
        self.rank = [0]*numel
        self.parent = [i for i in range(numel)]

    def _find(self,x):
        """"""

        if self.parent[x] != x:
            self.parent[x] = self._find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        """Performs a union operation on the sets of x and y"""
        x_root, y_root = self._find(x), self._find(y)
        if x_root==y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[y_root] < self.rank[x_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root]+=1

    def same_set(self,x,y):
        """returns a boolean if elements are in the same set"""
        return self._find(x) == self._find(y)
