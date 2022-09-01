# Queue #1

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
        return str(self._items) if self.size() > 0 else "Empty"

def queue_cmd(list_cmd):
    queue = Queue()
    for i in list_cmd:
        if i[0] == 'E':
            queue.en_queue(i[1])
            print(f"Add {i[1]} index is {queue.size() - 1}")
        elif i[0] == 'D':
            if queue.size() < 1: print("-1")
            else: print(f"Pop {queue.de_queue()} size in queue is {queue.size()}")
    
    print((f"Number in Queue is :  {queue}") if queue.size() > 0 else queue) 

input_cmd = [str(i).split(" ") for i in input("Enter Input : ").split(",")]
queue_cmd(input_cmd)