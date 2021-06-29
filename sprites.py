import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.walk_left = False
        self.walk_right = False
        self.walk_up = False
        self.walk_down = False

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        if (self.rect.x) % 64 == 0:
                self.walk_left = False
                self.walk_right = False
        if (self.rect.y) % 64 == 0:
                self.walk_up = False
                self.walk_down = False

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if (self.rect.x) % 64 == 0:
                self.walk_left = True
        
        if keys[pygame.K_RIGHT]:
            if (self.rect.x) % 64 == 0:
                self.walk_right = True

        if keys[pygame.K_UP]:
            if (self.rect.y) % 64 == 0:
                self.walk_up = True

        if keys[pygame.K_DOWN]:
            if (self.rect.x) % 64 == 0:
                self.walk_down = True

        if self.walk_left == True:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'

        if self.walk_right == True:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        
        if self.walk_up == True:
            self.y_change -= PLAYER_SPEED
            self.facing = 'down'

        if self.walk_down == True:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'