class Paper:

    def __init__(self, opponent):
        self.opponent = opponent
        self.game_states = {'A':6, 'B':3, 'C':0}
        self.points = 2

    def __str__(self):
        return f'Points from self: {self.points}\nPoints from matchup: {self.game_states[self.opponent]}'

    def resolve_round(self):
        return self.points + self.game_states[self.opponent]