# Binary Search

def bi_search(left: int, right: int, arr: list, key: int):
    mid = (left+right) // 2
    # print(f"key: {key} \tleft: {arr[left]}, \t mid: {arr[mid]} \t right: {arr[right]}")
    # print(f"\t\tleft: {left}, \t mid: {mid} \t right: {right}")
    if mid == left:
        return arr[mid] == key
    if right > left:
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            # print(f"{key} > {arr[mid]}")
            return bi_search(mid+1, right, arr, key)
        elif arr[mid] > key:
            # print(f"{key} < {arr[mid]}")
            return bi_search(left, mid-1, arr, key)


inp = input('Enter Input : ').split('/')
# inp = "33 2 11 82 77 -28 15 76 9 64/-28".split('/')
# inp = "33 2 11 82 77 28 15 76 9 64/50".split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
