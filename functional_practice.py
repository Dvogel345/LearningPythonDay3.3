
##                       Functional Prompt
# Implement a function that will flatten and sort an array of integers in 
# ascending order, and which adheres to a functional programming paradigm
def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_and_sort(['12','23','34','45']))
# 1. How does this solution ensure data immutability?

# the deifned array makes it so the data can't be changed?

# 2. Is this solution a pure function? Why or why not?

# This is not a pure function as it displays the num_list globally instead of 
# within a function 

# 3. Is this solution a higher order function? Why or why not?

# This solution is not a HOF as it doesnt take in a function as a param or return a function
# in the output

# 4. Would it have been easier to solve this problem using a different programming style?

# 5. Why in particular is functional programming a helpful paradigm when solving this problem?


            
                    
            
         
