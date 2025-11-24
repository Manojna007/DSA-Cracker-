"""
Problem Statement:
Reverse a sequence (either an array of integers or a string).
- For an array, reverse its elements in place so the first becomes last, second becomes second last, etc.
- For a string, reverse its characters so the first character becomes last, and so on.

Sample Inputs and Outputs:
Array Input: [1, 4, 3, 2, 6, 5]
Array Output: [5, 6, 2, 3, 4, 1]

String Input: "abcdef"
String Output: "fedcba"
"""

def reverse_sequence(seq):
    # If input is a string, convert to list for in-place reversal
    is_string = isinstance(seq, str)
    arr = list(seq) if is_string else seq

    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    if is_string:
        return ''.join(arr)
    else:
        return arr

# Examples
array_input = [1, 4, 3, 2, 6, 5]
print("Reversed array:", reverse_sequence(array_input))  # Output: [5, 6, 2, 3, 4, 1]

string_input = "abcdef"
print("Reversed string:", reverse_sequence(string_input))  # Output: "fedcba"
