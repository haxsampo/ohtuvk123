class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            score = self.equal_scores()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.a_score_greater_than_3()
        else:
            score = self.different_scores()
        return score

    def different_scores(self):
        return self.pisteen_kirjallinen_vastine(self.m_score1) + "-" + self.pisteen_kirjallinen_vastine(self.m_score2)

    def equal_scores(self):
        if(self.m_score1 > 3):
            score = "Deuce"
        else:
            score = self.pisteen_kirjallinen_vastine(self.m_score1) + "-All"
        return score

    def a_score_greater_than_3(self):
        erotus = self.m_score1 - self.m_score2
        if(abs(erotus)<2):
            return self.etu(erotus)
        else:
            return self.voitto(erotus)

    def voitto(self, erotus):
        if(erotus >=2):
            return "Win for player1"
        else:
            return "Win for player2"
    
    def etu(self, erotus):
        if(erotus == 1):
            return "Advantage player1"
        else:
            return "Advantage player2"
    
    def pisteen_kirjallinen_vastine(self, pisteet):
        if pisteet == 0:
            return "Love"
        elif pisteet == 1:
            return "Fifteen"
        elif pisteet == 2:
            return "Thirty"
        elif pisteet == 3:
            return "Forty"
