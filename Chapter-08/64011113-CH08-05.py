# Van
class MinHeap:
    def __init__(self):
        self.__FRONT_IDX: int = 1
        self.__heap: list = [None]
        
    def get_parent_index(self, idx: int):
        return idx//2
    
    def get_left_child_index(self, idx: int):
        return idx*2
    
    def get_right_child_index(self, idx: int):
        return idx*2 + 1
    
    def __swap(self, ref_idx: int, des_idx: int):
        heap = self.__heap
        heap[ref_idx], heap[des_idx] = heap[des_idx], heap[ref_idx]
    
    def __is_leaf(self, pos: int):
        return pos*2 > (len(self.__heap) -1)
    
    def __heapify(self, pos: int = None):
        pos = self.__FRONT_IDX if pos is None else pos
        heap = self.__heap
        idx = pos
        
        while not self.__is_leaf(idx):
            left_idx = self.get_left_child_index(idx)
            right_idx = self.get_right_child_index(idx)
            
            if right_idx > self.get_size():
                if heap[idx] > heap[left_idx]:
                    self.__swap(idx, left_idx)
                break
            
            if (heap[idx] > heap[left_idx] or
                heap[idx] > heap[right_idx]):
                
                if heap[left_idx] < heap[right_idx]:
                    self.__swap(idx, left_idx)
                    idx = self.get_left_child_index(idx)
                else:
                    self.__swap(idx, right_idx)
                    idx = self.get_right_child_index(idx)
            else:
                break
            
    def get_size(self):
        return len(self.__heap)-1
    
    def insert(self, new):
        list_ele = new if isinstance(new, list) else [new]
        heap = self.__heap
        
        for x in list_ele:
            heap.append(x)
            
            idx = len(heap)-1
            parent_idx = self.get_parent_index(idx)
            if parent_idx < self.__FRONT_IDX:
                continue
            
            while heap[idx] < heap[parent_idx]:
                self.__swap(idx, parent_idx)
                idx = parent_idx
                parent_idx = self.get_parent_index(idx)
    
    def pop_front(self):
        heap = self.__heap
        min = heap.pop(self.__FRONT_IDX)
        heap.insert(self.__FRONT_IDX, heap.pop())
        self.__heapify()
        return min
    
    def is_empty(self):
        return self.get_size() == 0
    
    def get_heap(self):
        return self.__heap[1:]
    
class VanCompany:
            
    class Van:
        def __init__(self, number = 0):
            self.day: int = 0
            self.number: int = number
        
        def __lt__(self, other: 'VanCompany.Van'):   
            return self.number < other.number
        
        def __gt__(self, other: 'VanCompany.Van'):
            return self.number > other.number
        
        def __eq__(self, other: 'VanCompany.Van'):
            return self.number == other.number
        
    def __init__(self, amount: int):
        amount = amount if amount > 0 else 0
        self.vans = MinHeap()
        for n in range(1, amount+1):
            self.vans.insert(self.Van(n))

    def booking(self, days: list):
        queue: list = []
        vans = self.vans
        van_total = vans.get_size()
        
        queue_n = 1
        while len(days) != 0:
            
            if len(queue) < van_total:
                new_queue = vans.pop_front()
                new_queue.day = days.pop(0)
                queue.append(new_queue)
                print(f"Customer {queue_n} Booking Van {new_queue.number} | {new_queue.day} day(s)")
                queue_n += 1
            else:
                day_queue = [x.day for x in queue]
                day_pass = min(day_queue)
                is_pass = False 
                idx = 0
                while not is_pass:
                    if idx > len(queue)-1:
                        is_pass = True
                    else:
                        queue[idx].day -= day_pass
                        if queue[idx].day == 0:
                            temp = queue.pop(idx)
                            vans.insert(temp)
                            idx -= 1
                        idx += 1
                        

# input = input("Enter Input : ").split("/")
input = "16/10 1 1 1".split("/")
k = int(input[0])
days = [int(i) for i in input[1].split(" ")]
company = VanCompany(k)
company.booking(days)
