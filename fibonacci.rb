
def fibonacci(count)
    if count <= 1
       return count
    else 
      return fibonacci(count - 1) + fibonacci(count - 2) 
    end
end

puts fibonacci(8)

