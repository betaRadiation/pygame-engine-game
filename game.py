import pygame
import time
from states.title import title
from pygame.locals import *

class game:
    def __init__(self):
        self._running = True
        self.fullscreen = False
        self.stateStack = []
        self.screen = None
        self.dt, self.prev_time = 0, 0
        pygame.display.set_caption('Funky game')
        self.size = self.gWidth, self.gHeight = 720, 540
        self.size = self.sWidth, self.sHeight = 720, 540
        self.nWidth = self.sHeight*(4/3)
        self.nHeight = self.sHeight
        self.height = 540
        self.width = 720
        self.gameCanvas = pygame.Surface((self.gWidth,self.gHeight))
        self.actions = {"up": False, "down": False, "left": False, "right": False, "action1": False, "action2": False}
        self.loadStates()
 
    def init(self):
        pygame.init()
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self._running = True

    def loadStates(self):
        self.titleScreen = title(self)
        self.stateStack.append(self.titleScreen)

    def getDT(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def events(self, event):
        # Checks if you quit the game
        if event.type == pygame.QUIT:
            self._running = False
        # Checks all input keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                self.actions["up"] = True
            if event.key == pygame.K_s:
                self.actions["down"] = True
            if event.key == pygame.K_a:
                self.actions["left"] = True
            if event.key == pygame.K_d:
                self.actions["right"] = True
            if event.key == pygame.K_f:
                if self.screen.get_flags() & pygame.FULLSCREEN:
                    self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
                else:
                    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Checks mouse buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.actions["action1"] = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            self.actions["action2"] = True
        # Check if the keys got let go!
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                self.actions["up"] = False
            if event.key == pygame.K_s:
                self.actions["down"] = False
            if event.key == pygame.K_a:
                self.actions["left"] = False
            if event.key == pygame.K_d:
                self.actions["right"] = False
            if event.key == pygame.K_f:
                self.actions["fullscreen"] = False
        # Checks mouse buttons
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.actions["action1"] = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            self.actions["action2"] = False



    def update(self):
        self.stateStack[-1].update(self.dt,self.actions)
        self.height = self.screen.get_height()
        self.width = self.screen.get_width()
        self.nHeight = self.height
        self.nWidth = self.height*(4/3)


    def render(self):
        self.stateStack[-1].render(self.gameCanvas)
        # Render current state to the screen

        self.screen.blit(pygame.transform.scale(self.gameCanvas,(self.nWidth, self.nHeight)), ((self.width/2)-(self.nWidth/2), 0))
#        self.screen.fill((0, 0, 0))
        pygame.display.update()

    def cleanup(self):
        pygame.quit()

    def execute(self):
        if self.init() == False:
            self._running = False
 
        while( self._running ):
            self.getDT()
            for event in pygame.event.get():
                self.events(event)
            self.update()
            self.render()
        self.cleanup()
 
if __name__ == "__main__" :
    theGame = game()
    theGame.execute()