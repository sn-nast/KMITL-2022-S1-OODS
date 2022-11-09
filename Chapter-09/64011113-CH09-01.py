def bubble_sort(list: list, idx: int = 0, count_ordered: int = 0):
    if count_ordered == len(list):
        return list
    elif idx < len(list)-1:
        if list[idx] > list[idx+1]:
            list[idx], list[idx+1] = list[idx+1], list[idx]
        bubble_sort(list, idx+1, count_ordered)
        return list
    bubble_sort(list, 0, count_ordered+1)

input = [int(x) for x in input("Enter Input : ").split(" ")]
# input = [int(x) for x in "1 2 3 4 5".split(" ")]
print(bubble_sort(input))