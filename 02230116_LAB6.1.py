##############################################################
#Task 1: Quick Sort
##############################################################

def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def median_of_three(a, low, high):
        mid = (low + high) // 2
        trio = [(a[low], low), (a[mid], mid), (a[high], high)]
        trio.sort(key=lambda x: x[0])
        return trio[1][1]  
    
    def partition(a, low, high):
        nonlocal comparisons, swaps
        
        pivot_index = median_of_three(a, low, high)
        a[pivot_index], a[high] = a[high], a[pivot_index]
        swaps += 1
        
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps += 1

        a[i + 1], a[high] = a[high], a[i + 1]
        swaps += 1
        return i + 1

    def quicksort_recursive(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quicksort_recursive(a, low, pi - 1)
            quicksort_recursive(a, pi + 1, high)

    quicksort_recursive(arr, 0, len(arr) - 1)
    return arr, comparisons, swaps


# Example usage
data = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comparisons, swaps = quick_sort(data.copy())

print("Original List:", data)
print("Sorted using Quick Sort:", sorted_list)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)