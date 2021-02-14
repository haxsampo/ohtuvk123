class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.score = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20}"  +" team "+ self.team +" goals "+ str(self.goals) +" assists "+ str(self.assists)

    def __lit__(self, other):
        return self.goals+self.assists < other.goals+other.assists