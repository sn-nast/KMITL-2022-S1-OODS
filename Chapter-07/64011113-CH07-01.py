# Chapter : 7 - item : 1 - รู้จักกับ Binary Search Tree
# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root: Node = None

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
        else:
            temp = self.root
            while temp is not None:
                if new.data < temp.data:
                    if temp.left is None:
                        temp.left = new
                        break
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new
                        break
                    temp = temp.right
        return self.root
    
    def printTree(self, node: Node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)