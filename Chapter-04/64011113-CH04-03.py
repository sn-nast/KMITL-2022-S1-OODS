# Bookstore

class Queue:
    
    def __init__(self, list=None):
        self._items = [] if list == None else list
    
    def en_queue(self, value):
        self._items.append(value)
        
    def de_queue(self):
        return self._items.pop(0)
    
    def is_empty(self):
        return self._items == []
    
    def size(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items) if self.size() > 0 else "[]"

def bookshelf(remaining, cmd):
    remaining_book = Queue(remaining.split(" "))
    shelf_cmd = [i.split(" ") for i in cmd.split(",")]
    for i in shelf_cmd:
        if i[0] == 'E':
            remaining_book.en_queue(i[1])
        elif i[0] == 'D':
            remaining_book.de_queue()
    print("NO " if len(set(remaining_book._items)) == remaining_book.size() else "", "Duplicate", sep="")
    
input_cmd = input("Enter Input : ").split("/")
bookshelf(input_cmd[0], input_cmd[1])