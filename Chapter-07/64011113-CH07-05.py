"""Chapter : 7 - item : 5 - Expression Tree

ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  
โดย Operator จะมีแค่ + - * /ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น 
Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

"""

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
        
class BST:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.left: 'BST.Node' = None
            self.right: 'BST.Node' = None
            
        def __str__(self):
            return str(self.data)
        
    def __init__(self):
        self.root: self.Node = None
        
    def insert(self, data):
        new = self.Node(data) if isinstance(data, str) else data
        if self.root is None:
            self.root = new
        else:
            temp = self.root
            while temp is not None:
                if temp.right is None:
                    temp.right = new
                    break
                elif temp.left is None:
                    temp.left = new
                    break
                temp = temp.right
        return self.root
    
    def print_tree(self, node: Node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

class ReversePolishNotation:
    
    def __init__(self, cmd: list):
        self.stack = Stack()
        self.tree = BST()
        self.__read_cmd(cmd)
        
    def __read_cmd(self, cmd: list):
        stack = self.stack
        for i in cmd:
            if i in "+-*/":
                bst = BST()
                bst.insert(data=i)
                bst.insert(stack.pop())
                bst.insert(stack.pop())
                stack.push(bst.root)
            else:
                stack.push(i)
        self.tree.root = stack.pop()
        return self.tree.root
    
    def print_result(self):
        print("Tree :")
        self.tree.print_tree(self.tree.root)
        print("--------------------------------------------------")
        print(f"Infix : {self.to_infix(self.tree.root)}")
        print(f"Prefix : {self.to_prefix(self.tree.root)}")
    
    def to_infix(self, root: 'BST.Node', list: list=[]):
        # postorder
        if root is not None:
            if root.data in "+-*/":
                list.append('(')
            self.to_infix(root.left, list)
            list.append(root.data)
            self.to_infix(root.right, list)
            if root.right is not None and root.left is not None:
                list.append(')')
        return ''.join(list)
    
    def to_prefix(self, root: 'BST.Node', list: list=[]):
        # preorder
        if root is not None:
            list.append(root.data)
            self.to_prefix(root.left, list)
            self.to_prefix(root.right, list)
        return ''.join(list)
    

cmd = [x for x in input("Enter Postfix : ")]
# cmd = [x for x in "ab+c*de-fg+*-"]

postfix = ReversePolishNotation(cmd)
postfix.print_result()