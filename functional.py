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


