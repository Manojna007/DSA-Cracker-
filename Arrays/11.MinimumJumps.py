class Solution:
    def minJumps(self, arr):
        """
        Find minimum jumps to reach array end where arr[i] = max forward steps from i.

        Time Complexity: O(n) - single pass
        Space Complexity: O(1) - constant variables only
        """
        n = len(arr)
        if n <= 1: return 0
        if arr[0] == 0: return -1

        jumps, currEnd, maxReach = 0, 0, 0
        for i in range(n - 1):
            maxReach = max(maxReach, i + arr[i])
            if i == currEnd:
                jumps += 1
                currEnd = maxReach
                if currEnd >= n - 1: return jumps
                if i == maxReach: return -1
        return -1


def main():
    sol = Solution()
    print("Array:", [2, 2, 0, 2, 1], "→", sol.minJumps([2, 2, 0, 2, 1]))  # 3
    print("Array:", [2, 3, 1, 1, 4], "→", sol.minJumps([2, 3, 1, 1, 4]))  # 2
    print("Array:", [0, 1, 2], "→", sol.minJumps([0, 1, 2]))  # -1


if __name__ == "__main__":
    main()
