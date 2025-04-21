#Part 2 Merge Sort Implementation

def merge_sort(arr):
    stats = {"comparisons": 0, "accesses": 0}

    def merge(left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            stats["comparisons"] += 1
            stats["accesses"] += 2  
            if left[i] <= right[j]:
                merged.append(left[i])
                stats["accesses"] += 1 
                i += 1
            else:
                merged.append(right[j])
                stats["accesses"] += 1
                j += 1

        while i < len(left):
            merged.append(left[i])
            stats["accesses"] += 1
            i += 1

        while j < len(right):
            merged.append(right[j])
            stats["accesses"] += 1
            j += 1

        return merged

    def sort(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr
        mid = len(sub_arr) // 2
        left = sort(sub_arr[:mid])
        right = sort(sub_arr[mid:])
        stats["accesses"] += len(sub_arr) 
        return merge(left, right)

    sorted_arr = sort(arr)
    return sorted_arr, stats["comparisons"], stats["accesses"]


original_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comparisons, accesses = merge_sort(original_list)

print("Original List:", original_list)
print("Sorted using Merge Sort:", sorted_list)
print("Number of comparisons:", comparisons)
print("Number of array accesses:", accesses)
