# Chapter : 7 - item : 2 - หาค่า Below

# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ 
# และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree

# ***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()

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
        new = self.Node(data)
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
            
    def _below(self, key: int, root: Node, list=[]):
        if root is None:
            return
        elif key > root.data:
            self._below(key, root.left)
            list.append(root.data)
            self._below(key, root.right)
        else:
            self._below(key, root.left)
        return list

    def print_below(self, key):
        if self.root is not None:
            list = self._below(key, self.root)
            print("--------------------------------------------------")
            string = " ".join([str(i) for i in list]) if  len(list) != 0 else "Not have"
            print(f'Below {key} : {string}')
    
T = BST()
inp = input('Enter Input : ').split('|')
# inp = "100 70 200 34 80 300|71".split('|')
data, key = [int(i) for i in inp[0].split()], int(inp[1])

for i in data:
    root = T.insert(i)
T.printTree(root)
T.print_below(key)