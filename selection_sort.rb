=begin
Natively, programming languages ​​already implement this sorting algorithm (selection_sort). However, knowing this algorithm
makes it easier to learn other sorting algorithms, such as quick_sort.

Before executing this code, we must know that its running time is O(n2), that is, this algorithm will grow quadratically,
being extremely slow.

Why?

Each time we search the array for the smallest value, we add the found value (based on the logic below) to the end of the new list,
and we remove it from the original list, after that we search again in the original list for the lowest value, and this process that was previously described
it is carried out until we find it the smallest value. In the end, we have ordered the array in an ascending order.
=end

def min_value(arr)
  lower_value = arr[0]
  lower_value_index = 0

  arr.length.times do |i| 
    if arr[i] < lower_value
      lower_value = arr[i] 
      lower_value_index = i
    end
  end
  return lower_value_index 
end

def selection_sort(arr)
  new_arr = []
  arr.length.times do |i|
    lower_value = min_value(arr)
    new_arr.append(arr.delete_at(lower_value))
  end
  return new_arr 
end

arr = [5,1,7,9,3]

puts selection_sort(arr)