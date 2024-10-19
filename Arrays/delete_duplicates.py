def delete_duplicates(arr):
    if not arr: return arr

    # starting from 1 because the first element will always been written
    write_idx = 1
    for i in range(1,len(arr)):
        if arr[i] == arr[write_idx - 1]:
            continue # skip as its the same element
        else:
            arr[write_idx] = arr[i]
            write_idx += 1
    return arr[:write_idx]


    
           



a = [2,3,5,5,7,11,11,13]
print(delete_duplicates(a))