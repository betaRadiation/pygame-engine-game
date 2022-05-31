from states.baseState import state
from pygame.locals import *
import pygame

class gameWorld(state):
    def __init__(self, game):
        state.__init__(self, game)
        

    def update(self, delta_time, actions):
        pass
        # if actions["action1"]:
            # new_state = Game_World(self.game)
            # new_state.enter_state()
        # self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        pygame.draw.rect(display, (20, 0, 0), (50,60,800,200))
        pygame.draw.rect(display, (60, 30, 0), (700,90,60,100))