import pygame

from core.artefacts import Artefact
from core.background_manager import Background
from core.enemy import Enemy
from core.scene import Scene
from hero import Hero


class Game(Scene):

    def __init__(self):
        super().__init__()
        self.valid_keys = [
            pygame.K_LEFT,
            pygame.K_RIGHT,
            pygame.K_SPACE,
        ]

        self.all_platforms = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.all_crystals = pygame.sprite.Group()

        self.background = Background("assets/bg.png", 0, 0, self.all_sprites)

        self.tree1 = Artefact("assets/tree1.png", 80, 250, self.all_sprites)
        self.tree2 = Artefact("assets/tree2.png", 450, 250, self.all_sprites)
        self.tree3 = Artefact("assets/tree1.png", 1060, 250, self.all_sprites)

        self.plat1 = Artefact("assets/plat1.png", 50, 550, self.all_sprites, self.all_platforms)
        self.plat2 = Artefact("assets/plat3.png", 430, 550, self.all_sprites, self.all_platforms)
        self.plat3 = Artefact("assets/plat2.png", 1080, 550, self.all_sprites, self.all_platforms)

        self.crystal1 = Artefact("assets/crystal.png", 520, 300, self.all_sprites, self.all_crystals)
        self.crystal2 = Artefact("assets/crystal.png", 870, 300, self.all_sprites, self.all_crystals)
        self.crystal3 = Artefact("assets/crystal.png", 1155, 300, self.all_sprites, self.all_crystals)

        self.enemy1 = Enemy(520, 502, self.all_sprites, self.all_enemies)
        self.player = Hero("assets/idle0.png", 100, 250, self.all_sprites)

        self.hud = Artefact("assets/hud.png", 50, 50, self.all_sprites)

    def update(self):
        super().update()
        self.check_platform()
        self.check_crystal()
        self.check_enemy()

    def check_platform(self):
        platform = self.player.is_collide(self.all_platforms, False)
        if platform:
            self.player.rect.bottom = platform[0].rect.top

    def check_crystal(self):
        crystal = self.player.is_collide(self.all_crystals, True)
        if crystal:
            self.player.points += 1

    def check_enemy(self):
        enemy = self.player.is_collide(self.all_enemies, False)
        if enemy:
            if self.player.rect.y + 90 < enemy[0].rect.top:
                self.player.velocity *= -1
                enemy[0].kill()
            else:
                self.player.rect[0] -= 16
                enemy[0].kill()
                self.player.power -= 1

    def check_events(self, event):
        self.player.check_events(event)

    def check_keys(self, event):
        self.player.check_keys(event)
