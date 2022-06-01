from states.baseState import state
from states.gameWorld import gameWorld
from pygame.locals import *
import pygame

class title(state):
    def __init__(self, game):
        state.__init__(self, game)

    def update(self, delta_time, actions):
        pass
        if actions["start"]:
            newState = gameWorld(self.game)
            newState.enterState()

    def render(self, display):
        display.fill((255,255,255))
        self.game.drawText(self.game.gameCanvas, "Welcome to video my game.", (0,0,0), 260, 30)
        self.game.drawText(self.game.gameCanvas, "press enter to play.", (0,0,0), 260, 200)