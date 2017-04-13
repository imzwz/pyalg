def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def quicksort(seq):
    if len(seq)<=1 : return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)

def qsort(seq,low=0,high=None):
    if high==None:
        high = len(seq)-1
    if low < high:
        s, i, j = seq[low],low,high
        while i < j:
            while i < j and seq[j] >=s:
                j=j-1
            if i<j:
                seq[i]=seq[j]
                i=i+1
            while i < j and seq[i] <=s:
                i=i+1
            if i<j:
                seq[j] = seq[i]
                j=j-1
        seq[i] = s
        qsort(seq, low, i-1)
        qsort(seq, i+1, high)

seq = [3,1,9,5,2,4]
qsort(seq)
print(seq)

