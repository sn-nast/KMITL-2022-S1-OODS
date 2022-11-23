import time


class Sort:
    def __init__(self, list: list):
        self.list = list
        self.__shell_increments = [5, 3, 1]

    def bubble_sort(self, list: list = None):
        if list is None:
            list = []
        list = list if list != [] else self.list
        swaped = False
        for last in range(len(list)-1, 0, -1):
            for i in range(last):
                if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
                    swaped = True
            if not swaped:
                break
        return list

    def insertion_sort(self, list: list = None):
        if list is None:
            list = []
        list = list if list != [] else self.list
        for i in range(1, len(list)):
            i_element = list[i]
            for j in range(i, -1, -1):
                if i_element < list[j-1] and j > 0:
                    list[j] = list[j-1]
                else:
                    list[j] = i_element
                    break
        return list

    def selection_sort(self, list: list = None):
        if list is None:
            list = []
        list = list if list != [] else self.list
        # from len-1 to 0
        for last in range(len(list)-1, 0, -1):
            # declare var
            biggest = list[0]
            biggest_idx = 0
            # round from 1 to last for find Max
            for i in range(1, last+1):
                if list[i] > biggest:
                    biggest = list[i]
                    biggest_idx = i
            # swap value
            # biggest each round must stay in last_idx
            list[last], list[biggest_idx] = list[biggest_idx], list[last]
        return list

    def shell_sort(self, list: list = None, d_increments: list = None):
        if list is None:
            list = []
        if d_increments is None:
            d_increments = []
        list = list if list != [] else self.list
        d_increments = d_increments if d_increments != [] else self.__shell_increments
        for inc in d_increments:
            for i in range(inc, len(list)):
                i_element = list[i]
                for j in range(i, -1, -inc):
                    if i_element < list[j-inc] and j >= inc:
                        list[j] = list[j-inc]
                    else:
                        list[j] = i_element
                        break
        return list

    def merge_sort(self, list: list = None):
        if list is None:
            list = []
        list = list if list != [] else self.list
        self.__merge_sort(list, 0, len(list)-1)
        return list

    def __merge_sort(self, list: list, left, right):
        center = (left + right) // 2
        if left < right:
            self.__merge_sort(list, left, center)
            self.__merge_sort(list, center+1, right)
            self.__merge(list, left, center+1, right)

    def __merge(self, list: list, idx_left, idx_right, idx_end_right):
        start = idx_left
        idx_end_left = idx_right-1
        result = []
        # เช็คสองชุด ใช้ list เดียวกัน หั่นด้วยเลข idx
        while idx_left <= idx_end_left and idx_right <= idx_end_right:
            if list[idx_left] < list[idx_right]:
                result.append(list[idx_left])
                idx_left += 1
            else:
                result.append(list[idx_right])
                idx_right += 1
        # เหลือซ้ายไหม
        while idx_left <= idx_end_left:
            result.append(list[idx_left])
            idx_left += 1
        # เหลือขวาไหม
        while idx_right <= idx_end_right:
            result.append(list[idx_right])
            idx_right += 1

        # เก็บค่าใหม่
        for x in result:
            list[start] = x
            start += 1
            if start > idx_end_right:
                break

    def partition(self, low, high):
        list = self.list
        # choose the rightmost element as pivot
        pivot = list[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if list[j] <= pivot:

                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (list[i], list[j]) = (list[j], list[i])

        # Swap the pivot element with the greater element specified by i
        (list[i + 1], list[high]) = (list[high], list[i + 1])

        # Return the position from where partition is done
        return i + 1

    # function to perform quicksort

    def quickSort(self, low=None, high=None):
        low = 0 if low is None else low
        high = len(self.list)-1 if high is None else high

        if low < high:

            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition(low, high)

            # Recursive call on the left of pivot
            self.quickSort(low, pi - 1)

            # Recursive call on the right of pivot
            self.quickSort(pi + 1, high)
        return self.list


class SortB:
    def bubble_sort(self, list: list, idx: int = 0, count_ordered: int = 0):
        if count_ordered == len(list):
            return list
        elif idx < len(list)-1:
            if list[idx] > list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
            self.bubble_sort(list, idx+1, count_ordered)
            return list
        self.bubble_sort(list, 0, count_ordered+1)


sort = Sort([5, 2, 5, 1, 8, 2, 4, 6, 1, 15, 2, -6, -8, -2, 0, 11, 12, 17, -9])
print(sort.selection_sort())
