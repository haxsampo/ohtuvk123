class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        players1 = filter(lambda plr: filterByNat(plr, nationality), self.players)
        players = sorted(players1, key=lambda player: player.score,reverse=True)
        return players

def filterByNat(player, nat):
    if player.nationality == nat:
        return True
    else:
        return False

    