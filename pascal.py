from functools import wraps
def memo(func):
    cache={}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
            return cache[args]
    return wrap

@memo
def C(n,k):
    if k==0: return 1
    if n==0: return 0
    return C(n-1, k-1) + C(n-1,k)
