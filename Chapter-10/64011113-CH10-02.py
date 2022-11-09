# First Greater Value

def find_first_greater(list: list, key: list):
    for x in key:
        for i in range(len(list)):
            if x < list[i]:
                print(list[i]) 
                break
            elif i == len(list)-1:
                print("No First Greater Value")

input = input("Enter Input : ").split("/")
# input = "3 2 7 6 8/9".split("/")
ls, key = list(map(int, input[0].split(" "))), list(map(int, input[1].split(" ")))

find_first_greater(sorted(ls), key)