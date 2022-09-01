# Queue #2

class Queue:
    
    def __init__(self, list=None):
        self._items = [] if list == None else list
    
    def en_queue(self, value):
        self._items.append(value)
        
    def de_queue(self):
        return self._items.pop(0)
    
    def is_empty(self):
        return self._items == []
    
    def size(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items) if self.size() > 0 else "[]"

def calculate_queue(people, time_in_minute):
    main_row = Queue(people)
    cashier_1_row = Queue()
    cashier_2_row = Queue()
    cashier_1_time_spent = 3
    cashier_2_time_spent = 2
    max_people_per_row = 5
    time_start_cashier_2 = 0
    
    for minute in range(1, time_in_minute+1):

        if minute > 3 and \
            minute % cashier_1_time_spent == 1 and \
            not cashier_1_row.is_empty():
            cashier_1_row.de_queue()
        if (minute - time_start_cashier_2) >= 2 and\
            (minute - time_start_cashier_2) % cashier_2_time_spent == 0 and \
            not cashier_2_row.is_empty():
            cashier_2_row.de_queue()
        
        if not main_row.is_empty():    
            if cashier_1_row.size() == max_people_per_row:
                if cashier_2_row.is_empty(): time_start_cashier_2 = minute                    
                cashier_2_row.en_queue(main_row.de_queue())
            else:
                cashier_1_row.en_queue(main_row.de_queue())

        print(f"{minute} {main_row} {cashier_1_row} {cashier_2_row}")

people, time = input("Enter people and time : ").split(" ")
people = list(people)
time = int(time)
calculate_queue(people, time)