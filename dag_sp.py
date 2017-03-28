def dag_sp(W, s, t):
    d = {u: float('inf') for u in W}
    d[s]=0
    for u in topsort(W):
        if u == t: break
        for v in W[u]:
            d[v] = min(d[v], d[u]+d[u][v])
    return d[t]
        

