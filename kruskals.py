from DirectedGraph import DirectedGraph
from DisjointSet import DisjointSet


def kruskal(graph):
    djs = DisjointSet(numel=len(graph.nodes))
    all_nodes = set(range(len(graph.nodes)))
    weight = 0
    edges = list(graph.get_edges())
    edges.sort(key=lambda tup: tup[2])
    fs = set()

    for e in edges:
        source = e[0]
        dest = e[1]
        wt = e[2]

        if not djs.same_set(source,dest):
            fs.add(source)
            fs.add(dest)
            weight+=wt
            djs.union(source,dest)

    return weight




def tester():
    f = open('MST_tests.in','r')
    t = int(f.readline())
    for _ in range(t):
        size = int(f.readline())
        adj = [None]*size

        for i in range(size):
            adj[i] = [int(x) for x in f.readline().split()]
        soln = int(f.readline())
        print(kruskal(DirectedGraph(adj))==soln)

tester()
