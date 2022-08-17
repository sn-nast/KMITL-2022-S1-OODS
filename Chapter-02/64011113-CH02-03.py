# new Range
# TODO

def range(end, start=0.0, step=1.0):
    range_list = []
    i = start
    while i <= end:
        i += step
        range_list.append(i)
    
    # return range_list
    # print(tuple(range_list))
    print(range_list)

print("*** New Range ***")
input_num = float(input("Enter Input : "))
# num_list = []
range(5)