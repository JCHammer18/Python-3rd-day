def flatten_and_sort(arr):
    out = []
    for item in arr:
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
            out.append(item)



    return sorted(out)

first_collection = [1, [55, 17, 12],3, [22, 19, 35], 9,2]
print(flatten_and_sort(first_collection))
print(first_collection)

"""
How does this solution ensure data immutability?
    passes back a different collection than the one passed in

Is this solution a pure function? Why or why not?
    yes- it does not produce side effects and does not retain state

Is this solution a higher order function? Why or why not?
    No - because it is not take a function as a parameter

Would it have been easier to solve this problem using a different programming style?
    no- this seems easy enough and works well   

Why in particular is functional programming a helpful paradigm when solving this problem? 
     Because it uses a pure function the results will consistent 
"""
