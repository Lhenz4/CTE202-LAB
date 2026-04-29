######################################################
#Task 2: Merge Sort
######################################################
def merge_sort(arr):
    comparisons = 0
    array_accesses = 0

    if arr is None:
        return None, 0, 0
    if len(arr) <= 1:
        return arr, 0, 0

    def merge(left, right):
        nonlocal comparisons, array_accesses
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            array_accesses += 2  

            if left[i] <= right[j]:
                merged.append(left[i])
                array_accesses += 1
                i += 1
            else:
                merged.append(right[j])
                array_accesses += 1
                j += 1

       
        while i < len(left):
            merged.append(left[i])
            array_accesses += 1
            i += 1

        while j < len(right):
            merged.append(right[j])
            array_accesses += 1
            j += 1

        return merged

    def merge_sort_recursive(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = merge_sort_recursive(a[:mid])
        right = merge_sort_recursive(a[mid:])
        return merge(left, right)

    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, comparisons, array_accesses


# Example usage
data = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comparisons, accesses = merge_sort(data.copy())

print("Original List:", data)
print("Sorted using Merge Sort:", sorted_list)
print("Number of comparisons:", comparisons)
print("Number of array accesses:", accesses)