def insertion_sort(
    list: list, 
    # idx: int = 0, 
    idx_ref: int = -1, 
    sorted_list: list = []):
    
    if len(sorted_list) == 0:
        sorted_list.append(list.pop(0))
        print(f"list: {list}, sort: {sorted_list}")
    
    if len(list) == 0:
        print(f"sorted")
        return sorted_list
    
    if abs(idx_ref) > len(sorted_list):
        return sorted_list
    
    if list[0] > sorted_list[idx_ref]:
        print(f"            {sorted_list}")
        print(f"            {list[0]} > {sorted_list[idx_ref]}")
        x = list.pop(0)
        x_i = idx_ref
        sorted_list.insert(x+1, x)
        # else
        print(f"insert {x} at index {x_i+1} : {sorted_list} {list if len(list) != 0 else ''}")
        # insertion_sort(list, 0, sorted_list)
    else:
        insertion_sort(list, idx_ref-1, sorted_list)
        # checking = list.pop(idx)


# input = [int(x) for x in input("Enter Input : ").split(" ")]
input = [int(x) for x in "1 3 4 2".split(" ")]
print(insertion_sort(input))