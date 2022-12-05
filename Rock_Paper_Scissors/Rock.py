class Rock:

    def __init__(self, opponent):
        self.opponent = opponent
        self.game_states = {'A':3, 'B':0, 'C':6}
        self.points = 1

    def __str__(self):
        return f'Points from self: {self.points}\nPoints from matchup: {self.game_states[self.opponent]}'

    def resolve_round(self):
        return self.points + self.game_states[self.opponent]