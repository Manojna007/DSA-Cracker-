"""
Bubble sort is like sorting a stack of blocks.

Imagine you have a stack of blocks of different colors. You want to arrange them from the smallest to the biggest.

Look at the first two blocks. If the first block is bigger than the second, you swap them.
Then move to the next pair of blocks. Keep comparing and swapping until you reach the end of the stack.
After one round, the biggest block will be at the end.
Now, start again from the beginning, but this time, you don't need to check the last block because it's already in the right place.
Keep doing this until all the blocks are sorted.
So, bubble sort is just moving the biggest blocks to the end, one round at a time, until everything is in order!
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swapped = True
        if not swapped:
            break

# Larger array example
a = [64, 34, 25, 12, 22, 11, 90, 88, 76, 45, 67, 54, 32, 21, 78, 85, 29, 18, 10, 5]
bubble_sort(a)
print(*a) # * is an unpacking operator used to pass indivial value from a list to print function which allows to print without comma and [] as a list

