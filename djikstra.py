import heapq
import inspect
from DirectedGraph import DirectedGraph

inf = float('inf')




def dijkstra(graph,source):
    distances = [inf]*len(graph.nodes)
    distances[source] = 0
    visited = {source}
    hep = [(0,source)]

    while len(hep) > 0:
        u = heapq.heappop(hep)
        for adj in graph.edges_of(u[0]):
            source = adj[0]
            dest = adj[1]
            weight = adj[2]

            if distances[dest] > distances[source] +weight:
                distances[dest] =  distances[source] +weight
                #Ideally would check if the destination is already in the heap
                heapq.heappush(hep,(dest,distances[dest]))
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
        print(dijkstra(DirectedGraph(adj),0)==soln)

tester()
