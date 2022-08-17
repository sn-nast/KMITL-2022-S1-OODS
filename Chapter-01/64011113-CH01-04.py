# TODO

# print("*** Fun with Drawing ***")
# size_input = int(input("Enter input : "))

# print('#')
# print('.')
# odd สลับ
#################
rows = 17
cols = 17
sharp = '#'
star = '*'

for row in range(1, rows+1):
    if row == 1 or row == rows:
        print(sharp*rows)
    print(row) 