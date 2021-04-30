from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, All
from query_builder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #matcher = And(
    #    HasAtLeast(5, "goals"),
    #    HasAtLeast(5, "assists"),
    #    PlaysIn("PHI")
    #)
    query = QueryBuilder()
    matcher = query.playsIn("NYR").hasAtLeast(5,"goals").build()  #

   
    #print(typeof(matcher))    

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
