#Part 2: Binary Search Implementation

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            comparisons += 1
            left = mid + 1
        else:
            comparisons += 1
            right = mid - 1

    return -1, comparisons


# Main
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67

print("Sorted List:", arr)
print(f"Searching for {target} using Binary Search")

index, comparisons = binary_search(arr, target)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
print(f"Number of comparisons: {comparisons}")



