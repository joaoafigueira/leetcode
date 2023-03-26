# Below there are two ways to find the biggest value in an array. The first is without using recursive function, and the second  it is using recursive function.
# Obs: the way of the recursive function works is find the two biggest values in the list and compare then in the final.

def find_the_biggest_value(arr):
    if (arr == []):
        return 0
    number = 0
    for element in arr:
        if(element > number):
            number = element
    return number     
            
print(find_the_biggest_value([3,2,5,6]))

def find_the_biggest_value_recursive(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_the_biggest_value_recursive(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max 
            
print(find_the_biggest_value_recursive([3,2,5,6]))

            

