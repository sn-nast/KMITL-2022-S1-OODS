# Singly Linked List

class SLL:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
            
    def __init__(self, head: Node = None):
        self.head = head
        self.size = 0 if head is None else 1
    
    def __str__(self):
        if self.is_empty(): return 'Empty'
        temp_node = self.head
        list_string = str(temp_node.value) + ' '
        while temp_node.next != None:
            list_string += str(temp_node.next.value) + ' '
            temp_node = temp_node.next
        return list_string
    
    def append(self, *items):
        for item in items:
            new = self.Node(item)
            if self.is_empty():
                self.head = new
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = new
            self.size += 1
        
    # ทวน
    def is_empty(self):
        return self.head == None
    
    def add_head(self, item):
        new = self.Node(item)
        if self.is_empty():
            self.append(item)
        else:
            new.next = self.head
            self.head = new
    
    def search(self, item):
        checking_node = self.Node(item)
        temp_node = self.head
        if self.is_empty(): 
            return "Not Found"
        while temp_node.value != None:
            if temp_node.value == checking_node.value: return 'Found'
            elif temp_node.next is None: return 'Not Found'
            temp_node = temp_node.next
    
    def index(self, item):
        if self.is_empty(): return -1
        
        checking_node = self.Node(item)
        temp_node = self.head
        index = 0
        while temp_node.value != None:
            if temp_node.value == checking_node.value: return index
            elif temp_node.next is None: return -1
            temp_node = temp_node.next
            index += 1
            
    def pop(self, pos: int = 0):
        temp_node = self.head
        index = 0
        while temp_node != None:
            if pos == index:
                if self.size == 1:
                    self.head = None
                elif self.size == 2:
                    self.head = temp_node.next
                elif pos == 0:
                    self.head = self.head.next
                self.size -= 1
                return 'Success'
            elif index == pos-1:
                temp_node.next = temp_node.next.next
                self.size -= 1
                return 'Success'
            elif temp_node.next is None: return 'Out of Range'
            temp_node = temp_node.next
            index += 1

l = SLL()
print(l)

l.append("Hello", 'hi', "how", 'are')
print(l)

l.pop()
print("pop:", l)

l.pop(2)
print("pop 2:", l)

print(l.size)
print(l)

print(l.search('how'))
print(l)

print(l.index('how'))