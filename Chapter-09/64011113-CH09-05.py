# Premier League Score

class Team:
    def __init__(self, data):
        self.name = data[0]
        self.wins = int(data[1])
        self.loss = int(data[2])
        self.draws = int(data[3])
        self.scored = int(data[4])
        self.conceded = int(data[5])
    
    def get_total_point(self):
        point = {'win': 3, 'draw': 1, 'loss': 0}
        return self.wins*point['win'] + self.draws*point['draw']
    
    def get_goal_dif(self):
        return self.scored-self.conceded
    
    def get_info(self):
        return [
            self.name,
            {'point': self.get_total_point()},
            {'gd': self.get_goal_dif()}
        ]
        
class Sort:
    def sort_point(self, list):
        for i in range(1, len(list)):
            i_data = list[i]
            for j in range(i, -1, -1):
                if i_data.get_total_point() > list[j-1].get_total_point() \
                    and j > 0:
                    list[j] = list[j-1]
                else:
                    list[j] = i_data
                    break
        list = self.sort_goal_diff(list)
        return list
    
    def sort_goal_diff(self, list):
        for i in range(0, len(list)):
            if i < len(list)-1 :
                idx = i
                for x in range(i, len(list)):
                    if list[x].get_total_point() == list[x+1].get_total_point():
                        idx += 1
                    else: 
                        break
                for last in range(idx, i-1, -1):
                    for x in range(i, last):
                        if list[x].get_goal_dif() < list[x+1].get_goal_dif():
                            list[x], list[x+1] = list[x+1], list[x]
        return list
    
input = [i.split(',') for i in [x for x in input("Enter Input : ").split("/")]]
teams = []
print("== results ==")

for i in input:
    teams.append(Team(i))

Sort.sort_point(teams)

for i in teams:
    print(i.get_info())