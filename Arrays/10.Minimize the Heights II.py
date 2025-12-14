class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0

        arr.sort()

        # Initial difference without any modification
        ans = arr[-1] - arr[0]

        # Base small & big after adding/subtracting k
        small = arr[0] + k
        big = arr[-1] - k
        if small > big:
            small, big = big, small

        for i in range(1, n):
            if arr[i] - k < 0:
                continue

            min_height = min(small, arr[i] - k)
            max_height = max(big, arr[i - 1] + k)

            ans = min(ans, max_height - min_height)

        return ans


def main():
    arr = [1, 5, 8, 10]
    k = 2
    print("Original heights:", arr)
    sol = Solution()
    result = sol.getMinDiff(arr, k)
    print("Minimum possible difference:", result)  # Expected: 5

    arr2 = [3, 9, 12, 16, 20]
    k2 = 3
    print("\nOriginal heights:", arr2)
    print("k =", k2)
    print("Minimum possible difference:", sol.getMinDiff(arr2, k2))  # Common example: 11


if __name__ == "__main__":
    main()
