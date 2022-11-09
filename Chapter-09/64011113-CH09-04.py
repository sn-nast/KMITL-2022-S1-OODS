# Median
    
def insertion_sort(list: list):
    for i in range(1, len(list)):
        i_element = list[i]
        for j in range(i, -1, -1):
            if i_element < list[j-1] and j > 0:
                list[j] = list[j-1]
            else:
                list[j] = i_element
                break
    return list

def median(list: list):
    insertion_sort(list)
    size = len(list)
    if size == 1:
        return float(list[0])
    elif (size / 2) % 1 != 0:
        return float(list[size//2])
    else:
        x = size//2 - 1
        return (list[x]+list[x+1]) / 2

l = [e for e in input("Enter Input : ").split()]
# l = [e for e in "12 4 5 3 8 7 83".split()]
l=list(map(int, l))
for i in range(1, len(l)+1):
    list = l[:i]
    print(f"list = {list} : median = {median(list)}")