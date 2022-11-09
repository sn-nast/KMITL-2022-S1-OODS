# Bean

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
        # Tracking
        track = []
        
        if self.root is None:
            self.root = new
            track.append("*")
        else:
            temp = self.root
            while temp is not None:
                if new.data < temp.data:
                    track.append("L")
                    if temp.get_left() is None:
                        temp._set_left(new)
                        track.append("*")
                        break
                    temp = temp.get_left()
                else:
                    track.append("R")
                    if temp.get_right() is None:
                        temp._set_right(new)
                        track.append("*")
                        break
                    temp = temp.get_right()
                    
        if track is not []: print(''.join(track))
        return self.root
    
    def __print_tree(self, node: Node, level=0):
        if node != None:
            self.__print_tree(node.get_right(), level + 1)
            print('     ' * level, node)
            self.__print_tree(node.get_left(), level + 1)
            
    def print_tree(self, node: Node = None):
        node = self.root if node is None else node
        self.__print_tree(node)
            
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
# inp = [int(i) for i in "48 47 194194 3534 39 20 2014 35289 53".split()]

for i in inp:
    root = T.insert(i)