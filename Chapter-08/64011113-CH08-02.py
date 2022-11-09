# Closest Value

class BST:
    
    class Node:
        def __init__(self, data: int):
            self.data = data
            self.__left: 'BST.Node' = None
            self.__right: 'BST.Node' = None
            
        def __str__(self):
            return str(self.data)
        
        def get_left(self) -> 'BST.Node':
            return self.__left
        
        def _set_left(self, data):
            self.__left = data if isinstance(data, BST.Node) else BST.Node(data)
            
        def get_right(self):
            return self.__right
        
        def _set_right(self, data):
            self.__right = data if isinstance(data, BST.Node) else BST.Node(data)
            
        def is_node(other):
            return isinstance(other, BST.Node)
            
    def __init__(self):
        self.root: BST.Node = None
        
    def insert(self, data):
        new = self.Node(data)
        
        if self.root is None:
            self.root = new
        else:
            temp = self.root
            while temp is not None:
                if new.data < temp.data:
                    if temp.get_left() is None:
                        temp._set_left(new)
                        break
                    temp = temp.get_left()
                else:
                    if temp.get_right() is None:
                        temp._set_right(new)
                        break
                    temp = temp.get_right()
                    
        self.print_tree()
        return self.root
    
    def closest(self, key):
        closest_value = self.__closest(key, self.root)
        print("Closest value of {} : {}".format(key, closest_value))
    
    def __closest(self, key, root: Node = None):
        if root is not None:
            closest = root.data
            if root.data < key:
                closest = self.__closest(key, root.get_right())
            else:
                closest = self.__closest(key, root.get_left())
            
            if closest is not None and \
                abs(closest - key) < abs(root.data - key):
                return closest
            else:
                return root.data
    
    def __print_tree(self, node: Node, level=0):
        if node != None:
            self.__print_tree(node.get_right(), level + 1)
            print('     ' * level, node)
            self.__print_tree(node.get_left(), level + 1)
            
    def print_tree(self, node: Node = None):
        node = self.root if node is None else node
        self.__print_tree(node)
        print("--------------------------------------------------")
        
T = BST()
inp = input('Enter Input : ').split('/')
# inp = "2 5 1 -7 -5 6 9 12 0 -4/4".split('/')
data, key = [int(i) for i in inp[0].split()], int(inp[1])

for i in data:
    root = T.insert(i)
    
T.closest(key)