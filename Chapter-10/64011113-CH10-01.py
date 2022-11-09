# Binary Search

def bi_search(left: int, right: int, arr: list, key: int):
    if right > left:
        mid = (left+right) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            return bi_search(left, mid-1, arr, key)
        elif arr[mid] > key:
            return bi_search(mid+1, right, arr, key)
    else:
        return False

inp = input('Enter Input : ').split('/')
# inp = "33 2 11 82 77 28 15 76 9 64/29".split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))