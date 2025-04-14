# Part 1: Sequential Search Implementation 

def sequential_search(arr, target):
    comparisons = 0  

    for index, value in enumerate(arr):
        comparisons += 1  
        if value == target:
            return index, comparisons  

    return -1, comparisons  

sample_list = [23, 45, 12, 67, 89, 34, 56]
target_value = 67

print(f"List: {sample_list}")
print(f"Searching for {target_value} using Sequential Search")

index, comparisons = sequential_search(sample_list, target_value)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
print(f"Number of comparisons: {comparisons}")
