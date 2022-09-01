# Color Crush 2

class Queue:
    
    def __init__(self, list=None):
        self._items = [] if list == None else list
    
    def en_queue(self, value):
        self._items.append(value)
        
    def de_last_queue(self, value=1):
        return self._items.pop(-1*value)
        
    def de_queue(self):
        return self._items.pop(0)
    
    def is_empty(self):
        return self._items == []
    
    def size(self):
        return len(self._items)
    
    def __str__(self):
        return ''.join(self._items) if self.size() > 0 else "Empty"
    
    def to_list(self):
        return self._items
    
    def peek(self, index=0):
        return self._items[index] if self.size() > 0 else False
    
    def insert_queue(self, index, value):
        self._items.insert(index, value)
        
    def reverse(self):
        self._items = self._items[::-1]
        return self._items
    
    def last_queue(self, count_last=1):
        return self._items[-1*count_last]
    
def play_color_crush(cmd):
    color_crush_game = ColorCrush2(cmd)
    color_crush_game.play()

class ColorCrush2:
    def __init__(self, cmd):
        self.normal_side = Queue(list(cmd[0]))
        self.mirror_side = Queue(list(cmd[1]))
        self.mirror_side.reverse()
    def play(self):
        reverse = lambda x: x[::-1]
        remaining, explose, interrupter = self.explose()
        print("NORMAL :")
        print(remaining["normal"].size())
        print(remaining["normal"])
        print(f"{explose['normal']} Explosive(s) ! ! ! (NORMAL)")
        
        if interrupter > 0:
            print(f"Failed Interrupted {interrupter} Bomb(s)")

        print("------------MIRROR------------")
        print(reverse("MIRROR :"))
        print(remaining["mirror"].size())
        print(reverse(str(remaining["mirror"])))
        print(f"(RORRIM) ! ! ! (s)evisolpxE {explose['mirror']}")
        
    def explose(self):
        CHAR_BOMB_COUNT = 3
        INSERTED_INDEX = 2
        
        failed_intterupt = 0
        interrupter_char = Queue()
        explose_count = {"mirror": 0, "normal": 0}
        remaining_char = {"mirror": Queue(), "normal": Queue()}
        
        for round in remaining_char:
            side = None
            if round == "normal":
                side = self.normal_side
            elif round == "mirror":
                side = self.mirror_side
                
            while not side.is_empty():
                if side.size() >= CHAR_BOMB_COUNT and side.peek() == side.peek(1) == side.peek(2):
                    if round == "mirror":
                        interrupter_char.en_queue(side.de_queue())
                        self.__remove_char(side, 2)
                        explose_count["mirror"] += 1
                    elif round == "normal":
                        if interrupter_char.size() > 0:
                            if side.peek() == interrupter_char.peek():
                                interrupter_char.de_queue()
                                self.__remove_char(side, 2)
                                failed_intterupt += 1
                            else: 
                                side.insert_queue(INSERTED_INDEX, interrupter_char.de_queue())
                        else:
                            explose_count["normal"] += 1
                            self.__remove_char(side, 3)
                elif remaining_char[round].size() >= INSERTED_INDEX and \
                    remaining_char[round].last_queue() == remaining_char[round].last_queue(2) == side.peek():
                        side.insert_queue(0, remaining_char[round].de_last_queue())
                        side.insert_queue(0, remaining_char[round].de_last_queue())
                else:
                    remaining_char[round].en_queue(side.de_queue())
        remaining_char["normal"].reverse()            
        return remaining_char, explose_count, failed_intterupt
    
    def __remove_char(self, queue, amount):
        for i in range(amount):
            queue.de_queue()

input_cmd = input("Enter Input (Normal, Mirror) : ").split(" ")
play_color_crush(input_cmd)