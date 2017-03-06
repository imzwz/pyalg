def ins_sort_req(seq,i):
    if i==0:
        return
    ins_sort_req(seq, i-1)
    j=i
    while j>0 and seq[j-1]> seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

def ins_sort(seq):
    for i in range(1, len(seq)):
        j=i 
        while j>0 and seq[j-1]> seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j-=1


