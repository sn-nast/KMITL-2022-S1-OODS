def selection_sort(list: list) -> str:
    for end in range(len(list)-1, 0, -1):
        max = list[end]
        max_i = end
        if max < 0:
            continue
        for i in range(0, end+1):
            if list[i] > max:
                max = list[i]
                max_i = i
        while list[end] < 0:
            end -= 1
        list[end], list[max_i] = list[max_i], list[end]
    return " ".join([str(x) for x in list])

input = [int(x) for x in input("Enter Input : ").split(" ")]
# input = [int(x) for x in "6 3 -2 5 -8 2 -2".split(" ")]
print(selection_sort(input))