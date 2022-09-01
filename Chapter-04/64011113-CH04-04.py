# Relationship

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
    
    def to_list(self):
        return self._items
    
def calculate_relationship(day_cmd):
    class ActivityWithLocation:
        def __init__(self):
            self.activity_queue = Queue()
            self.location_queue = Queue()
            self.__info_queue = Queue()
            self._size = 0
        def __str__(self):
            return str(f"activity {self.activity_queue} \nlocation {self.location_queue}")
        
        def summarize_info_queue(self):
            return str(f"Queue = {', '.join(self.__info_queue._items)}")
        
        def summarize_info(self):
            return str(f"Activity:Location = {', '.join(self.convert_info_to_meaning())}")
        
        def add_day_info(self, day_info):
            self.__info_queue.en_queue(day_info)
            day_info = day_info.split(":")
            self.activity_queue.en_queue(int(day_info[0]))
            self.location_queue.en_queue(int(day_info[1]))
            self._size += 1
            
        def convert_info_to_meaning(self):
            meaning_info = []
            activity = ["Eat", "Game", "Learn", "Movie"]
            location = ["Res.", "ClassR.", "SuperM.", "Home"]
            activity_queue = [activity[i] for i in self.activity_queue._items]
            location_queue = [location[i] for i in self.location_queue._items]
            for i in range(self._size):
                meaning_info.append(str(f"{activity_queue[i]}:{location_queue[i]}"))
            return meaning_info
        
        def get_info_list(self):
            info_list = []
            for i in range(self._size):
                activity = self.activity_queue._items[i]
                location = self.location_queue._items[i]
                info_list.append({"activity": activity, "location": location})
            return info_list

    my_list = ActivityWithLocation()
    your_list = ActivityWithLocation()
    relationship_score = 0
    best_score = 7
    result_relationship = None
    
    day_cmd = [i.split(" ") for i in day_cmd]
    for day_value in day_cmd:
        for info_idx, info_value in enumerate(day_value):
            (my_list if info_idx % 2 == 0 else your_list).add_day_info(info_value)
            
    for day_idx in range(len(day_cmd)):
        my_info = my_list.get_info_list()[day_idx]
        your_info = your_list.get_info_list()[day_idx]
        if  my_info["activity"] == your_info["activity"]:
            if my_info["location"] == your_info["location"]:
                relationship_score += 4
            else: relationship_score += 1
        elif my_info["location"] == your_info["location"]:
            relationship_score += 2
        else: relationship_score -= 5
    
    if relationship_score >= best_score: 
        result_relationship = str(f"Yes! You're my love! : Score is {relationship_score}.")
    elif relationship_score < best_score and relationship_score > 0:
        result_relationship = str(f"Umm.. It's complicated relationship! : Score is {relationship_score}.")
    else: result_relationship = str(f"No! We're just friends. : Score is {relationship_score}.")
    
    print(f"My   {my_list.summarize_info_queue()}")
    print(f"Your {your_list.summarize_info_queue()}")
    print(f"My   {my_list.summarize_info()}")
    print(f"Your {your_list.summarize_info()}")
    print(result_relationship)

input_cmd = input("Enter Input : ").split(",")
calculate_relationship(input_cmd)