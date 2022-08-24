# วันหนึ่งฉันเดินเข้าป่า (ต่อ)

class Stack:
    
    def __init__(self, ls = None):
        self.items = [] if ls == None else ls
        self.__size = len(self.items)
    
    def __str__(self):
        string = ' '.join(str(element) for element in self.items) if self.size() != 0 else "Empty"
        return string
    
    def push(self, value):
        self.items.append(value)
        self.__size += 1
        
    def pop(self, index=-1):
        value_last_index = None
        if self.size() != 0:
            value_last_index = self.items.pop(index)
            self.__size -= 1
        return value_last_index
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return self.__size
    
    def copy(self, destination_stack):
        for i in self.items:
            destination_stack.push(i)

    def change_member(self, index, value):
        self.items[index] = value
    

def tree_command(input_cmd):
    tree_stack = Stack()
    
    for cmd in input_cmd:
        if cmd == 'B':
            tree_can_count = 0
            max_height_tree = 0
            
            temp_tree_stack = Stack()
            tree_stack.copy(temp_tree_stack)
            
            while temp_tree_stack.size()>1:
                last_tree = temp_tree_stack.pop()
                before_last_tree = temp_tree_stack.peek()
                
                if before_last_tree > last_tree and before_last_tree > max_height_tree: 
                    tree_can_count += 1
                    max_height_tree = before_last_tree
                    
                max_height_tree = last_tree if max_height_tree == 0 else max_height_tree
                
            print(tree_can_count + 1 if temp_tree_stack.size() == 1 else 0)
        
        elif cmd == 'S':
            for idx, value in enumerate(tree_stack.items):
                value += (2 if value % 2 != 0 else -1 if value-1 >= 1 else -(value-1))
                tree_stack.change_member(idx, value)
        
        else:
            cmd = [i for i in str(cmd).split(" ")]
            if cmd[0] == 'A':
                tree_stack.push(float(cmd[1]))
    return input_cmd

S = Stack()
inp = input('Enter Input : ').split(',')
tree_command(inp)