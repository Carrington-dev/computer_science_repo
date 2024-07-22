from itertools import permutations


def get_all_subsets(nums):
    all_subsets = []
    for i in range(len(nums)):
        m = [ nums[i] ]
        c = (nums[:i] + nums[i+1:])
        for i in permutations(c):
            all_subsets.append(list(i) + m)
        

    return (all_subsets)

print(get_all_subsets([2, 3, 4]))