class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next if next is None else next
    
    def __str__(self):
        return str(self.data)
        
class List:
    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.__size = 0
            
        else:
            self.head = head
            t = self.head
            self.__size = 1
            while t.next != None:
                t = t.next
                self.__size += 1
            self.tail = t
            
    def size(self):
        return self.__size
    
    def is_empty(self):
        pass
    
    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = p
    
    def __str__(self):
        node = self.head
        data_list = []
        while node != None:
            data_list.append(node.data)
            node = node.next
        return ' '.join(data_list)
    
    def add_head():
        pass
    
    def remove(items):
        pass
    
    def remove_tail(self):
        p = self.head
        while p.next.next != None:
            p = p.next
        p.next = p.next.next
    
    def remove_head(self):
        self.head = self.head.next
    
    def search(item):
        pass
    
    def insert_after(data, target_node):
        p = Node(data)
        p.next = target_node.next
        target_node.next = p
        
    def delete_after(target_node):
        target_node.next = target_node.next.next

ls = List()
ls.append("A")
ls.append("B")
ls.append("C")
ls.append("D")
ls.append("E")
print(ls)