class MinHeap:
    def __init__(self):
        self.__FRONT_IDX: int = 1
        self.heap: list = [None]
        
    def get_parent_index(self, idx: int):
        return idx//2
    
    def get_left_child_index(self, idx: int):
        return idx*2
    
    def get_right_child_index(self, idx: int):
        return idx*2 + 1
    
    def swap(self, ref_idx: int, des_idx: int):
        heap = self.heap
        heap[ref_idx], heap[des_idx] = heap[des_idx], heap[ref_idx]
    
    def is_leaf(self, pos: int):
        return pos*2 > len(self.heap)
    
    def heapify(self, pos: int = None):
        pos = self.__FRONT_IDX if pos is None else pos
        heap = self.heap
        idx = pos
        
        while not self.is_leaf(idx):
            left_idx = self.get_left_child_index(idx)
            right_idx = self.get_right_child_index(idx)
            
            if (heap[idx] > heap[left_idx] or
                heap[idx] > heap[right_idx]):
                
                if heap[left_idx] < heap[right_idx]:
                    self.swap(idx, left_idx)
                    idx = self.get_left_child_index(idx)
                else:
                    self.swap(idx, right_idx)
                    idx = self.get_right_child_index(idx)
            else:
                break
    
    def insert(self, new):
        list_ele = new if isinstance(new, list) else [new]
        heap = self.heap
        
        for x in list_ele:
            heap.append(x)
            
            idx = len(heap)-1
            parent_idx = self.get_parent_index(idx)
            if parent_idx < self.__FRONT_IDX:
                continue
            
            while heap[idx] < heap[parent_idx]:
                self.swap(idx, parent_idx)
                idx = parent_idx
                parent_idx = self.get_parent_index(idx)
    
    def pop_front(self):
        heap = self.heap
        min = heap.pop(self.__FRONT_IDX)
        heap.insert(self.__FRONT_IDX, heap.pop())
        self.heapify()
        return min
    
heap = MinHeap()
heap.insert([13, 14, 16, 24, 50, 21, 19, 68, 65, 26, 32, 96])

print(heap.heap)
print(heap.pop_front())

print(heap.heap)
print(heap.pop_front())

print(heap.heap)
print(heap.pop_front())

print(heap.heap)
print(heap.pop_front())

print(heap.heap)
print(heap.pop_front())