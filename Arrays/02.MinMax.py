"""
### Pairwise Comparison Method

**Key Idea:**
Compare elements in pairs to reduce the number of comparisons.

#### Steps:

1. **Initialization:**
   - If the array length is **even**:
     - Set `min` to the smaller of the first two elements.
     - Set `max` to the larger of the first two elements.
     - Start loop from index `2`.
   - If **odd**:
     - Set both `min` and `max` to the first element.
     - Start loop from index `1`.

2. **Process Pairs:**
   - Traverse the array two elements at a time.
   - For each pair:
     - Compare the two elements to each other (1st comparison).
     - Compare the smaller with `min` (2nd comparison).
     - Compare the larger with `max` (3rd comparison).
   - Total per pair: **3 comparisons** (instead of 4 in naive way).

#### Example:

Array: `[5, 2, 9, 1, 6]`
- Odd length, so `min = max = 5`.
- Check pairs:
  - Pair `(2, 9)`: 2 < 9
    - Compare 2 with min → `min = 2`
    - Compare 9 with max → `max = 9`
  - Pair `(1, 6)`: 1 < 6
    - Compare 1 with min → `min = 1`
    - Compare 6 with max → (no change, still 9)

**Final Result:**
- Minimum: `1`
- Maximum: `9`
"""


def find_min_max(arr):
    n = len(arr)
    # Initialize min and max
    if n % 2 == 0:
        minimum = min(arr[0], arr[1])
        maximum = max(arr[0], arr[1])
        i = 2
    else:
        minimum = maximum = arr[0]
        i = 1
    while i < n - 1:
        if arr[i] < arr[i + 1]:
            minimum = min(minimum, arr[i])
            maximum = max(maximum, arr[i + 1])
        else:
            minimum = min(minimum, arr[i + 1])
            maximum = max(maximum, arr[i])
        i += 2
    return minimum, maximum

# Example usage
arr = [1, 4, 3, -5, -4, 8, 6]
minimum, maximum = find_min_max(arr)
print("Minimum element:", minimum)
print("Maximum element:", maximum)
