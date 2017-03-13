def naive_find(C, u):
    while C[u] !=u :
        u = C[u]
    return u

def naive_union(C, u, v):
    u = naive_find(C, u)
    v = naive_find(C, v)
    C[u] = v

def naive_kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C = {u:u for u in G}
    for _, u, v in sorted(E):
        if naive_find(C,u) != naive_find(C, v):
            T.add((u,v))
            naive_union(C, u, v)
    return T

def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]

def union(C, R, u, v):
    u, v = find(C,u), find(C,v)
    if R[u] > R[v]:
        C[v]=u
    else:
        C[u]=v
    if R[u]==R[v]:
        R[v]+=1

def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R = {u:u for u in G}, {u:0 for u in G}
    for _, u, v in sorted(E):
        if find(C, u)!=find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T

        


