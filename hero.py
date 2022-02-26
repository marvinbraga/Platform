import pygame.sprite
from pygame.sprite import AbstractGroup

from core.artefacts import Artefact


class Hero(Artefact):

    def __init__(self, image, x, y, *groups: AbstractGroup):
        super().__init__(image, x, y, *groups)

        self.velocity = 4
        self.gravity = 1
        self.right, self.left, self.jump = False, False, False

    def update(self, *args):
        self.move_by_gravity()
        self.move()

    def move_by_gravity(self):
        self.velocity += self.gravity
        self.rect[1] += self.velocity
        if self.velocity >= 10:
            self.velocity = 10

    def is_collide(self, group, kill):
        return pygame.sprite.spritecollide(self, group, kill)

    def check_events(self, event):
        pass

    def check_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right = True
            elif event.key == pygame.K_LEFT:
                self.left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right = False
            elif event.key == pygame.K_LEFT:
                self.left = False

    def move(self):
        if self.left:
            self.rect[0] -= 8
        elif self.right:
            self.rect[0] += 8