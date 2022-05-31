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
        pygame.draw.rect(display, (20, 0, 0), (10,20,100,100))
        pygame.draw.rect(display, (60, 30, 0), (500,20,60,100))