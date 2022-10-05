class SLL:
    class Node:
        def __init__(self, value, next: 'SLL.Node' =None):
            self.value = value
            self.next = next
            
    def __init__(self, head: Node = None):
        self.head = head
        self.size = 0 if head is None else 1
    
    def __str__(self):
        if self.is_empty(): return 'Empty'
        temp_node = self.head
        list_string = str(temp_node.value) + ' '
        while temp_node.next != None:
            list_string += str(temp_node.next.value) + ' '
            temp_node = temp_node.next
        return list_string
    
    def append(self, *items):
        for item in items:
            new = self.Node(item)
            if self.is_empty():
                self.head = new
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = new
            self.size += 1
        
    # ทวน
    def is_empty(self):
        return self.head == None
    
    def add_head(self, item):
        new = self.Node(item)
        if self.is_empty():
            self.append(item)
        else:
            new.next = self.head
            self.head = new
    
    def search(self, item):
        checking_node = self.Node(item)
        temp_node = self.head
        if self.is_empty(): 
            return "Not Found"
        while temp_node.value != None:
            if temp_node.value == checking_node.value: return 'Found'
            elif temp_node.next is None: return 'Not Found'
            temp_node = temp_node.next
    
    def index(self, item):
        if self.is_empty(): return -1
        
        checking_node = self.Node(item)
        temp_node = self.head
        index = 0
        while temp_node.value != None:
            if temp_node.value == checking_node.value: return index
            elif temp_node.next is None: return -1
            temp_node = temp_node.next
            index += 1
            
    def pop(self, pos: int = 0):
        temp_node = self.head
        index = 0
        while temp_node != None:
            if pos == index:
                if self.size == 1:
                    self.head = None
                elif self.size == 2:
                    self.head = temp_node.next
                elif pos == 0:
                    self.head = self.head.next
                self.size -= 1
                return 'Success'
            elif index == pos-1:
                temp_node.next = temp_node.next.next
                self.size -= 1
                return 'Success'
            elif temp_node.next is None: return 'Out of Range'
            temp_node = temp_node.next
            index += 1
            
    def concat(self, list:'SLL'):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = list.head
        
    def peek(self) -> Node:
        temp = self.head
        while temp.next != None:
            temp = temp.next
        return temp
    
def createLL(LL:list):
    list = SLL()
    for i in LL:
        list.append(i)
    return list.head

def printLL(head: SLL.Node):
    temp = head
    list_str = str(head.value) + ' '
    while temp.next != None:
        list_str += str(temp.next.value) + ' '
        temp = temp.next
    return list_str

def SIZE(head: SLL.Node):
    temp = head
    size = 0
    while temp != None:
        size += 1
        temp = temp.next
    return size

def scarmble(head: SLL.Node, b, r, size):
    b_amount = int((size * b)/100)
    r_amount = int((size * r)/100)
    bottom_up_list = make_bottom_up(head, b_amount, size)
    riffle_list = make_riffle(bottom_up_list.head, r_amount, size)
    print('BottomUp {:.3f} % : {}'.format(b, printLL(bottom_up_list.head)))
    print('Riffle {:.3f} % : {}'.format(r, printLL(riffle_list.head)))

def make_bottom_up(head: SLL.Node, n, size: int):
    list = SLL()
    cut_list = SLL()
    temp = head
    for count in range(1, size+1):
        if count > n:
            list.append(temp.value)
        elif count <= n:
            cut_list.append(temp.value)
        temp = temp.next
    list.concat(cut_list)
    return list
    
def make_riffle(head: SLL.Node, n, size: int):
    list = SLL()
    cut_list = SLL()
    remain_list = SLL()
    temp = head
    for count in range(1, size+1):
        if count <= n:
            cut_list.append(temp.value)
        else:
            remain_list.append(temp.value)
        temp = temp.next
    
    riffle_1 = cut_list.head
    riffle_2 = remain_list.head
    for count in range(1, size+1):
        if riffle_1 != None and riffle_2 != None:
            if count % 2 == 0 and count <= n*2:
                list.append(riffle_2.value)
                riffle_2 = riffle_2.next
            else:
                list.append(riffle_1.value)
                riffle_1 = riffle_1.next
    
    if riffle_1 != None:
        x = list.peek()
        x.next = riffle_1
    if riffle_2 != None:
        x = list.peek()
        x.next = riffle_2
    return list

inp1, inp2 = "1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 62,B 23".split('/')
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