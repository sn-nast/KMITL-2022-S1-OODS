# Reverse Sort List
def sort_list(list: list):
    insertion_sort(list)
    print(f"List after Sorted : {list}")

def insertion_sort(list:list, round=1):
    n = len(list) 
    if n > round:
        key = list[round]
        new_index = rearrange(list, key, round-1)
        list[new_index+1] = key
        insertion_sort(list, round+1)

def rearrange(list:list, key, index):
    if index >= 0 and key > list[index]:
        list[index+1] = list[index]
        index = rearrange(list, key, index-1)
    return index

list_input = input("Enter your List : ").split(',')
# list_input = "0,0,0,0,0".split(',')
list_input = list(map(int, list_input))
sort_list(list_input)