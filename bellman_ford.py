from DirectedGraph import DirectedGraph

def check_negative_cycle(graph,distances):
    edges = graph.get_edges()
    for edge in edges:
        s = edge[0]
        d = edge[1]
        w = edge[2]
        if distances[d] > (distances[s] + w):
            return True
    return False

def relax(graph,distances):
    edges = graph.get_edges()
    for edge in edges:
        s = edge[0]
        d = edge[1]
        w = edge[2]
        if distances[d] > (distances[s] + w):
            distances[d] =  (distances[s] + w)


def bellman_ford(graph,source):
    distances = [float('inf')]*len(graph.nodes)
    distances[source] = 0

    for _ in range(len(graph.nodes)):
        relax(graph,distances)

    if check_negative_cycle(graph,distances):
        return False
    return distances

def tester():
    f = open('SSP_tests.in','r')
    t = int(f.readline())
    for _ in range(t):
        size = int(f.readline())
        adj = [None]*size

        for i in range(size):
            adj[i] = [int(x) for x in f.readline().split()]
        soln = [int(x) for x in f.readline().split()]
        print(bellman_ford(DirectedGraph(adj),0)==soln)

tester()
