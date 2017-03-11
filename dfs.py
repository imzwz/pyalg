def rec_dfs(G, s, S=None):
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)

def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)
    while Q:
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
        yield u

def traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u

def dfs(G, s, d, f, S=None, t=0):
    if S = None:
        S = set()
    d[s]=t;
    t+=1
    S.add(s)
    for u in G[s]:
        if u in S: continue
        t = dfs(G, u, d, f, S, t)
    f[s]=t
    t+=1
    return t

def iddfs(G,s):
    yielded = set()
    def recurse(G, s, d, S=None):
        if s not in yielded:
            yield s 
            yielded.add(s)
        if d == 0: 
            return
        if S is None:
            S = set()
        S.add(s)
        for u in G[s]:
            if u in S:
                continue
            for v in recurse(G, u, d-1, S):
                yield v
    n = len(G)
    for d in range(n):
        if len(yielded)==n : break
        for u in recurse(G, s, d):
            yield u
        
