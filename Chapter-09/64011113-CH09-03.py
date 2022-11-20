def insertion_sort(list: list, sorted_list: list = None):
    sorted_list = [list.pop(0)] if sorted_list is None else sorted_list
    if not list:
        print("sorted")
        print(sorted_list)
    else:
        ref = list.pop(0)
        idx = find_sort_index(sorted_list, ref)
        sorted_list.insert(idx, ref)
        str_list = f"{sorted_list} {list}"
        if not list:
            str_list = f"{sorted_list}"
        print(f"insert {ref} at index {idx} : {str_list}")
        insertion_sort(list, sorted_list)
    # if sorted_list


def find_sort_index(sorted_list: list, value: int, idx_ref: int = None):
    idx_ref = len(sorted_list)-1 if idx_ref is None else idx_ref
    if value < sorted_list[idx_ref]:
        if idx_ref == 0:
            return idx_ref
        else:
            return find_sort_index(sorted_list, value, idx_ref-1)
    else:
        return idx_ref+1


input = [int(x) for x in input("Enter Input : ").split(" ")]
# input = [int(x) for x in "1 -4 4 -2 2 -3 4 5".split(" ")]
insertion_sort(input)
