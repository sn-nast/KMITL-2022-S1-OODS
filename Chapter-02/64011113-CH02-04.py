# Sum

def sum_of_three(numbers):
    if len(numbers) < 3:
        print("Array Input Length Must More Than 2")
        return
    
    final_list = []
    target_sum = 5
    for idx_1 in range(0, len(numbers)-2):
        for idx_2 in range(idx_1+1, len(numbers)-1):
            for idx_3 in range(idx_2+1, len(numbers)):
                if numbers[idx_1] + numbers[idx_2] + numbers[idx_3] == target_sum:
                    list_of_these_numbers = []
                    list_of_these_numbers.extend([numbers[idx_1], numbers[idx_2], numbers[idx_3]])
                    list_of_these_numbers.sort()
                    if (list_of_these_numbers not in final_list) and (set(list_of_these_numbers) not in [set(x) for x in final_list]):
                        final_list.append(list_of_these_numbers)
                        
    print(final_list)

input_num = [int(n) for n in input("Enter Your List : ").split()]
sum_of_three(input_num)