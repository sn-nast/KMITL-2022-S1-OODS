# Double Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def reverse(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s
    
    def is_empty(self):
        return self.head == None
    
    def append(self, item):
        p = Node(item)
        if self.is_empty():
            self.head = p
            self.tail = p
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = p
            self.tail = p
            self.tail.previous = temp
    
    def add_head(self, item):
        p = Node(item)
        p.next = self.head
        if self.is_empty():
            self.append(item)
        else:
            self.head.previous = p
            self.head = p
    
    def search(self, item):
        p = Node(item)
        temp = self.head
        if temp == None:
            return 'Not Found'
        while temp.value != None:
            if temp.value == p.value: return 'Found'
            elif temp.next is None: return 'Not Found'
            temp = temp.next
        
    def index(self, item):
        p = Node(item)
        temp = self.head
        index = 0
        if self.is_empty():
            return -1
        while temp.value != None:
            if temp.value == p.value: return index
            elif temp.next is None: return -1
            temp = temp.next
            index += 1
    
    def size(self):
        size = 0
        temp = self.head
        if self.is_empty():
            return size
        while temp.value != None:
            size += 1
            if temp.next is None: return size
            temp = temp.next
    
    def pop(self, pos):
        temp = self.head
        index = 0
        if self.is_empty():
            return 'Out of Range'
        while temp.value != None:
            if index == pos:
                if self.size() == 1:
                    self.head = None
                elif self.size() == 2:
                    self.head = temp.next
                    self.head.previous = None
                else:
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                return 'Success'
            elif temp == self.tail: return 'Out of Range'
            temp = temp.next
            index += 1
            
    def insert(self, pos, item):
        p = Node(item)
        if self.is_empty():
            self.append(item)
        else:
            temp = self.head if pos > 0 else self.tail
            index = 0 if pos > 0 else -1
            while temp.value != None:
                if index == pos:
                    p.next = temp
                    p.previous = temp.previous
                    temp.previous.next = temp.previous = p
                    return
                elif pos > self.size():
                    self.append(item)
                    return
                elif pos < -1*self.size():
                    self.add_head(item)
                    return
                temp = temp.next if pos > 0 else temp.previous
                index += 1 if pos > 0 else -1
    
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.add_head(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())