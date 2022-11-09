class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next if next is None else next
    
    def __str__(self):
        return str(self.data)
        
class List:
    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.__size = 0
            
        else:
            self.head = head
            t = self.head
            self.__size = 1
            while t.next != None:
                t = t.next
                self.__size += 1
            self.tail = t
            
    def size(self):
        return self.__size
    
    def is_empty(self):
        pass
    
    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = p
    
    def __str__(self):
        node = self.head
        data_list = []
        while node != None:
            data_list.append(node.data)
            node = node.next
        return ' '.join(data_list)
    
    def add_head():
        pass
    
    def remove(items):
        pass
    
    def remove_tail(self):
        p = self.head
        while p.next.next != None:
            p = p.next
        p.next = p.next.next
    
    def remove_head(self):
        self.head = self.head.next
    
    def search(item):
        pass
    
    def insert_after(data, target_node):
        p = Node(data)
        p.next = target_node.next
        target_node.next = p
        
    def delete_after(target_node):
        target_node.next = target_node.next.next

def deleteNode(root, key):
  
    # Base Case
    if root is None:
        return root
  
    # Recursive calls for ancestors of
    # node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root
  
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
        return root
  
    # We reach here when root is the node
    # to be deleted.
      
    # If root node is a leaf node
      
    if root.left is None and root.right is None:
          return None
  
    # If one of the children is empty
  
    if root.left is None:
        temp = root.right
        root = None
        return temp
  
    elif root.right is None:
        temp = root.left
        root = None
        return temp
  
    # If both children exist
  
    succParent = root
  
    # Find Successor
  
    succ = root.right
  
    while succ.left != None:
        succParent = succ
        succ = succ.left
  
    # Delete successor.Since successor
    # is always left child of its parent
    # we can safely make successor's right
    # right child as left of its parent.
    # If there is no succ, then assign
    # succ->right to succParent->right
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
  
    # Copy Successor Data to root
  
    root.key = succ.key
  
    return root

# https://www.geeksforgeeks.org/deletion-in-binary-search-tree/