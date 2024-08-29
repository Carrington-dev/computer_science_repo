class Solution:
    def fib(self, n: int) -> int:
        arr =  [0, 1]
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])
        print(arr)
        return arr[n-1]

   