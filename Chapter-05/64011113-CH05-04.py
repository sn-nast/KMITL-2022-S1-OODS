# VIM Text Editor

class Node:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.next = next
        self.previous = previous
        
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
        return self.head == None and self.tail == None 
    
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
        if self.is_em:
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
                
    def insert_node(self, cursor: Node, new_element: Node):
        before = cursor.previous
        new_element.previous = before
        if before != None:
            before.next = new_element
        cursor.previous = new_element
        new_element.next = cursor
        
    def _identify_head_or_tail(self, node: Node):
        if node == None: return
        if node.previous == None:
            self.head = node
        elif node.next == None:
            self.tail = node
        
class VimEditor:
            
    def __init__(self):
        self.list = LinkedList()
        self.cursor = Node('|')
    
    def add_input(self, input):
        for cmd in input:
            list = self.list
            if cmd[0] == 'I':
                if list.is_empty():
                    list.append(cmd[2:])
                    cursor = self.cursor
                    cursor.previous = list.head
                    list.tail = cursor
                    list.head.next = cursor
                else:
                    list.insert_node(self.cursor, Node(cmd[2:]))
            elif cmd[0] == 'L':
                self.move_cursor("L")
            elif cmd[0] == 'R':
                self.move_cursor("R")
            elif cmd[0] == 'B':
                self.delete('B')
            elif cmd[0] == 'D':
                self.delete('D')
        print(self.list)
            
    def move_cursor(self, side):
        cursor = self.cursor
        list = self.list
        before = cursor.previous
        after = cursor.next
        if list.is_empty():
            return
        if side == 'L' and cursor != list.head:
            cursor.previous = before.previous
            if before.previous != None:
                before.previous.next = cursor
            before.previous = cursor
            before.next = after
            cursor.next = before
            if after != None:
                after.previous = before
            list._identify_head_or_tail(before)

        elif side == 'R' and cursor != list.tail:
            cursor.previous = after
            if after.next != None:
                after.next.previous = cursor
            after.previous = before
            cursor.next = after.next
            after.next = cursor
            if before != None:
                before.next = after
            list._identify_head_or_tail(after)
        list._identify_head_or_tail(cursor)

    def delete(self, cmd):
        cursor = self.cursor
        list = self.list
        before = cursor.previous
        after = cursor.next
        if cmd == 'B' and list.head != cursor:
            cursor.previous = before.previous
            if before.previous != None:
                before.previous.next = cursor
                list._identify_head_or_tail(cursor.previous)
        elif cmd == 'D' and list.tail != cursor:
            cursor.next = after.next
            if after.next != None:
                after.next.previous = cursor
                list._identify_head_or_tail(cursor.next)
        list._identify_head_or_tail(cursor)
        if cursor.previous == None and cursor.next == None:
            self.list = LinkedList()

input = "I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate".split(',')
vim = VimEditor()
vim.add_input(input)