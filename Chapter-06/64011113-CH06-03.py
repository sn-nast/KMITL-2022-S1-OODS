#  GCD

def find_gcd(g_number, l_number):
    answer = 0
    l_number = abs(l_number)
    g_number = abs(g_number)
    
    if l_number > g_number:
        g_number, l_number = l_number, g_number
    elif g_number == 0 and l_number == 0:
        return False
    
    if l_number == 0:
        return g_number
    elif g_number%l_number == 0:
        answer = l_number
    else:
        answer = find_gcd(l_number, g_number%l_number)
    return answer

input = list(map(int, input("Enter Input : ").split(" ")))
answer = find_gcd(input[0], input[1])
if input[1] > input[0]:
    input = [input[1], input[0]]
if answer is False:
    print("Error! must be not all zero.")
else:
    print(f"The gcd of {input[0]} and {input[1]} is : {answer}")