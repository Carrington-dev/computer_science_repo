from itertools import product


def find_the_kth(n, k):
    arr = [ list(range(1, n + 1)) for i in range(n) ]
    pr = product(*arr)
    print({i for i in pr})

find_the_kth(4, 24)