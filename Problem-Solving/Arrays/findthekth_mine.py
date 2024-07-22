from itertools import permutations, product


def find_the_kth(n, k):
    a = permutations(n)
    for i in a:
        print(list(i))
    return list(a)

for i in range(6):
    print(find_the_kth([2, 3, 4], i))
