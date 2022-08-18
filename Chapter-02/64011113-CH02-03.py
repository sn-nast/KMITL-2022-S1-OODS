# new Range

def range(*numbers):
    start = 0.0
    end = 0.0
    step = 1.0
    range_list = []
    
    if len(numbers) == 3:
        start, end, step = numbers
    elif len(numbers) == 2:
        start, end = numbers
    elif len(numbers) == 1:
        end = numbers[0]
        
    max_decimal_places = 0
    for i in numbers:
        decimal_places = str(i)[::-1].find('.')
        if decimal_places > max_decimal_places:
            max_decimal_places = decimal_places
            
    i = start
    while i < end:
        range_list.append(round(i, max_decimal_places))
        i += step
    return tuple(range_list)

print("*** New Range ***")
input_num = [float(i) for i in input("Enter Input : ").split()]
print(range(*input_num))