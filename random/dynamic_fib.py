def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

# [1, 1, 2, 3, 5, 8, 13, 21, ...]
assert(fib(5) == 8)

fib_cache_recursive = {
    0: 1,
    1: 1,
}

def fib_memo_recursive(n):
    if n not in fib_cache_recursive:
        fib_cache_recursive[n] = fib_memo_recursive(n-1) + fib_memo_recursive(n-2)
    return fib_cache_recursive[n]

def fib_memo_iterative(n):
    cache = [1, 1]
    while len(cache) < n:
        cache.append(cache[-1] + cache[-2])
    return cache[n]

