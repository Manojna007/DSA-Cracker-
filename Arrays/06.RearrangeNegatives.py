class Solution:
    def segregateElements(self, arr):
        """
        Rearranges arr in-place so that:
        - All non-negative elements come first in their original order.
        - All negative elements come afterwards in their original order.
        Time:  O(n)
        Space: O(n) extra (two temporary lists), but same arr object is modified.
        """
        pos = []  # to store non-negative elements in order
        neg = []  # to store negative elements in order

        # 1. Partition into two lists while preserving order
        for x in arr:
            if x >= 0:
                pos.append(x)
            else:
                neg.append(x)

        # 2. Overwrite arr in-place: first positives, then negatives
        i = 0
        for x in pos:
            arr[i] = x
            i += 1
        for x in neg:
            arr[i] = x
            i += 1
        # No return needed; arr is modified in-place


def main():
    arr = [1, -1, 3, 2, -7, -5, 11, 6]
    print("Before:", arr)

    sol = Solution()
    sol.segregateElements(arr)  # modifies arr in-place

    print("After: ", arr)


if __name__ == "__main__":
    main()
