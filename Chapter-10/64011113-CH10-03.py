# Hashing
class Data:
    def __init__(self, key: str, value: str):
        self.key: str = key
        self.value: str = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class Hash:
    def __init__(self, size: int, max_collision: int, datas: list):
        self.table: list[Data] = [None]*size
        self.table_size: int = size
        self.max_collision: int = max_collision
        self.__is_full: bool = False
        for data in datas:
            self.insert_data(data)

    def insert_data(self, data: Data):
        if self.__is_full:
            return False
        elif self.is_full():
            print(f"This table is full !!!!!!")
            self.__is_full = True
            return False

        ascii_value = 0
        for char in list(data.key):
            ascii_value += ord(char)
        hash_idx = ascii_value % self.table_size

        if self.table[hash_idx] is None:
            self.table[hash_idx] = data
        else:
            self.probing(hash_idx, data)

        self.show_table()

    def is_full(self):
        for data in self.table:
            if data is None:
                return False
        return True

    def probing(self, hash_idx: int, data: Data):
        for n in range(1, self.max_collision+1):
            idx = (hash_idx + pow(n-1, 2)) % self.table_size
            if self.table[idx] is None:
                self.table[idx] = data
                return True
            print(f"collision number {n} at {idx}")
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
# input = "5 5/one Un,two Deux,three Trois,four Quatre,five Cinq,ten Dix,eleven Onze".split("/")

size, max_col = list(map(int, input[0].split(" ")))

data = [Data(i[0], i[1]) for i in [
    x.split(" ")for x in list(map(str, input[1].split(",")))
]]

hash = Hash(size, max_col, data)
