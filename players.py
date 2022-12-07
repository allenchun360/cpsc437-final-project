"""players class"""

class Player:
    """players class"""

    def __init__(self, player_id=None, player=None, team=None, pos=None, average_standard_score=None):
        self._player_id = player_id
        self._player = player
        self._team = team
        self._pos = pos
        self._average_standard_score = average_standard_score

    def get_player_id(self):
        """get player id"""
        return self._player_id

    def get_player(self):
        """get player"""
        return self._player

    def get_team(self):
        """get team"""
        return self._team

    def get_pos(self):
        """get position"""
        return self._pos

    def get_average_standard_score(self):
        return self._average_standard_score

class Kicker:
    """players class"""

    def __init__(self, player=None, Off_abbrev=None, photo=None, average_standard_score=None):
        self._player = player
        self._Off_abbrev = Off_abbrev
        self._photo = photo
        self._average_standard_score = average_standard_score

    def get_player(self):
        """get player"""
        return self._player

    def get_Off_abbrev(self):
        """get team"""
        return self._Off_abbrev

    def get_photo(self):
        """get photo"""
        return self._photo

    def get_average_standard_score(self):
        return self._average_standard_score