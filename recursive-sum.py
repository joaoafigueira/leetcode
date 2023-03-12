# Divide and conquer algorithm - A way of thinking about a problem, in short, we're always find a way to divide a specific problem in its smaller version.

# Below we have a e.g. "the recursive sum", we used the divide and conquer algorithm there, first we have it to discover the base case, 
# which is the simplest case of the problem, an array of one element, after that we have to divide our problem to find this simplest base case. 

# So to divide our problem we're using an array, and we sum the first element plus the rest of the array e.g. : 2 + recursive_sum(4,6) = 10, 2 + 10 = 12.
# The base case here it is found in the second call of the recursive_sum(4,6), the array of one element it is [6], we sum 6 plus 4, and after that plus 2, 
# we can sum plus 2 because recursion save the state of the functions.

def recursive_sum(arr):
    if (arr == []):
        return print(0)
    return arr[0] + recursive_sum(arr[1:])

recursive_sum([2,4,6])