"""
###################################################
# Task 1: Counting Sort
###################################################

def counting_sort(arr):
    if not arr:
        return []

    # maximum value
    max_val = max(arr)

    # Ccount array
    count = [0] * (max_val + 1)

    # Count the frequency of each element
    for num in arr:
        count[num] += 1

    # Build the sorted output
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))

"""
###################################################
# Task 2: Radix Sort
###################################################

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  

    # Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count[i] to store actual position
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (stable sort)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy output to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number
    max_val = max(arr)

    exp = 1
    # Apply counting sort for each digit
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr


# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))

