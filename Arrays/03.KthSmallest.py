def quickSelect(arr, left, right, k):
    if left <= right:
        pivot = partition(arr, left, right)
        if pivot == k - 1:
            return arr[pivot]  # Kth smallest found
        elif pivot > k - 1:
            return quickSelect(arr, left, pivot - 1, k)
        else:
            return quickSelect(arr, pivot + 1, right, k)
    return -1  # K is out of bounds

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

# Example: Find 3rd smallest and 3rd largest
arr = [7, 10, 4, 3, 20, 15]
k = 3
n = len(arr)
print(f"{k}th Minimum: {quickSelect(arr[:], 0, n - 1, k)}")             # Output: 7
print(f"{k}th Maximum: {quickSelect(arr[:], 0, n - 1, n - k + 1)}")     # Output: 10
