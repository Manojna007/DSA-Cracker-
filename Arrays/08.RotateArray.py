class Solution:
    def rotate(self, arr):
        """
        Rotates arr by one position clockwise (right) in-place.
        Example: [1, 2, 3, 4, 5] -> [5, 1, 2, 3, 4]
        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)
        if n <= 1:
            return  # nothing to do

        last = arr[-1]           # store last element
        # shift elements to the right
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last            # put last element at front

def main():
    arr = [1, 2, 3, 4, 5]
    print("Before:", arr)
    sol = Solution()
    sol.rotate(arr)
    print("After: ", arr)  # [5, 1, 2, 3, 4]

if __name__ == "__main__":
    main()
