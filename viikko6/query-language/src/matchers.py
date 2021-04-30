class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        ret = False
        for matcher in self._matchers:
            if matcher.matches(player):
                ret = True
        return ret

class All:
    def __init__(self):
        pass

    def matches(self, player):
        return True

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value

class Not:
    def __init__(self, matcher):
        self._matcher = matcher
    
    def matches(self, player):
        return not self._matcher.matches(player)

class PlaysIn:
    def __init__(self, matchers,team):
        self._team = team
        self._matchers = matchers

    def matches(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, matchers,value, attr):
        self._value = value
        self._attr = attr
        self._matchers = matchers

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

