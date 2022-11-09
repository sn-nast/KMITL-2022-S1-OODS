class AVL:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.left: 'AVL.Node' = None
            self.right: 'AVL.Node' = None
            self.height: int = 0
            
        def __str__(self):
            return str(self.data)
        
        def get_balance(self):
            h_left = self.left.height if self.left is not None else 0
            h_right = self.right.height if self.right is not None else 0
            return h_left - h_right
        
        def get_left(self) -> 'AVL.Node':
            return self.__left
        
        def _set_left(self, data):
            self.__left = data if isinstance(data, AVL.Node) else AVL.Node(data)
            
        def get_right(self):
            return self.__right
        
        def _set_right(self, data):
            self.__right = data if isinstance(data, AVL.Node) else AVL.Node(data)
            
        def is_node(other):
            return isinstance(other, AVL.Node)
        
    def __init__(self):
        self.root: AVL.Node = None
        
    
    def insert(self, data):
        new = data if isinstance(data, AVL.Node) else self.Node(data)
        if self.root is None:
            self.root = new
        else:
            self.__insert(self.root, new)
        return self.root
    
    def __insert(self, root: 'AVL.Node', new: 'AVL.Node'):
        if root is None:
            root = self.Node(new.data)
            return True
        elif root.data < new.data:
            root.height += 1
            if root.left is None:
                self.__insert(root.left, new)
            else:
                self.__insert(root.right, new)
        root.height = 1 + max(root.left.height, root.right.height)
        bal_fac = root.get_balance()
        
        if bal_fac > 1 and root.left.data > new.data:
            self.__right_rotate(root)
        elif bal_fac < -1 and new.data > root.right.data:
            self.__left_rotate(root)
        elif bal_fac > 1 and root.left.data < new.data:
            self.__right_left_rotate(root)
        elif bal_fac < -1 and new.data < root.right.data:
            self.__left_right_rotate(root)
            
    def rebalance(self, root: 'AVL.Node', new: 'AVL.Node'):
        pass
    
    def __right_rotate(self, node_x: 'AVL.Node'):
        node_y = node_x.left
        node_x.left = node_y.right
        node_y.right = node_x
        return node_y
    
    def __left_rotate(self, node_x: 'AVL.Node'):
        node_y = node_x.right
        node_x.right = node_x.left
        node_y.left = node_x
        return node_y
    
    def __right_left_rotate(self, node_x: 'AVL.Node'):
        node_y = node_x.left
        node_x = self.__left_rotate(node_y)
        node_x = self.__right_rotate(node_x)
        return node_x
    
    def __left_right_rotate(self, node_x: 'AVL.Node'):
        node_y = node_x.right
        node_x = self.__right_rotate(node_y)
        node_y = self.__left_rotate(node_x)
        return node_x
    
    def __print_tree(self, node: Node, level=0):
        if node != None:
            self.__print_tree(node.get_right(), level + 1)
            print('     ' * level, node)
            self.__print_tree(node.get_left(), level + 1)
            
    def print_tree(self, node: Node = None):
        node = self.root if node is None else node
        self.__print_tree(node)
        
t = AVL()
input = [int(i) for i in "10 20 30 40 50 25".split(" ")]
print(input, type(input))
for i in input:
    root = t.insert(i)
    print(root)
    
t.print_tree(root)