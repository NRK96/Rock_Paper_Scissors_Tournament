class Paper:

    # Initialize our hand.
    def __init__(self, opponent):
        # Your opponent, A = Rock, B = Paper, C = Scissors.
        self.opponent = opponent
        # The various game states, 0 points for a loss, 3 for a draw and 6 for a win.
        self.game_states = {'A':6, 'B':3, 'C':0}
        # The number of points calculated for choosing this hand.
        self.points = 2

    # Define our string, in this case I want to display the number of points the current matchup yields.
    def __str__(self):
        return f'Points from self: {self.points}\nPoints from matchup: {self.game_states[self.opponent]}'

    # Return the points generated by the current matchup.
    def resolve_round(self):
        return self.points + self.game_states[self.opponent]
