"""
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Note: You need to solve this problem without utilizing the built-in sort function.

Dutch National Flag algorithm for sorting an array containing only 0s, 1s, and 2s.

    Steps:
    1. Initialize three pointers:
       - low: points to the start, boundary where 0s should be placed
       - mid: current index for scanning the array
       - high: points to the end, boundary where 2s should be placed

    2. Traverse the array with 'mid' until it exceeds 'high'.

    3. If the element at 'mid' is 0:
       - Swap it with the element at 'low'.
       - Increment both 'low' and 'mid'.
       - This pushes 0s to the beginning of the array.

    4. If the element at 'mid' is 1:
       - Just move 'mid' one step forward.
       - 1s remain in the middle section.

    5. If the element at 'mid' is 2:
       - Swap it with the element at 'high'.
       - Decrement 'high' (because this area gets filled with 2s).
       - Do NOT increment 'mid' here as the swapped element needs to be checked.

    6. Repeat the above steps until 'mid' passes 'high'.

    This algorithm sorts the array in a single pass (O(n) time complexity) and uses only constant extra space (O(1)) because it rearranges elements in-place.
"""

def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# Example usage
a = [2, 0, 1, 2, 1, 0, 0, 2, 1]
sort_012(a)
print(*a)

