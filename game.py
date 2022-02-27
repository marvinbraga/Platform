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

        Artefact("assets/tree1.png", 80, 250, self.all_sprites)
        Artefact("assets/tree2.png", 450, 250, self.all_sprites)
        Artefact("assets/tree1.png", 1060, 250, self.all_sprites)

        Artefact("assets/plat1.png", 50, 550, self.all_sprites, self.all_platforms)
        Artefact("assets/plat3.png", 430, 550, self.all_sprites, self.all_platforms)
        Artefact("assets/plat2.png", 1080, 550, self.all_sprites, self.all_platforms)

        Artefact("assets/crystal.png", 520, 300, self.all_sprites, self.all_crystals)
        Artefact("assets/crystal.png", 870, 300, self.all_sprites, self.all_crystals)
        Artefact("assets/crystal.png", 1155, 300, self.all_sprites, self.all_crystals)

        Enemy(520, 502, self.all_sprites, self.all_enemies)
        Enemy(800, 502, self.all_sprites, self.all_enemies)
        Enemy(1100, 502, self.all_sprites, self.all_enemies)

        self.player = Hero("assets/idle0.png", 100, 250, self.all_sprites)
        self.hud = Artefact("assets/hud.png", 50, 50, self.all_sprites)

        self.is_finished = False

    def update(self):
        super().update()
        self.check_platform()
        self.check_crystal()
        self.check_enemy()
        self.check_drop()
        self.check_is_finished()

    def check_is_finished(self):
        self.is_finished = self.player.power <= 0
        if self.is_finished:
            self.change_scene = True

    def check_platform(self):
        platform = self.player.is_collide(self.all_platforms, False)
        if platform:
            if self.player.rect[1] + 50 < platform[0].rect.top:
                if self.player.rect.left + 30 <= platform[0].rect.right:
                    if self.player.rect.right - 30 >= platform[0].rect.left:
                        self.player.rect.bottom = platform[0].rect.top

    def check_crystal(self):
        crystal = self.player.is_collide(self.all_crystals, True)
        if crystal:
            self.player.points += 1
            self.update_hud_crystals()

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
                self.update_hud_enemies()

    def check_events(self, event):
        self.player.check_events(event)

    def check_keys(self, event):
        self.player.check_keys(event)

    def update_hud_crystals(self):
        pos = [136, 160, 185]
        Artefact("assets/icon_crystal.png", pos[self.player.points - 1], 126, self.all_sprites)

    def update_hud_enemies(self):
        pos = [216, 177, 140]
        Artefact("assets/icon_head.png", pos[self.player.power], 81, self.all_sprites)

    def check_drop(self):
        if self.player.power > 0:
            if self.player.rect.y > 720:
                self.player.rect.x, self.player.rect.y = 100, 250
                self.player.power -= 1
                self.update_hud_enemies()
