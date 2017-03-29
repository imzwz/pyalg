from itertools import combinations

def naive_lis(seq):
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub)==sorted(sub):
                return sub

def rec_lis(seq):
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1+ L(pre))
        return res
    return max( L(i) for i in range(len(seq)))

def basic_lis(seq):
    L = [1]* len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1+L[pre])
    return max(L)


