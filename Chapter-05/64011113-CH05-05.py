# Scramble

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def is_empty(self):
        return self.head == None
    
    def append(self, item):
        p = Node(item)
        if self.is_empty():
            self.head = p
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = p
    
    def add_head(self, item):
        p = Node(item)
        if self.is_empty():
            self.append(item)
        else:
            p.next = self.head
            self.head = p
    
    def search(self, item):
        p = Node(item)
        temp = self.head
        if self.is_empty():
            return 'Not Found'
        while temp.value != None:
            if temp.value == p.value: return 'Found'
            elif temp.next is None: return 'Not Found'
            temp = temp.next
    
    def index(self, item):
        p = Node(item)
        temp = self.head
        index = 0
        if self.is_empty():
            return -1
        while temp.value != None:
            if temp.value == p.value: return index
            elif temp.next is None: return -1
            temp = temp.next
            index += 1
    
    def size(self):
        size = 0
        temp = self.head
        if self.is_empty():
            return size
        while temp.value != None:
            size += 1
            if temp.next is None: return size
            temp = temp.next
    
    def pop(self, pos=0):
        temp = self.head
        index = 0
        pop_value = None
        if self.is_empty():
            return pop_value
        while temp.value != None:
            if index == pos:
                pop_value = temp.value
                if self.size() == 1:
                    self.head = None
                elif self.size() == 2:
                    self.head = temp.next
                return pop_value
            elif index == pos-1:
                pop_value = temp.value
                temp.next = temp.next.next
                return pop_value
            elif temp.next is None: return pop_value
            temp = temp.next
            index += 1

    def __str__(self):
        return str(self.value)

def createLL(LL):
    list = LinkedList()
    for i in LL:
        list.append(i)
    return list.head

def printLL(head):
    temp = head
    list_str = head.value
    while temp.next != None:
        list_str += " " + str(temp.next.value)
        temp = temp.next
    return list_str

def SIZE(head):
    temp = head
    size = 0
    while temp != None:
        size += 1
        temp = temp.next
    return size

def scarmble(head, b, r, size):
    b_amount = int((size * b)/100)
    r_amount = int((size * r)/100)

    bottom_up_list = LinkedList()
    temp = head
    for count in range(1, size+1):
        if count > b_amount:
            bottom_up_list.append(temp.value)
        if count == size:
            sub_temp = head
            for count_lift in range(1, b_amount+1):
                bottom_up_list.append(sub_temp.value)
                sub_temp = sub_temp.next
        temp = temp.next
    
    riffle_list = LinkedList()
    temp_riffle_list_1 = LinkedList()
    temp_riffle_list_2 = LinkedList()
    
    temp = bottom_up_list.head
    for count in range(1, size+1):
        if count > r_amount:
            temp_riffle_list_2.append(temp.value)
        else:
            temp_riffle_list_1.append(temp.value)
        temp = temp.next
        
    riffle_1 = temp_riffle_list_1.head
    riffle_2 = temp_riffle_list_2.head
    for count in range(1, size+1):
        if riffle_1 != None and riffle_2 != None:
            if count % 2 == 0 and count <= r_amount*2:
                riffle_list.append(riffle_2.value)
                riffle_2 = riffle_2.next
            elif riffle_1 != None:
                riffle_list.append(riffle_1.value)
                riffle_1 = riffle_1.next
    while riffle_2 != None:
        riffle_list.append(riffle_2.value)
        riffle_2 = riffle_2.next
    while riffle_1 != None:
        riffle_list.append(riffle_1.value)
        riffle_1 = riffle_1.next
        
    print('BottomUp {:.3f} % : {}'.format(b, printLL(bottom_up_list.head)))
    print('Riffle {:.3f} % : {}'.format(r, printLL(riffle_list.head)))
    print('Deriffle {:.3f} % : {}'.format(r, printLL(bottom_up_list.head)))
    print('Debottomup {:.3f} % : {}'.format(b, printLL(head)))
    
inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)