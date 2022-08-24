# Stack

class Stack:
    
    def __init__(self, list = None):
        self.items = [] if list == None else list
        self.__size = len(self.items)
    
    def __str__(self):
        string = ' '.join(str(element) for element in self.items) if self.size() != 0 else "Empty"
        return string
    
    def push(self, value):
        self.items.append(value)
        self.__size += 1
        print(f"Add = {value} and Size = {self.size()}")
        
    def pop(self, index=-1):
        value_last_index = None
        if self.size() != 0:
            value_last_index = self.items.pop(index)
            self.__size -= 1
            print(f"Pop = {value_last_index} and Index = {self.size()}") 
        else:
            value_last_index = -1
            print(value_last_index)
        return value_last_index
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return self.__size

input_cmd = [i for i in input("Enter Input : ").split(",")]
stack_list = Stack()
for i in input_cmd:
    if i == 'P':
        stack_list.pop()
    else:
        cmd = [k for k in i.split()]
        if cmd[0] == 'A':
            stack_list.push(int(cmd[1]))

print(f"Value in Stack = {stack_list}")