from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, All

class QueryBuilder:
    def __init__(self, matchers = All()):
            self._matchers = matchers

    def build(self):
        return And(self._matchers)

    def playsIn(self,team):
        return QueryBuilder(PlaysIn(self._matchers,team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(self._matchers,value,attr))
