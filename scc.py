from topsort import dfs_topsort
from components import walk
def tr(G):
    GT = {}
    for u in G:
        GT[u]=set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

def scc(G):
    GT = tr(G)
    sccs, seen = [], set()
    for u in dfs_topsoet(G):
        if u in seen: continue
        C = walk(GT, u, seen)
        seen.update(C)
        sccs.append(C)
    return sccs

