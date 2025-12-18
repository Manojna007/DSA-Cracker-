class Solution:
    def findDuplicates(self, arr):
        """
        Return all values that appear exactly twice in arr (values in [1, n]).

        Time Complexity:  O(n)  - single pass over the array
        Space Complexity: O(1)  - ignores output list, modifies arr in-place
        """
        res = []
        for x in arr:
            idx = abs(x) - 1          # map value x to index x-1
            if arr[idx] < 0:          # already visited once → duplicate
                res.append(abs(x))
            else:
                arr[idx] = -arr[idx]  # mark as visited by negating
        return res


def main():
    sol = Solution()

    arr1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print("Array:", arr1)
    print("Duplicates:", sol.findDuplicates(arr1))   # [2, 3]

    arr2 = [1, 1, 2]
    print("Array:", arr2)
    print("Duplicates:", sol.findDuplicates(arr2))   # [1]

    arr3 = [1, 2, 3, 4]
    print("Array:", arr3)
    print("Duplicates:", sol.findDuplicates(arr3))   # []

if __name__ == "__main__":
    main()
