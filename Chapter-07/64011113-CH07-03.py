"""
Chapter : 7 - item : 3 - สีแดงแรง 3 เท่า

ให้น้องๆรับ input เป็น list และ k โดยให้สร้าง Binary Search Tree จาก list ที่รับมา 
และหลังจากนั้นให้ทำการดูว่าใน Tree มีค่าไหนที่มากกว่าค่า k หรือไม่ ถ้ามีให้ทำการคูณ 3 เพิ่มเข้าไป

"""
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
            
    def find_greater_than(self, key: int, root: Node, mutiplier=3):
        if root is None: return
        elif root.data > key:
            self.find_greater_than(key, root.left)
            self.find_greater_than(key, root.right)
            root.data *= mutiplier
        else:
            self.find_greater_than(key, root.right)
            
T = BST()
inp = input('Enter Input : ').split('/')
# inp = "5 3 1 4 7 6 8/4".split('/')
data, key = [int(i) for i in inp[0].split()], int(inp[1])

for i in data:
    root = T.insert(i)
T.printTree(root)

T.find_greater_than(key, T.root)
print("--------------------------------------------------")
T.printTree(root)