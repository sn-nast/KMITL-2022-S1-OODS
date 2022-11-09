import Time as Time

class Search:
    def __init__(self):
        pass
    
    def search_unorder_typical(self, list: list, key):
        if list is None: return
        pos = len(list) + 1
        idx = 0
        while idx != pos:
            # Finded
            if key == list[idx]:
                pos = idx
                break
            else:
                idx += 1
                
        return self.__has_key(idx, list)
    
    def search_unorder_sentinel(self, list: list, key):
        if list is None: return
        list.append(key)
        idx = 0
        while key != list[idx]:
            idx += 1
        list.pop()
        return self.__has_key(idx, list)
    
    def search_unorder_heuristic(self, list: list, key):
        if list is None: return
        list.append(key)
        idx = 0
        while key != list[idx]:
            idx += 1
        list.pop()
        list.insert(0, list.pop(idx))
        return self.__has_key(idx, list)
    
    def search_unorder_transposition(self, list: list, key):
        if list is None: return
        list.append(key)
        idx = 0
        while key != list[idx]:
            idx += 1
        list.pop()
        result = self.__has_key(idx, list)
        if idx > 0 and result:
            list[idx-1], list[idx] = list[idx], list[idx-1]
        return result
            
    def __has_key(self, idx: int, list: list):
        return True if idx <= len(list) - 1 else False
    
    
s = Search()
t = Time.Time()
lst = [1, -5, 6, 8 , 4, -6, 5, 2]
result = s.search_unorder_typical(lst, 5)
print(f"search found: {result}")
t.get_time()

t.reset()
result = s.search_unorder_sentinel(lst, 5)
print(f"search found: {result}")
t.get_time()

t.reset()
result = s.search_unorder_transposition(lst, 5)
print(f"search found: {result}")
t.get_time()
print(lst)

t.reset()
result = s.search_unorder_transposition(lst, 5)
print(f"search found: {result}")
t.get_time()
print(lst)

t.reset()
result = s.search_unorder_transposition(lst, 5)
print(f"search found: {result}")
t.get_time()
print(lst)

t.reset()
result = s.search_unorder_transposition(lst, 5)
print(f"search found: {result}")
t.get_time()
print(lst)

t.reset()
result = s.search_unorder_transposition(lst, 5)
print(f"search found: {result}")
t.get_time()
print(lst)

t.reset()
result = s.search_unorder_transposition(lst, 5)
print(f"search found: {result}")
t.get_time()
print(lst)

t.reset()
result = s.search_unorder_transposition(lst, 5)
print(f"search found: {result}")
t.get_time()
print(lst)
