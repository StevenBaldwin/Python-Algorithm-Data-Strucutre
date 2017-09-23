import copy

inf = float('inf')

def floyd_warshall(adj_mat):
    dist = copy.deepcopy(adj_mat)
    for k in range(len(adj_mat)):
        for i in range(len(adj_mat)):
            for j in range(len(adj_mat)):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    return dist


graph = [[0,5,inf,10],
             [inf,0,3,inf],
             [inf, inf, 0,   1],
             [inf, inf, inf, 0]
        ]



print(floyd_warshall(graph) == [[0, 5, 8, 9], [inf, 0, 3, 4], [inf, inf, 0, 1], [inf, inf, inf, 0]])
