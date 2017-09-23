class DirectedGraph(object):

    def __init__(self, adj_mat):
        self.nodes =set(range(len(adj_mat)))
        self.adj_list = [[] for i in range(len(adj_mat))]
        self._build_from_adj(adj_mat)

    def _build_from_adj(self,adj_mat):
        JAVA_MAX_INT = 2147483647
        for i in range(len(adj_mat)):
            for j in range(len(adj_mat)):
                if adj_mat[i][j] != float("inf") and adj_mat[i][j] != 0 and adj_mat[i][j] != JAVA_MAX_INT:
                    self.adj_list[i].append((j,adj_mat[i][j]))

    def print_adj(self):
        adj = [[float("inf")]*len(self.nodes) for i in range(len(self.nodes))]
        for i in range(len(adj)):
            adj[i][i] = 0
        for idx,l in enumerate(self.adj_list):

            for edge in l:
                adj[idx][edge[0]] = edge[1]
        for row in adj:
            for itm in row:
                print(itm, end='\t')
            print()

    def adjacent(self,vtx):
        return {edge[0] for edge in self.adj_list[vtx]}

    def get_edges(self):
        """returns edges as a tuple of (source,destination,weight)"""
        edge_set = set()
        for idx,edges in enumerate(self.adj_list):
            for edge in edges:
                edge_set.add((idx,*edge))
        return edge_set

    def edges_of(self,vtx):
        edge_set = set()
        for edge in self.adj_list[vtx]:
            edge_set.add((vtx,*edge))
        return edge_set
