# Postfix Calculator

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

def post_fixeval(st):
    stack = Stack()
    
    for i in st:
        if i in "+-*/":
            operator = {'+': lambda x, y: x + y,
                        '-': lambda x, y: x - y,
                        '*': lambda x, y: x * y,
                        '/': lambda x, y: x / y,}
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            stack.push(operator[i](operand_1, operand_2))
        else:
            stack.push(float(i))
    return stack.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(post_fixeval(token)))