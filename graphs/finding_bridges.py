def __get_demo_graph(index):
    return [
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3, 5],
            3: [2, 4],
            4: [3],
            5: [2, 6, 8],
            6: [5, 7],
            7: [6, 8],
            8: [5, 7],
        },
        {
            0: [6],
            1: [9],
            2: [4, 5],
            3: [4],
            4: [2, 3],
            5: [2],
            6: [0, 7],
            7: [6],
            8: [],
            9: [1],
        },
    ][index]


def compute_bridges(graph: dict) -> list:
    """
    Return the list of undirected graph bridges [(a1, b1), ..., (ak, bk)]; ai <= bi
    >>> compute_bridges(__get_demo_graph(0))
    [(3, 4), (2, 3), (2, 5)]
    >>> compute_bridges(__get_demo_graph(1))
    [(6, 7), (0, 6), (1, 9), (3, 4), (2, 4), (2, 5)]
    >>> compute_bridges({})
    []
    """

    id = 0
    n = len(graph)  # No of vertices in graph
    low = [0] * n
    visited = [False] * n

    def dfs(at, parent, bridges, id):
        visited[at] = True
        low[at] = id
        id += 1
        for to in graph[at]:
            if to == parent:
                pass
            elif not visited[to]:
                dfs(to, at, bridges, id)
                low[at] = min(low[at], low[to])
                if id <= low[to]:
                    bridges.append((at, to) if at < to else (to, at))
            else:
                # This edge is a back edge and cannot be a bridge
                low[at] = min(low[at], low[to])

    bridges = []
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, bridges, id)
    return bridges
