"""
##########################################
# Sequential Search Algorithm
##########################################

def sequential_search(arr, target):
    comparisons = 0
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons  
    
    return -1, comparisons  

# Example usage
data = [23, 45, 12, 67, 89, 34, 56]
target = 67

index, comparisons = sequential_search(data, target)

print("List:", data)
print("Searching for", target, "using Sequential Search")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)

"""
###################################################
#Iterative Binary Search Algorithm
###################################################
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0

    while left <= right:
        mid = (left + right) // 2
        count += 1

        if arr[mid] == target:
            return mid, count
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, count


# Main
data = [12, 23, 34, 45, 56, 67, 89]
target = 67

index, comparisons = binary_search(data, target)

print("Sorted List:", data)
print("Searching for", target, "using Binary Search")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)

"""
####################################################
# Recursive Binary Search Algorithm
#####################################################
def binary_search_recursive(arr, target, left, right, count=0):
    if left > right:
        return -1, count

    mid = (left + right) // 2
    count += 1

    if arr[mid] == target:
        return mid, count
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, count)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, count)


# Main
data = [12, 23, 34, 45, 56, 67, 89]
target = 67

index, comparisons = binary_search_recursive(data, target, 0, len(data) - 1)

print("Sorted List:", data)
print("Searching for", target, "using Binary Search")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)

"""