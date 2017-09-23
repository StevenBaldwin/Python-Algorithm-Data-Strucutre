from DirectedGraph import DirectedGraph

def top_util(graph,vtx,visited,stack):
    visited[vtx] = True

    for i in graph.adjacent(vtx):
        if not visited[i]:
            top_util(graph,i,visited,stack)
    stack.append(vtx)


def topological_sort(graph):
    visited = [False]*len(graph.nodes)
    stack = []

    for i in graph.nodes:
        if not visited[i]:
            top_util(graph,i,visited,stack)
    return list(reversed(stack))


inf = float('inf')
adj_mat = [
            [0,inf,inf,inf,inf,inf],
            [inf,0,inf,inf,inf,inf],
            [inf,inf,0,1,inf,inf],
            [inf,1,inf,0,inf,inf],
            [1,1,inf,inf,0,inf],
            [1,inf,1,inf,inf,0]
            ]
so =  topological_sort(DirectedGraph(adj_mat))
print(so )
print(so == [5, 4, 2, 3, 1, 0])
