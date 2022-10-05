# Doubly Linked List

class DLL:
    class Node:
        def __init__(self, value, previous: 'DLL.Node' = None, next: 'DLL.Node' = None):
            self.value = value
            self.previous = previous
            self.next = next
    
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail
        self._size = 0 + (1 if head != None else 0) + (1 if tail != None else 0)  
        
    def __str__(self):
        if self.is_empty(): return 'Empty'
        cur, string = self.head, str(self.head.value) + ' '
        while cur.next != None:
            string += str(cur.next.value) + ' '
            cur = cur.next
        return string
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        return self._size
    
    def append(self, item=None, node: Node = None):
        new = self.Node(item) if node is None else node
        if self.is_empty():
            self.head = new
            self.tail = new
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new
            new.previous = temp
            self.tail = new
        self._size += 1
            
    def add_head(self, item, node: Node = None):
        new = self.Node(item) if node is None else node
        new.next = self.head
        if self.is_empty():
            self.append(node=new)
        else:
            self.head.previous = new
            self.head = new
            self._size += 1
    
    def search(self, item):
        return 'Found' if self.index(item) > -1 else 'Not Found'
            
    def index(self, item, node: Node = None):
        if self.is_empty(): return -1
        checking_node = self.Node(item) if node is None else node
        temp = self.head
        index = 0
        while temp.next != None:
            if temp.value == checking_node.value: return index
            elif temp.value is None: return -1
            temp = temp.next
            index += 1
            
    def pop(self, pos: int = 0):
        if self.is_empty(): return 'Out of Range'
        temp = self.head
        index = 0
        while temp.value != None:
            if index == pos:
                if temp.previous is not None:
                    temp.previous.next = temp.next
                if temp.next is not None:
                    temp.next.previous = temp.previous
                    
                if self.size() == 1:
                    self.head = None
                    self.tail = None
                elif self.size() == 2:
                    self.head = self.tail = temp
                if pos == 0:
                    self.head = temp.next
                self._size -= 1
                return 'Success'
            elif temp == self.tail: return 'Out of Range'
            temp = temp.next
            index += 1
            
    def insert(self, pos, item=None, node: Node = None):
        new = self.Node(item) if node is None else node
        if self.is_empty():
            self.append(node=new)
        else:
            temp = self.head if pos > 0 else self.tail
            index = 0 if pos > 0 else -1
            while temp.value != None:
                if index == pos:
                    new.previous = temp.previous
                    new.next = temp
                    if temp.previous is not None:
                        temp.previous.next = new
                    temp.previous = new
                    self._size += 1
                    return 'Success'
                elif pos > self.size():
                    self.append(node=new)
                    return 'Success'
                elif pos < -1*self.size():
                    self.add_head(node=new)
                    return 'Success'
                temp = temp.next if pos > 0 else temp.previous
                index += 1 if pos > 0 else -1
                
    def reverse(self):
        if self.is_empty(): return 'Empty'
        cur, string = self.tail, str(self.tail.value) + ' '
        while cur.previous != None:
            string += str(cur.previous.value) + ' '
            cur = cur.previous
        return string
    
l = DLL()
print(l)

l.append("Hello")
l.append('hi')
l.append('how')
l.append('are')
l.append('you')
print('append:\t', f'size: {l.size()}', f'list : {l}')

print('search "how": ', l.search('how'), 'index: ', l.index('how'))

print('pop(0): ', l.pop() , f'size: {l.size()}', f'list : {l}')
print('pop(2): ', l.pop(2), f'size: {l.size()}', f'list : {l}')

print('insert: 20', l.insert(20, "test02"), ': ',f'size: {l.size()}', f'list : {l}')
print('insert: -2', l.insert(-2, "test03"), ': ',f'size: {l.size()}', f'list : {l}')

print(l.reverse())