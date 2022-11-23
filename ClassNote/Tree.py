from math import floor, log2


class AVL:

    class Node:
        def __init__(self, data):
            self.data = data
            self.left: 'AVL.Node' = None
            self.right: 'AVL.Node' = None
            self.height: int = 0

        def __str__(self):
            return str(self.data)

        def get_balance(self):
            h_left = self.left.height if self.left is not None else 0
            h_right = self.right.height if self.right is not None else 0
            return h_left - h_right

        def get_left(self) -> 'AVL.Node':
            return self.__left

        def _set_left(self, data):
            self.__left = data if isinstance(
                data, AVL.Node) else AVL.Node(data)

        def get_right(self):
            return self.__right

        def _set_right(self, data):
            self.__right = data if isinstance(
                data, AVL.Node) else AVL.Node(data)

        def is_node(other):  # sourcery skip: instance-method-first-arg-name
            return isinstance(other, AVL.Node)

    def __init__(self):
        self.root: AVL.Node = None

    def insert(self, data):
        new = data if isinstance(data, AVL.Node) else self.Node(data)
        if self.root is None:
            self.root = new
        else:
            self.__insert(self.root, new)
        return self.root

    def __insert(self, root: 'AVL.Node', new: 'AVL.Node'):
        if root is None:
            root = self.Node(new.data)
            return True
        elif root.data < new.data:
            root.height += 1
            if root.left is None:
                self.__insert(root.left, new)
            else:
                self.__insert(root.right, new)
        root.height = 1 + max(root.left.height, root.right.height)
        bal_fac = root.get_balance()

        if bal_fac > 1 and root.left.data > new.data:
            self.__right_rotate(root)
        elif bal_fac < -1 and new.data > root.right.data:
            self.__left_rotate(root)
        elif bal_fac > 1 and root.left.data < new.data:
            self.__right_left_rotate(root)
        elif bal_fac < -1 and new.data < root.right.data:
            self.__left_right_rotate(root)

    def rebalance(self, root: 'AVL.Node', new: 'AVL.Node'):
        pass

    def __right_rotate(self, node_x: 'AVL.Node'):
        node_y = node_x.left
        node_x.left = node_y.right
        node_y.right = node_x
        return node_y

    def __left_rotate(self, node_x: 'AVL.Node'):
        node_y = node_x.right
        node_x.right = node_x.left
        node_y.left = node_x
        return node_y

    def __right_left_rotate(self, node_x: 'AVL.Node'):
        node_y = node_x.left
        node_x = self.__left_rotate(node_y)
        node_x = self.__right_rotate(node_x)
        return node_x

    def __left_right_rotate(self, node_x: 'AVL.Node'):
        node_y = node_x.right
        node_x = self.__right_rotate(node_y)
        node_y = self.__left_rotate(node_x)
        return node_x

    def __print_tree(self, node: Node, level=0):
        if node != None:
            self.__print_tree(node.get_right(), level + 1)
            print('     ' * level, node)
            self.__print_tree(node.get_left(), level + 1)

    def print_tree(self, node: Node = None):
        node = self.root if node is None else node
        self.__print_tree(node)


class MinHeap:
    def __init__(self):
        self.__FRONT_IDX: int = 1
        self.__heap: list = [None]

    def get_parent_index(self, idx: int):
        return idx//2 if idx > 1 else 1

    def get_left_child_index(self, idx: int):
        return idx*2

    def get_right_child_index(self, idx: int):
        return idx*2 + 1

    def __swap(self, ref_idx: int, des_idx: int):
        heap = self.__heap
        heap[ref_idx], heap[des_idx] = heap[des_idx], heap[ref_idx]

    def __is_leaf(self, pos: int):
        return pos*2 > (len(self.__heap) - 1)

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


class HeapInClass():
    def __init__(self):
        self.__heap: list = [None]

    @property
    def heap(self):
        return self.__heap[1:]

    def insert(self, data: int):
        heap = self.__heap
        idx = len(heap)
        parent_idx = idx//2
        self.__heap.insert(idx, data)
        while idx > 1 and data < self.__heap[parent_idx]:
            heap[idx] = heap[parent_idx]
            idx = parent_idx
            parent_idx = idx//2
        self.__heap[idx] = data

    def tree(self, i: int = None, max_i: int = None):
        i = 1 if i is None else i
        max_i = len(self.__heap)-1 if max_i is None else max_i

        if i <= max_i:
            indent = floor(log2(i+1))-1
            self.tree((i*2)+1, max_i)
            print('\t' * indent, self.__heap[i])
            self.tree((i*2)+2, max_i)


h = [50, 90, 30, 85, 97, 100, 200]
heap = HeapInClass()
for data in h:
    heap.insert(data)
print(heap.heap)
heap.tree()
