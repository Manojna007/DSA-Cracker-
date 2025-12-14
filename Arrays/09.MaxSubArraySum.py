class Solution:
    def maxSubarraySum(self, arr):
        """
        Returns the maximum sum of any non-empty contiguous subarray.
        Time:  O(n)
        Space: O(1)
        """
        max_ending_here = arr[0]
        max_so_far = arr[0]

        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


def main():
    # Test case 1: Mixed positive/negative
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    result1 = sol.maxSubarraySum(arr1)
    print(f"Array: {arr1}")
    print(f"Max subarray sum: {result1}")  # 6 ([4, -1, 2, 1])

    # Test case 2: All negative
    arr2 = [-1, -2, -3, -4]
    result2 = sol.maxSubarraySum(arr2)
    print(f"Array: {arr2}")
    print(f"Max subarray sum: {result2}")  # -1 (largest single element)

    # Test case 3: Single element
    arr3 = [5]
    result3 = sol.maxSubarraySum(arr3)
    print(f"Array: {arr3}")
    print(f"Max subarray sum: {result3}")  # 5


if __name__ == "__main__":
    main()
