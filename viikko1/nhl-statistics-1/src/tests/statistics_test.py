import unittest
from statistics import Statistics
from player_reader import PlayerReader
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())
    
    def test_konstruktori_pelaajalista(self):
        self.assertEqual(len(self.stats._pr.get_players()),5)

    def test_search(self):
        kolmas = self.stats._players[3].name
        haettu = self.stats.search(kolmas).name
        self.assertEqual(haettu, kolmas)

    def test_search_tyhjalla(self):
        self.assertIsNone(self.stats.search("Jaska Jokunen"))

    def test_team_eityhja(self):
        pl = self.stats.team("EDM")
        self.assertTrue(len(pl)>0)

    def test_top_scorers(self):
        highest = 0
        for player in self.stats._players:
            score = player.goals + player.assists
            if(score > highest):
                highest = score
        topPlr = self.stats.top_scorers(1)[0]
        self.assertEqual(highest, topPlr.goals + topPlr.assists)