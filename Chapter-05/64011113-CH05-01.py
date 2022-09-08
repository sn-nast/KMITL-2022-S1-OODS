# Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def is_empty(self):
        return self.head == None
    
    def append(self, item):
        p = Node(item)
        if self.is_empty():
            self.head = p
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = p
    
    def add_head(self, item):
        p = Node(item)
        if self.is_empty():
            self.append(item)
        else:
            p.next = self.head
            self.head = p
    
    def search(self, item):
        p = Node(item)
        temp = self.head
        if self.is_empty():
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
                return 'Success'
            elif index == pos-1:
                temp.next = temp.next.next
                return 'Success'
            elif temp.next is None: return 'Out of Range'
            temp = temp.next
            index += 1
    
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
print("Linked List :", L)