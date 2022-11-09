# Hashing
class Data:
    def __init__(self, key, value):
        self.key: str = key
        self.value: str = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, size, max_col, list):
        self.table: list[Data] = [None]*size
        self.size: int = size
        self.max_col: int = max_col
        self.is_full: bool = False
        for x in list:
            self.insert_data(x)
    
    def insert_data(self, data: Data):
        if self.is_full: return False
        elif self.__is_full():
            print(f"This table is full !!!!!!")
            self.__is_full = True
            return False
        
        total_ascii = 0
        for x in list(data.key):
            total_ascii += ord(x)
        hash_idx = total_ascii % self.size
        
        if self.table[hash_idx] is None or self.probing(hash_idx):
            self.table[hash_idx] = data
        
        self.show_table()
    
    def __is_full(self):
        for x in self.table:
            if x is None:
                return False
        return True
        
    
    def probing(self, hash_idx: int):
        for n in range(self.max_col):
            idx = 0
            if n == 0:
                print(f"collision  number {n+1} at {hash_idx}")
                continue
            else:
                idx = (hash_idx + pow(n, 2)) % self.size
            if self.table[idx] is None:
                hash_idx = idx
                return True
            print(f"collision number {n+1} at {idx}")
        print(f"Max of collisionChain")
        return False   

    def show_table(self):
        for idx, data in enumerate(self.table):
            text = None
            if data is not None:
                text = f"({data.key}, {data.value})"
            print(f"#{idx+1}\t{text}")
        print("---------------------------")

print(" ***** Fun with hashing *****")
input = input("Enter Input : ").split("/")
size, max_col = list(map(int, input[0].split(" ")))

data = [Data(i[0], i[1]) for i in [x.split(" ") for x in list(map(str, input[1].split(",")))]]

hash = hash(size, max_col, data)