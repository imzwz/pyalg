def rec_lcs(a, b):
    @memo
    def L(i,j):
        if min(i,j) < 0 : return 0
        if a[i]==b[j]: return 1 + L(i-1, j-1)
        return max(L(i-1,j), L(i, j-1))
    return L(len(a)-1, len(b)-1)

def lcs(a,b):
    n, m = len(a), len(b)
    pre, cur = [0]*(n+1), [0]*(n+1)
    for j in range(1, m+1):
        pre, cur = cur, pre
        for i in range(1, n+1):
            if a[i-1] == b[j-1]:
                cur[i] = pre[i-1] + 1
            else:
                cur[i] = max(pre[i], cur[i-1])
    return cur[n]

