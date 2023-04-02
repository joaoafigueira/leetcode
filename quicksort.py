
# Quicksort it is a sorting algorithm, that uses the divide and conquering thinking and 
# it is much faster than selecion sort, where the big O grows accordingly the pivot.
# Below we have an example of the algorithm.


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        minors = [i for i in arr[1:] if i <= pivot] 
        bigger = [i for i in arr[1:] if i > pivot]   
        return quicksort(minors) + [pivot] + quicksort(bigger)

print(quicksort([2,4,10,3]))