def findMinMaxSums(n, arr, k):
	# Write your code here
	arr = sorted(arr)
	if k == 1:
		return [sum(arr[k:]), sum(arr[:n-1])]
	else:
		return [sum(arr[k:]), sum(arr[:n-k])]


n = int(input())
arr = list(map(int, input().split()))
k = int(input())

result = findMinMaxSums(n, arr, k)
print(result[0], result[1])
