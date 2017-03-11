def bfs(G, s):
    P, Q = {s:none}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P:
                continue
            P[v] = u
            Q.append(v)
    return P
