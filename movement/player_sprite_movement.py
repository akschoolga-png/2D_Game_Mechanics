import pygame
from movement.config import *

class Player_move(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self._layer = ppg_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        #REPLACE IMAGE WITH SPRITE OF CHOICE

        self.rect = self.image.get_rect() #hitbox
        self.rect.x = self.x
        self.rect.y = self.y
        self.facing = 'down'

        self.x_change = 0 #changes in loop
        self.y_change = 0

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.collide('x')
        self.rect.y += self.y_change
        self.collide('y')

        self.x_change, self.y_change = 0, 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= ppg_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += ppg_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= ppg_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += ppg_SPEED
            self.facing = 'down'

    def collide(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom


class blocks(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = blocks_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        #REPLACE BLOCK IMAGE WITH GRAPHIC OF CHOICE
        #CREATE MORE OPTIONS OF IMAGE CHOICE IF NEEDED

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
