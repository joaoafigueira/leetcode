=begin 
Binary search is a searching algorithm used in a sorted array. With binary search, we guess an intermediate number and eliminate half of the remaining numbers each time.

It is good to use binary search algorithm when we dont want it to iterate over each element.

Ex: 

Suppose we're searching for a specif number in a list. The list has 240.000 numbers. 

If the number  we need to find it is the last, in the worst case cenario using a linear search, we have to iterate each number.

Using Binary search, in each step we eliminate the numbers in the list cutting them in a half, until only the specific number remains.

In the example below, it is a small list but it is a good representation of the example above.
=end

def binary_search(list,item)
  low = 0
  high = list.length - 1

  while low <= high
    mid = (low + high) / 2
    guess = list[mid]
         
    if guess == item
      return mid
    elsif guess > item
      high = mid - 1
    else 
      low = mid + 1  
    end   
  end

  return nil
end      

list = [1,3,5,7,9]

puts binary_search(list, 3)