def shellsort(lists,step):
    l = len(lists)
    step = step
    group = l/step
    while group > 0:
        for i in range(0, group):
            j = i+group
            while j < l:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k+group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists

seq = [1,3,5,6,7,7,8,2,1]
print(shellsort(seq,3))
            

    
