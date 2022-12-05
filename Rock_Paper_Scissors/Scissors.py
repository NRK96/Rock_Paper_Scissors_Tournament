class Scissors:

    def __init__(self, opponent):
        self.opponent = opponent
        self.game_states = {'A':0, 'B':6, 'C':3}
        self.points = 3

    def __str__(self):
        return f'Points from self: {self.points}\nPoints from matchup: {self.game_states[self.opponent]}'

    def resolve_round(self):
        return self.points + self.game_states[self.opponent]