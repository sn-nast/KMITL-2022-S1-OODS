# Mondstadt

class Mondstadt:
    
    class Knight:
        def __init__(self, number: int, power: int):
            self.power = power if power > 0 else 0
            self.number = number if number > 0 else 0
        
    def __init__(self):
        self._knights: list[Mondstadt.Knight] = []
        self._n_knights = 0
        self._power = 0
    
    def add_knight(self, powers):
        powers = [int(x) for x in powers.split(" ")] if isinstance(powers, str) else powers
        for x in powers:
            new = self.Knight(self.get_n_knights(), x)
            self._knights.append(new)
            self._power += x
    
    def get_n_knights(self):
        return self._n_knights
    
    def get_knights(self):
        return self._knights
    
    def get_power(self):
        return self._power
    
    def compare_group(self, groups):
        groups = [[int(x) for x in pair.split(" ")] for pair in groups.split(",")] \
            if isinstance(groups, str) else groups
        knights = self.get_knights()
        for group in groups:
            a, b = group
            team_power = [knights[a].power, knights[b].power]
            for i, value in enumerate(group):
                member_1, member_2 = 2*value + 1, 2*value + 2
                if member_1 < len(knights):
                    team_power[i] += knights[member_1].power
                if member_2 < len(knights):
                    team_power[i] += knights[member_2].power
            
            if team_power[0] < team_power[1]:
                print(f"{a}<{b}")
            elif team_power[0] > team_power[1]:
                print(f"{a}>{b}")
            elif team_power[0] == team_power[1]:
                print(f"{a}={b}")
            else:
                print("error")
                

power, compare = input('Enter Input : ').split('/')
# power, compare = "4 5/0 1,1 0".split('/')

land = Mondstadt()
land.add_knight(power)
print(land.get_power())
land.compare_group(compare)