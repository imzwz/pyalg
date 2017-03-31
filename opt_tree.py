from collections import defaultdict
def opt_tree(p):
    n = len(p)
    s, e = defaultdict(int), defaultdict(int)
    for k in range(1, n+1):
        for i in range(n-k+1):
            j = i+k
            s[i,j] = s[i, j-1] + p[j-1]
            e[i,j] = min(e[i,r] + e[r+1,j] for r in range(i,j))
            e[i,j] += s[i,j]
    return e[0,n]

def rec_opt_tree(p):
    @memo
    def s(i,j):
        if i==j: return 0
        return s(i, j-1) + p[j-1]
    @memo
    def e(i,j):
        if i==j: return 0
        sub = min(e(i,r)+ e(r+1, j) for r in range(i,j))
        return sub + s(i,j)
    return e(0, len(p))
