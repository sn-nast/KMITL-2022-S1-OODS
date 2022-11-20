# Rehashing
class Data:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Data = None

    def __str__(self):
        return self.value


class Hash:
    def __init__(
        self, size: int, max_collision: int,
        threshold: int, datas: list
    ):
        self.table: list[Data] = [None]*size
        self.table_size: int = size
        self.max_collision: int = max_collision
        self.__is_full: bool = False
        self.threshold: int = threshold
        self.inserted_root: Data = None

        print(f"Initial Table :")
        self.show_table()

        for data in datas:
            print(f"Add : {data.value}")
            self.insert_data(data)

    def insert_data(self, data: Data, is_rehashing: bool = False):
        if self.__is_full:
            return False
        elif self.is_full():
            print(f"This table is full !!!!!!")
            self.__is_full = True
            return False

        if self.is_over_threshold(has_new=True):
            print(f"****** Data over threshold - Rehash !!! ******")
            self.rehashing()

        idx = self.__probing(data.value, data)
        self.table[idx] = data

        if not is_rehashing:
            if self.inserted_root is None:
                self.inserted_root = data
            else:
                temp = self.inserted_root
                while temp.next is not None:
                    temp = temp.next
                temp.next = data
            self.show_table()

    def is_full(self):
        for data in self.table:
            if data is None:
                return False
        return True

    def is_over_threshold(self, has_new: bool = False):
        count_data = 0 if not has_new else 1
        for data in self.table:
            if data is not None:
                count_data += 1
        if count_data > (self.table_size*self.threshold) / 100:
            return True
        else:
            return False

    def __probing(self, hash_idx: int, data: Data):
        idx = 0
        for n in range(0, self.max_collision):
            idx = (hash_idx + pow(n, 2)) % self.table_size
            if self.table[idx] is None:
                return idx
            print(f"collision number {n+1} at {idx}")
        print(f"****** Max collision - Rehash !!! ******")
        self.rehashing()
        idx = self.__probing(hash_idx, data)
        return idx

    def rehashing(self):
        datas = self.__list_of_data()
        self.__resize_table()
        for data in datas:
            self.insert_data(data, is_rehashing=True)

    def __list_of_data(self):
        temp = self.inserted_root
        order_inserted = []
        while temp is not None:
            order_inserted.append(temp)
            temp = temp.next
        return order_inserted

    def __resize_table(self):
        new_table_size = self.next_prime(self.table_size*2)
        self.table = [None]*new_table_size
        self.table_size = new_table_size

    def show_table(self):
        for idx, data in enumerate(self.table):
            text = None
            if data is not None:
                text = f"{data.value}"
            print(f"#{idx+1}\t{text}")
        print("----------------------------------------")

    def is_prime(self, number: int):
        for n in range(1, number+1):
            if n == 1:
                continue
            elif n == number:
                return True
            elif number % n == 0:
                return False

    def next_prime(self, number: int):
        found = False
        while not found:
            if not self.is_prime(number):
                number += 1
            else:
                found = True
        return number


print(" ***** Rehashing *****")
input = input("Enter Input : ").split("/")
# input = "19 2 49/8741 4874 787842 77 8789 7542 751213 978458".split("/")

size, max_col, threshold = list(map(int, input[0].split(" ")))

data = [Data(int(x)) for x in input[1].split(" ")]

hash = Hash(size, max_col, threshold, data)
