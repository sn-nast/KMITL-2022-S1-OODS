# Tower of Hanoi

def move(n, A, C, B, maxn):
    if n == 1:
        print(f"move {n} from  {A} to {C}")
        replace_value(n, C)
        show_tower(maxn)
    else:
        move(n-1, A, B, C, maxn)
        print(f"move {n} from  {A} to {C}")
        replace_value(n, C)
        show_tower(maxn)
        move(n-1, B, C, A, maxn)
        
def replace_value(n, next_tower):
    index_a = tower_a.index(str(n)) if str(n) in tower_a else -1
    index_b = tower_b.index(str(n)) if str(n) in tower_b else -1
    index_c = tower_c.index(str(n)) if str(n) in tower_c else -1
    index = None
    tower_focused = None
    
    if index_a != -1:
        index = index_a
        tower_focused = tower_a
    elif index_b != -1:
        index = index_b
        tower_focused = tower_b
    elif index_c != -1:
        index = index_c
        tower_focused = tower_c
        
    tower_moved = None
    if next_tower == "A":
        tower_moved = tower_a
    elif next_tower == "B":
        tower_moved = tower_b
    elif next_tower == "C":
        tower_moved = tower_c
    
    inserted_index = find_inserted_index(tower_moved)
    tower_moved[inserted_index] = str(n)
    tower_focused[index] = "|"

def find_inserted_index(list:list, index=-1):
    if list[index] != "|":
        index = find_inserted_index(list, index-1)
    return index

def show_tower(stop, now=0):
    if stop+1 > now:
        print('  '.join([tower_a[now], tower_b[now], tower_c[now]]))
        show_tower(stop, now=now+1)
    
def make_tower(n):
    global tower_a
    global tower_b
    global tower_c
    tower_a = ['|']
    tower_b = ['|']
    tower_c = ['|']
    tower_b = tower_b*(n+1)
    tower_c = tower_c*(n+1)
    add_value(tower_a, n)

def add_value(list:list, stop, now=1):
    list.append(str(now))
    if now != stop:
        add_value(list, stop, now+1)
    else: 
        return

n = int(input("Enter Input : "))
# n = 4
make_tower(n)
show_tower(n)
move(n, "A", "C", "B", n)