# Yind and Yang

size_input = int(input("Enter Input : "))

sharp = "#"
dot = "."
plus = "+"
pair = sharp+plus

half_row = int(size_input+2)
rows = 2*(half_row)

def change_format(char_list):
    for i, char in enumerate(char_list):
        if char==sharp:
            char_list[i] = plus
        elif char == plus:
            char_list[i] = sharp
    return char_list

def make_half_pattern(reverse=False):
    pattern = []
    for row in range(1, half_row+1):
        char_size = [   half_row-row, 
                        row-1, 
                        1, 
                        size_input if row>1 and row<half_row else 0,
                        size_input+1 if row==1 or row==half_row else 1]
        row_pattern = [dot, sharp, pair, sharp, plus]
        
        if reverse==True:
            char_size.reverse()
            row_pattern.reverse()
            change_format(row_pattern)
        
        pattern.append(''.join([row_pattern[i]*char_size[i] for i in range(5)]))

    return pattern if reverse==False else list(reversed(pattern))

print('\n'.join(make_half_pattern() + make_half_pattern(True)))