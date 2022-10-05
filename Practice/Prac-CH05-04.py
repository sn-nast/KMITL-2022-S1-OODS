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
        return self.head == None and self.tail == None
    
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
            
    def insert(self, pos=0, item=None, node: Node = None):
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
    
    def insert_node(self, ref_node: Node, new_node: Node):
        if ref_node.previous is not None:
            ref_node.previous.next = new_node
        new_node.previous = ref_node.previous
        new_node.next = ref_node
        ref_node.previous = new_node
            
        
class VimEditor:
    def __init__(self):
        self.list = DLL()
        self.cursor = DLL.Node('|')
    
    def add_list(self, input: list):
        for cmd in input:
            list = self.list
            if cmd[0] == 'I':
                data = cmd[2:]
                new = DLL.Node(data)
                if list.is_empty():
                    list.append(node=new)
                    list.append(node=self.cursor)
                else:
                    list.insert_node(self.cursor, new)
            elif cmd[0] == 'L':
                self.move_cursor("L")
            elif cmd[0] == 'R':
                self.move_cursor("R")
        print(self.list)
    
    def move_cursor(self, side):
        list = self.list
        if list.is_empty(): return
        cursor = self.cursor
        before = self.cursor.previous
        after = self.cursor.next
        if side == 'L' and cursor != list.head:
            cursor.previous = before.previous
            if before.previous is not None:
                before.previous.next = cursor
            cursor.next = before
            before.previous = cursor
            before.next = after
            if after is not None:
                after.previous = before
            self._identify_end(list, before)
            
        elif side == 'R' and cursor != list.tail:
            cursor.previous = after
            cursor.next = after.next
            if after.next is not None:
                after.next.previous = cursor
            after.next = cursor
            if before is not None:
                before.next = after
            after.previous = before
            after.next = cursor
            self._identify_end(list, after)
        
        self._identify_end(list, cursor)
    
    def _identify_end(self, list: DLL, node: DLL.Node):
        if node is None: return
        if node.previous == None: list.head = node
        if node.next == None: list.tail = node

# input = input("Enter Input : ").split(',')
input = "I Apple,I Bird,I Cat,L,L,R".split(',')
vim = VimEditor()
vim.add_list(input)