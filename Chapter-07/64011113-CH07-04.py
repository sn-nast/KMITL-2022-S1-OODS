"""Chapter : 7 - item : 4 - delete node in tree

ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

โดยมีการป้อน input ดังนี้

i <int> = insert data

d <int> = delete data

หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว

"""

class Node:
    def __init__(self, data: int): 
        self.data = data  
        self.left: Node = None  
        self.right: Node = None 
        self.level = None 
        
    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root: Node = None

    def insert(self, val):  
        new = Node(val)
        if self.root is None:
            self.root = new
        else:
            temp = self.root
            level_left = 0
            level_right = 0
            while temp is not None:
                if new.data < temp.data:
                    if temp.left is None:
                        temp.left = new
                        temp.level = level_left
                        break
                    level_left += 1
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new
                        temp.level = level_right
                        break
                    level_right += 1
                    temp = temp.right
        print(f'insert {val}')
        return self.root
    
    def delete(self, root: Node, data: int):
        current = root
        prev = None
        print(f"delete {data}")
        
        # find node
        while current is not None and current.data != data:
            prev = current
            if current.data < data:
                current = current.right
            else:
                current = current.left
                
        if current is None:
            print("Error! Not Found DATA")
            return root
        
        # atmost one child
        if current.left is None or current.right is None:
            new = None
            # node has one branch
            if current.left == None:
                new = current.right
            else:
                new = current.left
                
            # delete node completed
            # Does prev node have child
            if prev is None:
                # 1st node
                self.root = current.left
                return new
            elif current == prev.left:
                prev.left = new
            else:
                prev.right = new
            current = None
            
        else:
            temp_prev = None
            temp = None
            # find min value that more than deleting node
            temp = current.right
            while temp.left is not None:
                temp_prev = temp
                temp = temp.left
                
            if temp_prev is not None:
                temp_prev.left = temp.right
            else:
                current.right = temp.right
            
            current.data = temp.data
            temp = None
            
        return root

def printTree90(node: Node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
# data = "d 1,i 1,d 1,i 0,i 2,i 4,i 1,i 5,i 3,d 2".split(",")

for i in data:
    cmd, value = i.split(" ")
    if cmd == 'i':
        tree.insert(int(value))
        printTree90(tree.root)
    elif cmd == 'd':
        tree.delete(tree.root, data=int(value))
        # TODO
        printTree90(tree.root)