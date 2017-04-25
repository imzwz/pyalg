def heap_adjust(seq, s, m):
    if 2*s > m:
        return
    tmp = s-1
    if seq[2*s-1] > seq[tmp]:
        tmp = 2*s-1
    if 2*s <= m-1 and seq[2*s] > seq[tmp]:
        tmp = 2*s
    if tmp <> s-1:
        seq[s-1], seq[tmp] = seq[tmp], seq[s-1]
        heap_adjust(seq, tmp+1, m)

def heap_sort(seq):
    m = len(seq)/2
    for i in range(m, 0, -1):
        heap_adjust(seq, i, len(seq))
    seq[0],seq[-1] = seq[-1], seq[0]
    for n in range(len(seq)-1,1,-1):
        heap_adjust(seq,1,n)
        seq[0], seq[n-1] = seq[n-1], seq[0]

seq = [5,1,3,2,9,7]
heap_sort(seq)
print(seq)

