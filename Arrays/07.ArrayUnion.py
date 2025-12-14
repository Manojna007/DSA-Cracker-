class Solution:
    def findUnion(self, a, b):
        """
        Returns the union of arrays a and b as a list of distinct elements.
        Order does not matter here because the driver will print in sorted order.
        """
        union_set = set(a) | set(b)
        return list(union_set)


def main():
    # Example input arrays
    a = [1, 2, 2, 3, 4]
    b = [3, 4, 4, 5, 6]

    sol = Solution()
    result = sol.findUnion(a, b)

    # Driver in many platforms will sort, but we can show sorted here for clarity
    print("Array a:", a)
    print("Array b:", b)
    print("Union  :", sorted(result))


if __name__ == "__main__":
    main()
