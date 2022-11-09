# Rehashing

class Data:
    def __init__(self, key, value):
        self.key: str = key
        self.value: str = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)
    
