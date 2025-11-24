"""
Question Description:
Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last, and so on.

Sample Input and Output
Input:
arr[] = [1, 4, 3, 2, 6, 5]
Output:
[5, 6, 2, 3, 4, 1]
Explanation:
The first element (1) moves to the last position, the second element (4) moves to the second-last, and so on.
"""

def reverse_array(arr):
    # Initialize pointers: left at start, right at end
    left = 0
    right = len(arr) - 1

    # Continue swapping until pointers meet or cross
    while left < right:
        # Swap the elements at the current pointers
        arr[left], arr[right] = arr[right], arr[left]

        # Move pointers towards each other
        left += 1
        right -= 1

    # Return the reversed array (optional, as arr is modified in place)
    return arr


# Sample Input
arr = [1, 4, 3, 2, 6, 5]

# Calling the function
result = reverse_array(arr)

# Output the result
print("Reversed array:", result)
