# Parenthesis Matching

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

def parent_matching(str):
    stack = Stack()
    i = 0
    error = 0
    
    while i < len(str) and error == 0:
        char = str[i]
        if char in '{[(':
            stack.push(char)
        else:
            if char in '}])':
                if stack.size() > 0:
                    if not match(stack.pop(), char):
                        error = 1
                else: 
                    error = 2
        i += 1
        
    if error == 0 and stack.size() > 0:
        error = 3
    
    return error, char, i, stack
                
def match(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

input = ''.join([str(i) for i in input("Enter expresion : ").split()])
error, char, i , stack = parent_matching(input)
print(input, end=" ")
if error == 1:
    print('Unmatch open-close')
elif error == 2:
    print('close paren excess')
elif error == 3:
    print('open paren excess  ', stack.size(), ": ", end='')
    for element in stack.items:
        print(element, sep='', end='')
else:
    print("MATCH")