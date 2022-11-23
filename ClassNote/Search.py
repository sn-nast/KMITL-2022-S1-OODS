import Time as Time


class Search:
    def __init__(self):
        pass

    def search_unorder_typical(self, list: list, key):
        if list is None:
            return
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
        if list is None:
            return
        # Add sentinel
        list.append(key)
        idx = 0
        while key != list[idx]:
            idx += 1
        list.pop()
        return self.__has_key(idx, list)

    def search_unorder_move_to_front(self, list: list, key):
        if list is None:
            return
        list.append(key)
        idx = 0
        while key != list[idx]:
            idx += 1
        list.pop()
        list.insert(0, list.pop(idx))
        return self.__has_key(idx, list)

    def search_unorder_transposition(self, list: list, key):
        if list is None:
            return
        list.append(key)
        idx = 0
        while key != list[idx]:
            idx += 1
        list.pop()
        result = self.__has_key(idx, list)
        if idx > 0 and result:
            # swap
            list[idx-1], list[idx] = list[idx], list[idx-1]
        return result

    def __has_key(self, idx: int, list: list):
        return True if idx <= len(list) - 1 else False

    class Hash:
        class Data():
            def __init__(self, key, value):
                self._key = key
                self.value = value

            def __str__(self):
                return "key: {:5} value: {:5}".format(self._key, self.value)

        def __init__(self, table_size: int, max_collision: int = None, datas: list = None):
            self.__table: list[Search.Hash.Data] = [None]*table_size
            self.__table_size: int = table_size
            self.__max_collision: int = max_collision
            self.__count_data: int = 0

            if datas is not None:
                for data in datas:
                    self.insert_data(data)

        @property
        def n_data(self):
            return sum(map(lambda x: x is not None, self.__table))

        @property
        def is_full(self):
            for data in self.__table:
                if data is None:
                    return False
            return True

        @property
        def table(self):
            return [{data._key, data.value} for data in self.__table if data is not None]

        def insert_data(self, data):
            data = data if isinstance(
                data, Search.Hash.Data) else self.Data(self.__count_data+1, data)
            if self.is_full:
                return False

            print(f"\t inserting {data.value}")
            insert_idx = self.__probing(self.__hash(str(data.value)))

            table = self.__table
            if insert_idx == -1:
                print(self.table)
                return False
            elif table[insert_idx] is None:
                self.__count_data += 1
                table[insert_idx] = data
                print(self.table)
            else:
                print(self.table)
                return False

        def __hash(self, value):
            return sum([ord(char) for char in value]) % self.__table_size

        def __probing(self, hash_idx: int, rehash: bool = False):
            # for n in range(0, self.__max_collision):
            #     idx = (hash_idx + pow(n, 2)) % self.__table_size
            #     if self.__table[idx] is not None:
            #         return idx
            #     print(f"collision number {n+1} at {idx}")
            idx = self.__check_collision(hash_idx)
            print(f"insert idx: {idx}")
            if idx == -1:
                rehash_str = " - Rehash !!! " if rehash else ""
                print(f"****** Max collision {rehash_str}******")
                if rehash:
                    self.__reshash()
            return idx

        def __check_collision(self, hash_idx: int):
            for n in range(0, self.__max_collision):
                # idx = (hash_idx + pow(n, 2)) % self.__table_size
                idx = self.__quadratic_idx(hash_idx, n)
                if self.__table[idx] is None:
                    return idx
                print(f"collision number {n+1} at {idx}")
            return -1

        def __quadratic_idx(self, idx: int, scale: int) -> int:
            return (idx + pow(scale, 2)) % self.__table_size

        def __reshash(self):
            pass

        def __str__(self):
            return f"""
        table_size: {self.__table_size}
        max_col: {self.__max_collision}
        count_data: {self.__count_data}
        """


t = Time.Time()
lst = ["He", "She", "it's", "Bangkok", "Thailand", 5]
s = Search.Hash(5, 2, lst)
print(s.table)
print(s)
