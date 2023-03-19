# Here we have a e.g. of "the recursive count",
# where the base case here it is found when the array reaches "[]". 
# The main point here, is that the count of the array it is how many times the recursive function is called.

def recursive_count(arr):
    if(arr == []):
        return 0
    return 1 + recursive_count(arr[1:])

recursive_count([1,2,3])