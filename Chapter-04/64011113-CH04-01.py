# Queue
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
    

# q = Queue()
# print(q._items)
input_cmd = [str(i).split(" ") for i in input("Enter Input : ").split(",")]
# input_cmd = [input("Enter Input : ").split(",")]
# input_cmd 
print(type(input_cmd))
print(input_cmd)