class state():
    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def update(self, delta_time, actions):
        pass
    def render(self, surface):
        pass

    def enterState(self):
        if len(self.game.stateStack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.stateStack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()