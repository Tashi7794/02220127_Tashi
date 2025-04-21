def quick_sort(arr):
    comparisons, swaps = 0, 0

    def partition(arr, low, high):
        nonlocal comparisons, swaps
        mid = (low + high) // 2
        pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        pivot_candidates.sort(key=lambda x: x[0])
        pivot, pivot_idx = pivot_candidates[1]

        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        swaps += 1

        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quick_sort_rec(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_rec(arr, low, pi - 1)
            quick_sort_rec(arr, pi + 1, high)

    quick_sort_rec(arr, 0, len(arr) - 1)
    return arr, comparisons, swaps

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, num_comparisons, num_swaps = quick_sort(arr)
print("Original List:", [38, 27, 43, 3, 9, 82, 10])
print("Sorted using Quick Sort:", sorted_arr)
print("Number of comparisons:", num_comparisons)
print("Number of swaps:", num_swaps)
