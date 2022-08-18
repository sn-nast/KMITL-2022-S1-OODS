# Pyramid

print("*** Fun with Drawing ***")
size_input = int(input("Enter input : "))

rows = (2*2*(size_input-1))+1
half = (2*size_input)-1
sharp = '#'
dot = '.'

for row in range(1, rows+1):
    pack = int(row/2) if row <= half else int(row/2)-(row-(half))

    if row == 1 or row == rows:
        print(sharp*rows)
    elif row%2 == 0:
        print((sharp+dot)*pack, dot*(rows-(4*pack)), (dot+sharp)*pack, sep="")
    else:
        print((sharp+dot)*pack, sharp*(rows-(4*pack)),(dot+sharp)*pack, sep="")