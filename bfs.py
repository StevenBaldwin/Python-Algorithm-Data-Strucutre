from DirectedGraph import DirectedGraph

def bfs(graph,source):
    visited = [False]*len(graph.nodes)
    visited[source] = True
    bfs_list = []
    queue = [source]

    while queue:
        s = queue.pop(0)
        bfs_list.append(s)

        for vtx in graph.adjacent(s):
            if not visited[vtx]:
                visited[vtx] = True
                queue.append(vtx)
    return bfs_list


inf = float("inf")
adj_mat = [[0,1,1,inf],[inf,0,1,inf],[1,inf,0,1],[inf,inf,inf,0]]
search = bfs(DirectedGraph(adj_mat),2)
print(search)
print(search == [2,0,3,1])
